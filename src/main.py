import os

from src.hh_api_class import HhAPI
from src.get_add_delete_class import JsonFormatSave
from src.vacancy_class import Vacancy
import json
from pathlib import Path


def get_value(dictionary, *keys):
    """
    Возвращает значение из словаря по заданному пути ключей, где dictionary - это словарь, из которого мы получаем значение, ф
    keys - переменное количество ключей в виде строки, определяющих путь к значению.
    Если хотя бы один ключ не существует или путь прерывается значениями None, будет возвращено None.
    """
    for key in keys:
        if dictionary is None:
            return None
        dictionary = dictionary.get(key)
    return dictionary


def interaction():
    print('''С помощью этой программы поиск вакансий на Hh.ru станет удобнее.
          Гайд по работе с программой:
          1. Ключевые слова нужно разделять пробелами
          2.Количество вакансий указывать только целыми числами, иначе будут выданы все найденные по имени вакансии

          Если не будет найдено ни одного совпадения по ключевым словам,
          то программа вернет количество вакансий, указанных в следующем вводе''')

    name_vacancy = input('Введите название вакансии: ')
    keyword_vacancy = input('Введите ключевые слова для поиска: ').split()

    try:
        top_n = int(input('Введите количество ваканский для отображения по убыванию зарплаты: '))
        if top_n <= 0:
            raise ValueError
    except ValueError:
        print('Получено некорректное значение. Будут выданы все результаты:')
        top_n = None

    vacancy_hh = HhAPI()
    all_vacancy = vacancy_hh.get_vacancies(name_vacancy)
    all_vacancy = [vacancy for vacancy in all_vacancy.get('items') if get_value(vacancy, 'salary', 'currency') == 'RUR']

    if len(all_vacancy) == 0:
        print("Таких вакансий нет, попробуйте изменить параметры поиска")
    else:
        print(f"Всего количество вакансий по запросу '{name_vacancy}': {len(all_vacancy)}")
        print(f"Топ {top_n} вакансий по зарплате:")

        suitable_vacancy = []

        if not keyword_vacancy:
            top_n_vacancy = top_n
            for vacancy in all_vacancy[:top_n_vacancy]:
                try:
                    name = get_value(vacancy, 'name')
                    area = get_value(vacancy, 'area', 'name')
                    salary_from = get_value(vacancy, 'salary', 'from')
                    salary_currency = get_value(vacancy, 'salary', 'currency')
                    requirement = get_value(vacancy, 'snippet', 'requirement')
                    suitable_vacancy.append(
                        Vacancy(name, area, salary_from, salary_currency, requirement))
                except Exception as e:
                    print(f"Ошибка обработки: {e}")

        else:
            for vacancy in all_vacancy:
                try:
                    name = get_value(vacancy, 'name')
                    area = get_value(vacancy, 'area', 'name')
                    salary_from = get_value(vacancy, 'salary', 'from')
                    salary_currency = get_value(vacancy, 'salary', 'currency')
                    requirement = get_value(vacancy, 'snippet', 'requirement')
                    if any(keyword.lower() in str(vacancy).lower() for keyword in keyword_vacancy):
                        suitable_vacancy.append(
                            Vacancy(name, area, salary_from, salary_currency, requirement,))
                except Exception as e:
                    print(f"Ошибка обработки вакансии: {e}")

        if len(suitable_vacancy) == 0:
            top_n_vacancy = top_n or len(all_vacancy)
            print(f"Ключевые слова не найдены. Будут выданы все результаты: {top_n_vacancy} вакансий.")
            good_vacancy = all_vacancy[:top_n_vacancy]
        else:
            top_vacancy = sorted(suitable_vacancy, key=lambda x: x.salary_from if x.salary_from is not None else 0,
                                 reverse=True)
            good_vacancy = top_vacancy[:top_n]

        for vacancy in good_vacancy:
            print(vacancy)

    with open(os.path.join('CourseW4', 'vacancies.json', 'w')) as file:
        json.dump(suitable_vacancy, file,
                  default=lambda x: x.__dict__)


if __name__ == "__main__":
    interaction()

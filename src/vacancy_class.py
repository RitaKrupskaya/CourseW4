class Vacancy:
    """
    Класс для представления вакансий
    """

    def __init__(self, name, city, salary_from, currency, requirements):
        self.name = name
        self.city = city
        self.salary_from = salary_from
        self.currency = currency
        self.requirements = requirements

        self.validate_data()

    def __repr__(self):
        """
        Отладочное строковое представление объекта класса Vacancy
        """
        return (f"""
                Название вакансии: {self.name}
                Город: {self.city}
                Заработная плата от: {self.salary_from} {self.currency}
                Требования: {self.requirements}
                """)

    @staticmethod
    def filtered_by_city(vacancies, name_of_city):
        return [vacancy for vacancy in vacancies if vacancy.city == name_of_city]

    def validate_data(self) -> int:
        """
        Валидация данных о вакансии, eсли зарплата не указана, устанавливает значение 0 для salary_from.
        """
        if not self.salary_from:
            self.salary_from = 0

    def __eq__(self, other) -> bool:
        """
        Проверка равенства вакансий по атрибутам. Вернет True, если атрибуты двух вакансий (self и other) равны
        """
        return (self.name == other.name and self.city == other.city and self.salary_from == other.salary_from
                and self.requirements == other.requirements)

    def __lt__(self, other) -> bool:
        """
        Метод для сравнения вакансий по ЗП. Вернет True, если зарплата текущей вакансии (self) меньше зарплаты второй вакансии (other)
        """
        return self.salary_from < other.salary_from




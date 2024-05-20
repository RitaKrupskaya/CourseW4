import json
from abc import ABC, abstractmethod


class FileWorker(ABC):

    @abstractmethod
    def add_vacancy(self, *agrs, **kwargs):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass

    @abstractmethod
    def delete_vacancy(self):
        pass


class JsonFormatSave(FileWorker):
    """
    Класс для сохранения и получения вакансий в JSON-файл
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancy_data):
        with open(self.file_name, 'a') as file:
            json.dump(vacancy_data, file)
            file.write('\n')

    def get_vacancies(self):
        with open(self.file_name, 'r') as file:
            vacancies = json.load(file)
            return vacancies

    def delete_vacancy(self):
        pass


class TxtVacancy(FileWorker):
    """
    Класс для сохранения, получения и удаления вакансий из .txt-файла
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def add_vacancy(self, vacancy_data):
        with open(self.file_name, 'a') as file:
            file.write(str(vacancy_data) + '\n')

    def get_vacancies(self):
        with open(self.file_name, 'r') as file:
            return file.readlines()

    def delete_vacancy(self):
        pass

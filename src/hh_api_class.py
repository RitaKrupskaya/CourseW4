import requests
from abc import ABC, abstractmethod


class APIVacHH(ABC):
    """
    Абстрактный класс для работы с API сервиса
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HhAPI(APIVacHH):
    """
    Подключается к API hh.ru и получает вакансии по ключевому слову
    """

    def get_vacancies(self, keyword):
        """
        Получает вакансии по ключевому слову из API сервиса по поиску вакансий
        """
        url = 'https://api.hh.ru/vacancies'
        params = {'text': keyword}
        response = requests.get(url, params=params)
        data = response.json()
        return data

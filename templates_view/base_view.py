from abc import ABC, abstractmethod
from render_template import render_template


class View():
    """
    Базовый класс для представлений веб-страниц.

    Атрибуты:
    template (str): Путь к шаблону страницы. Должен быть переопределен в подклассах.

    Методы:
    get(self, environ): Абстрактный метод для обработки GET-запросов. 
                        Должен быть реализован в каждом подклассе.
    """
    template = ''

    @abstractmethod
    def get(self, environ):
        """
        Абстрактный метод для обработки GET-запросов. 

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Должен быть реализован в каждом подклассе.
        """
        pass

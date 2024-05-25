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

    def get(self, environ):
        """
        Абстрактный метод для обработки GET-запросов. 

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Должен быть реализован в каждом подклассе.
        """
        pass


    def post(self, environ):
        """
        Метод для обработки POST-запросов.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Может быть реализован в подклассе, если требуется обработка POST-запросов.
        """
        pass

    def handle(self, environ):
        """
        Метод для обработки запросов и вызова соответствующих методов GET или POST.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Возвращает:
        tuple: Данные ответа и тип контента.
        """
        method = environ['REQUEST_METHOD']
        if method == 'POST' and hasattr(self, 'post'):
            return self.post(environ)
        else:
            return self.get(environ)

from response import Response
from templates_view.base_view import View
from render_template import render_template


class ErrorView(View):
    """
    Класс представляет собой представление страницы ошибки 404.

    Атрибуты:
    template (str): Путь к шаблону страницы ошибки 404.

    Методы:
    get(self, environ): Метод обрабатывает GET-запросы к странице ошибки 404.
    """
    template = 'templates/404.html'

    def get(self, environ):
        """
        Метод обрабатывает GET-запросы к странице ошибки 404.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Возвращает:
        str: Возвращает HTML-страницу ошибки 404.
        """
        data = render_template(template_name=self.template, context={})
        return Response(data=data, content_type='text/html', code=404)

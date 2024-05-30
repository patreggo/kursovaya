from response import Response
from templates_view.base_view import View
from render_template import render_template


class TemplateView(View):
    """
    Класс представляет собой общее представление для загрузки шаблонов.

    Атрибуты:
    template (str): Путь к шаблону.

    Методы:
    get(self, environ): Метод обрабатывает GET-запросы и возвращает HTML-страницу.
    """
    template = ''
    status_code = 200

    def get(self, environ):
        """
        Метод обрабатывает GET-запросы и возвращает HTML-страницу.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Возвращает:
        str: Возвращает HTML-страницу.
        """
        data = render_template(template_name=self.template, context={})
        return Response(data=data, content_type='text/html', code=self.status_code)

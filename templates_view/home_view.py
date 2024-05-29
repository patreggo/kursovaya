from response import Response
from templates_view.base_view import View
from render_template import render_template


class HomeView(View):
    """
    Класс представляет собой представление главной страницы.

    Атрибуты:
    template (str): Путь к шаблону главной страницы.

    Методы:
    get(self, environ): Метод обрабатывает GET-запросы к главной странице.
    """
    template = 'templates/index.html'
    
    def get(self, environ):
        """
        Метод обрабатывает GET-запросы к главной странице.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Возвращает:
        str: Возвращает HTML-страницу главной страницы.
        """
        data = render_template(template_name=self.template, context={})
        return Response(data=data, content_type='text/html', code=200)
from response import Response
from templates_view.base_view import View
from render_template import render_template


# Класс представления заказа
class CheckoutView(View):
    """
    Класс представляет собой представление страницы оформления заказа.

    Атрибуты:
    template (str): Путь к шаблону страницы оформления заказа.

    Методы:
    get(self, environ): Метод обрабатывает GET-запросы к странице оформления заказа.
    """
    template = 'templates/checkout.html'

    def get(self, environ):
        """
        Метод обрабатывает GET-запросы к странице оформления заказа.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Возвращает:
        str: Возвращает HTML-страницу оформления заказа.
        """
        data = render_template(template_name=self.template, context={})
        return Response(data=data, content_type='text/html', code=200)

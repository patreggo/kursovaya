from templates_view.base_view import View
from render_template import render_template


class ProductView(View):
    """
    Класс представляет собой представление страницы продукта.

    Атрибуты:
    template (str): Путь к шаблону страницы продукта.

    Методы:
    get(self, environ): Метод обрабатывает GET-запросы к странице продукта.
    """
    template = 'templates/product_page.html'
    
    def get(self, environ):
        """
        Метод обрабатывает GET-запросы к странице продукта.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Возвращает:
        str: Возвращает HTML-страницу продукта.
        """
        return render_template(template_name=self.template, context={})
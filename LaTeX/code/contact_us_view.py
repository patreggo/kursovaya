from templates_view.base_view import View
from render_template import render_template

class ContactUsView(View):
    """
    Класс представляет собой представление страницы " О нас ".

    Атрибуты:
    template (str): Путь к шаблону страницы " О нас ".

    Методы:
    get(self, environ): Метод обрабатывает GET-запросы к странице " О нас ".
    """
    template = 'templates/contact.html'
    
    
    def get(self, environ):
        """
        Метод обрабатывает GET-запросы к странице " О нас ".

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.

        Возвращает:
        str: Возвращает HTML-страницу " О нас ".
        """
        return render_template(template_name=self.template, context={})

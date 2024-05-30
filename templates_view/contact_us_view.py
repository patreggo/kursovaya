from templates_view.template_view import TemplateView


class ContactUsView(TemplateView):
    """
    Класс представляет собой представление страницы " О нас ".

    Атрибуты:
    template (str): Путь к шаблону страницы " О нас ".

    Методы:
    get(self, environ): Метод обрабатывает GET-запросы к странице " О нас ".
    """
    template = 'templates/contact.html'


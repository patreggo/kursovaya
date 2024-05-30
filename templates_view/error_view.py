from templates_view.base_view import View
from templates_view.template_view import TemplateView


class ErrorView(TemplateView):
    """
    Класс представляет собой представление страницы ошибки 404.

    Атрибуты:
    template (str): Путь к шаблону страницы ошибки 404.

    """
    template = 'templates/404.html'

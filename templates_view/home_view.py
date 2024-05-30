from templates_view.template_view import TemplateView


class HomeView(TemplateView):
    """
    Класс представляет собой представление главной страницы.

    Атрибуты:
    template (str): Путь к шаблону главной страницы.
    """
    template = 'templates/index.html'

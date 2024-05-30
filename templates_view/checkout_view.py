from templates_view.template_view import TemplateView


# Класс представления заказа
class CheckoutView(TemplateView):
    """
    Класс представляет собой представление страницы оформления заказа.

    Атрибуты:
    template (str): Путь к шаблону страницы оформления заказа.

    """
    template = 'templates/checkout.html'

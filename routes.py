from json_product.get_products import GetProducts
from templates_view.checkout_view import CheckoutView
from templates_view.contact_us_view import ContactUsView
from templates_view.error_view import ErrorView
from templates_view.home_view import HomeView
from templates_view.order_view import OrderView
from templates_view.product_view import ProductView
from templates_view.static_view import StaticView

# Словарь маршрутов
urls = [
    (r'^/$', HomeView),
    (r'^/contact$', ContactUsView),
    (r'^/api/products$', GetProducts),
    (r'^/product/.*$', ProductView),
    (r'^/checkout$', CheckoutView),
    (r'^/src/.*$', StaticView),
    (r'^/api/create_order$', OrderView),
    (r'.*', ErrorView)
]

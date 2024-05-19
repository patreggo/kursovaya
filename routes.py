from json_product.get_products import GetProducts
from templates_view.checkout_view import CheckoutView
from templates_view.contact_us_view import ContactUsView
from templates_view.home_view import HomeView
from templates_view.product_view import ProductView

# Словарь маршрутов
urls = {
    '/': HomeView,
    '/contact': ContactUsView,
    '/api/products': GetProducts,
    '/product/': ProductView,
    '/checkout': CheckoutView,
}
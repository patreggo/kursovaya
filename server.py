from waitress import serve
import cgi
from templates_view.checkout_view import CheckoutView
from templates_view.product_view import ProductView
from templates_view.home_view import HomeView
from templates_view.contact_us_view import ContactUsView
from render_template import render_template
from templates_view.static_view import static_view
from json_product.get_products import GetProducts
from db.connect import create_order

#Словарь маршрутов
urls = {
    '/': HomeView,
    '/contact': ContactUsView,
    '/api/products': GetProducts,
    '/product/': ProductView,
    '/checkout': CheckoutView,
}

def app(environ, start_response):
    path = environ.get("PATH_INFO")

    # Обработка POST-запроса для создания заказа
    if environ['REQUEST_METHOD'] == 'POST':
        if path == '/api/create_order':
            form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
            models = form.getvalue('models', '')
            total_price = form.getvalue('total_price', '')
            count = form.getvalue('count', '')
            name_user = form.getvalue('name_user', '')
            address_user = form.getvalue('address_user', '')
            mail_user = form.getvalue('mail_user', '')
            create_order(models,total_price,count,name_user,address_user,mail_user)
            start_response("200 OK", [("Content-type", "application/json")])
            return [b'{"status": "success"}']

    #Отображение страницы в зависимости от товара
    if path.startswith("/product/"):
        path = "/product/" 
        view_class = urls[path]

    #Обработка статических файлов
    if path.startswith("/src/"):
        return static_view(path, start_response)

    # Обработка запроса на основе представлений
    if path in urls:
        view_class = urls[path]
        view_instance = view_class()
        data, content_type = view_instance.get(environ)
    else:
        data, content_type = render_template(template_name='templates/404.html', context={})

    data = data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-type", content_type),
        ]
    )
    return iter([data])

serve(app)

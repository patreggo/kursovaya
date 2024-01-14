from waitress import serve

from templates_view.checkout_view import CheckoutView
from templates_view.product_view import ProductView
from templates_view.home_view import HomeView
from templates_view.contact_us_view import ContactUsView
from render_template import render_template
from templates_view.static_view import static_view
from json_product.get_products import GetProducts
import json
    
urls = {
    '/': HomeView,
    '/contact': ContactUsView,
    '/api/products': GetProducts,
    '/product/': ProductView,
    '/checkout': CheckoutView,
}

def app(environ, start_response):
    path = environ.get("PATH_INFO")

    if path.startswith("/product/"):
        path = "/product/" 
        view_class = urls[path]
    
        
    if path.startswith("/src/"):
        return static_view(path, start_response)

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

from db.connect import get_products_from_db
from templates_view.base_view import View


class GetProducts(View):
    def get(self, environ):
        data = get_products_from_db()
        content_type = "application/json"
        return data, content_type

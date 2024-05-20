from db.connect import get_products_from_db


class GetProducts():
    def get(self, environ):
        data = get_products_from_db()
        content_type = "application/json"
        return data, content_type

import cgi

from db.connect import create_order
from response import Response
from templates_view.base_view import View


class OrderView(View):
    def post (self, environ):
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        models = form.getvalue('models', '')
        total_price = form.getvalue('total_price', '')
        count = form.getvalue('count', '')
        name_user = form.getvalue('name_user', '')
        adress_user = form.getvalue('adress_user', '')
        mail_user = form.getvalue('mail_user', '')

        create_order(models, total_price, count, name_user, adress_user, mail_user)

        return Response(data=b'{"status": "success"}', content_type="application/json", code=200)
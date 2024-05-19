import cgi

from db.connect import create_order
from render_template import render_template
from routes import urls
from templates_view.static_view import static_view


def handle_request(environ, start_response):
    """
        Функция обрабатывает HTTP-запросы, приходящие на сервер.

        Параметры:
        environ (dict): Словарь, содержащий переменные окружения CGI.
        start_response (callable): Функция, предоставленная сервером WSGI для начала HTTP-ответа.
                                   Эта функция принимает два параметра: строку кода состояния и список
                                   кортежей (header_name, header_value).

        Возвращает:
        list: Список, содержащий ответ сервера на HTTP-запрос. Если запрос был успешно обработан,
              возвращает список, содержащий JSON-строку с сообщением об успехе.
        """
    path = environ.get("PATH_INFO")
    method = environ['REQUEST_METHOD']

    # Обработка POST-запроса для создания заказа
    if method == 'POST' and path == '/api/create_order':
        form = cgi.FieldStorage(fp=environ['wsgi.input'], environ=environ)
        models = form.getvalue('models', '')
        total_price = form.getvalue('total_price', '')
        count = form.getvalue('count', '')
        name_user = form.getvalue('name_user', '')
        adress_user = form.getvalue('adress_user', '')
        mail_user = form.getvalue('mail_user', '')
        create_order(models, total_price, count, name_user, adress_user, mail_user)
        start_response("200 OK", [("Content-type", "application/json")])
        return [b'{"status": "success"}']

    # Обработка статических файлов
    if path.startswith("/src/"):
        return static_view(path, start_response)

    # Отображение страницы в зависимости от товара
    if path.startswith("/product/"):
        path = "/product/"

    # Обработка запроса на основе маршрутов
    if path in urls:
        view_class = urls[path]
        view_instance = view_class()
        data, content_type = view_instance.get(environ)
    else:
        data, content_type = render_template(template_name='templates/404.html', context={})

    data = data.encode("utf-8")
    start_response("200 OK", [("Content-type", content_type)])
    return [data]
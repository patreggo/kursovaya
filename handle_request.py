import re

from render_template import render_template
from routes import urls


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

    view_class = None
    for pattern, view in urls:
        if re.match(pattern, path):
            view_class = view
            break

    if view_class:
        view_instance = view_class()
        if method == 'POST' and hasattr(view_instance, 'post'):
            data, content_type = view_instance.post(environ)
        else:
            data, content_type = view_instance.get(environ)
    else:
        data, content_type = render_template(template_name='templates/404.html', context={})

    data = data.encode("utf-8") if isinstance(data, str) else data
    start_response("200 OK", [("Content-type", content_type)])
    return [data]

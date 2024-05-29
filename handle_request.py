import re

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

    view_class = None
    for pattern, view in urls:
        if re.match(pattern, path):
            view_class = view
            break

    view_instance = view_class()
    response = view_instance.handle(environ)

    start_response(response.code, [("Content-type", response.content_type)])
    return [response.get_data()]

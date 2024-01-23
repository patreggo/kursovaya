import mimetypes


def static_view(path, start_response):
    """
    Эта функция обслуживает статические файлы из файловой системы.

    Параметры:
    path (str): Путь к обслуживаемому файлу. Первый '/' удаляется из пути.
    start_response (callable): Функция, предоставленная сервером WSGI для начала HTTP-ответа. 
                               Эта функция принимает два параметра: строку кода состояния и список 
                               кортежей (header_name, header_value).

    Возвращает:
    list: Список, содержащий содержимое обслуживаемого файла. Если файл не найден, 
          возвращает список, содержащий сообщение об ошибке 404.

    Вызывает:
    FileNotFoundError: Если файл, указанный в пути, не найден.
    """
    new_path = path.replace('/', '', 1)
    try:
        with open(new_path, 'rb') as f:
            content = f.read()
        mime_type, _ = mimetypes.guess_type(new_path)
        if mime_type is None:
            mime_type = 'application/octet-stream'
        start_response("200 OK", [("Content-type", mime_type)])
        return [content]
    except FileNotFoundError:
        start_response("404 Not Found", [("Content-type", "text/plain")])
        return [b"404 Not Found"]

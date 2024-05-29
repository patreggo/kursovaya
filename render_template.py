import mimetypes

#Отображение html страницы
def render_template(template_name, context={}):
    """
    Функция для рендеринга HTML-шаблона.

    Параметры:
    template_name (str): Имя файла шаблона, который нужно отрендерить.
    context (dict, optional): Словарь, содержащий контекст для шаблона. 
                              Ключи словаря будут использоваться как переменные в шаблоне. 
                              По умолчанию пустой словарь.

    Возвращает:
    tuple: Возвращает кортеж из двух элементов. Первый элемент - это отрендеренная HTML-строка. 
           Второй элемент - это тип контента для HTTP-ответа.

    Вызывает:
    FileNotFoundError: Если файл шаблона не найден.
    """
    with open(template_name, 'r', encoding='utf-8') as f:
        html_str = f.read()
        html_str = html_str.format(**context)

    
    return html_str

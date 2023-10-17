from waitress import serve

def render_template(template_name, context={}):
    html_str=""
    with open(template_name, 'r') as f:
        html_str=f.read()
        html_str=html_str.format(**context)
    return html_str

def home(environ):
    return render_template(template_name='templates/index.html', context={})

def contact_us(environ):
    return render_template(template_name='templates/contact.html', context={})

def contact2(environ):
    return render_template(template_name='templates/2.html', context={})

urls={
    '/' : {'view_function' : home, 'content_type' : 'text/plain; charset=utf-8'},
    '/contact' : {'view_function' : contact_us, 'content_type' : 'text/html; charset=utf-8'},
    '/contact/2': contact2,
}

def app(environ, start_response):
    path= environ.get("PATH_INFO")
    if path in urls:
        route=urls[path]
        view_function=route['view_function']
        content_type=route['content_type']
        data = view_function(environ)
    else:
        data = render_template(template_name='templates/404.html', context={"path":path})
        content_type='text/html; charset=UTF-8'
    data=data.encode("utf-8")
    start_response(
        f"200 OK", [
            ("Content-type", content_type),
        ]
    )
    return iter([data])

serve(app)
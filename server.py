from waitress import serve

from handle_request import handle_request


def app(environ, start_response):
    return iter(handle_request(environ, start_response))


serve(app)

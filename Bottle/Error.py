from bottle import run, route, error


@error(404)
def error404(error):
    return '<h1>Your have a 404 error </h1>'


@route('/')
def index():
    return "Hi there"


run(host='localhost', port=8082, debug=True, reloader=True)

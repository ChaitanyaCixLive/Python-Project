from bottle import run, route


@route('/')
def index():
    return '<h1>Hello world</h1>'

run(host='localhost', port=8082)

from bottle import run, route


@route('/')
def index():
    return '<h1>Hello world</h1>'


@route('/login')
def login():
    return '<h1>Log in page</h1>'


@route('/reg')
def login():
    return '<h1>Register page</h1>'


@route('/article/<id>')
def aritcle(id):
    return '<h1> You are viewing article ' + id + '</h1>'

run(host='localhost', port=8082, debug=True, reloader=True)

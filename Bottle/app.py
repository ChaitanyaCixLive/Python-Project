from bottle import run, route, template


@route('/')
def index():
    return template('index')


@route('/login')
def login():
    return '<h1>Log in page</h1>'


@route('/reg')
def login():
    return '<h1>Register page</h1>'


@route('/article/<id>')
def aritcle(id):
    return '<h1> You are viewing article ' + id + '</h1>'


@route('/page/<id>/<name>')
def page(id, name):
    return '<h1>you are viewing page id '+id+'</h1>'+'<br><p>Written by '+name+'</P>';


@route('/posted', method='POST')
def posted():
    return '<h1>Post</h1>'


run(host='localhost', port=8082, debug=True, reloader=True)

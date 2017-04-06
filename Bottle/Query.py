from bottle import run, route, request


@route('/')
def index():
    return "Hi there"


@route('/query')
def index():
    param1 = request.query.param1
    param2 = request.query.param2
    return 'The value of param1 is '+param1+' The value of param2 is '+param2

run(host='localhost', port=8082, debug=True, reloader=True)

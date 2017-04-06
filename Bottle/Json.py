from bottle import run, route


@route('/')
def index():
    return {"name": "jsonData", "myList": [1,2,3,4,5]}


run(host='localhost', port=8082, debug=True, reloader=True)

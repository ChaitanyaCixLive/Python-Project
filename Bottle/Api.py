from bottle import run, route, template


animals = [
    {'name': 'Elite', 'type': 'Elephant'},
    {'name': 'Python', 'type': 'Snake'},
    {'name': 'Zed', 'type': 'Zebra'},
]

@route('/')
def index():
    return 'Hi there'


@route('/animal')
def getAll():
    return {'animal': animals}


@route('/animal/<name>')
def getOne(name):
    the_animal = [animal for animal in animals if animal['name']== name]
    return {'animal': the_animal}



run(host='localhost', port=8082, debug=True, reloader=True)

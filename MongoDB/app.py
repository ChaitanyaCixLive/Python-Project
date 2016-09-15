import pymongo

uri = "mongodb://0.0.0.0:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collecion = database['students']
students = [student['name'] for student in (collecion.find())]

print(students)
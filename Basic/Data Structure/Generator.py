text = [1, 2, 3, 4, 5]


def search():
    for i in text:
        yield i

the_generator = search()

print(next(the_generator))
print(next(the_generator))
print(next(the_generator))
print(next(the_generator))
print()

print(next(search()))
print(next(search()))

print(type(search()))
print(the_generator)
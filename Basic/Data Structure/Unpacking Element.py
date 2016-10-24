records = [
    ('foo', 4, 5),
    ('goo', 'hello'),
    ('foo', 6, 7)
]


def do_foo(x, y):
    print('foo', x, y)


def do_goo(s):
    print('goo', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'goo':
        do_goo(*args)
answer = lambda x: x*5
print(answer(5))


def increment(n):
    return lambda x: x + n


f = increment(20)
print(f)
print(f(5))


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print(type(pairs))
print(type(pairs[0]))
pairs.sort(key=lambda l: l[1])

print(pairs)


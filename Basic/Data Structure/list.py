squares = []

for i in range (10):
    squares.append(i*i)

print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

# efficiently declaring list
setA = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]
print(setA)
print()

vec = [-4, -2, 0, 2, 4]
nv = [x*2 for x in vec]
print(nv)
print([x for x in vec if x>=2])
print([abs(x) for x in vec])
print()


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([name.strip() for name in freshfruit])
print()


matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

print([[row[i] for row in matrix]for i in range(4)])


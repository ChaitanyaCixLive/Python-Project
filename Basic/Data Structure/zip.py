first = ['bikash', 'sneha', 'shuvendu']
last = ['roy', 'paul', 'roy']

name = zip(first, last)
print(type(name))


for x, y in name:
    print(x, y)

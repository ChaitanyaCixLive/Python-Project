items = [1, 2, 5, 3, 4]

print(items)
print(items[0])

items[0] = 8
print(items)

items += [6, 7]
print(items)

items.append(10)
print(items)


word = ['b', 'i', 'k']
newList = [word, items]
print(newList)

newList2 = word + items
print(newList2)
print(newList2[0])
print(newList2[5])

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)

print(a)
print(a.index(333))

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

print(a.pop())

print(a)
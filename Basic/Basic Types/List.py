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
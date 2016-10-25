def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
b = list(dedupe(a))
print(b)
print()


def dedupe(items, key = None):  # Here key is a lambda that takes a dict as parameter and can be called as key(item)
    seen = set()                # Seen stores some temporary item as tuple to lookup only
    print("key", key)
    for item in items:
        val = item if key is None else key(item)
        print(val)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
b = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
b = list(dedupe(a, key=lambda d: (d['x'])))
print(b)


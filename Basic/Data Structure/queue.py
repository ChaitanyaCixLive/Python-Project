from collections import deque

q = deque()
q.append('bikash')
q.append('roy')
q.append('shuvo')

print(q)

q.appendleft('shuvendu')
print(q)

print(q.pop())
print(q)

print(q.popleft())
print(q)

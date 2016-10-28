import numpy as np

a = np.array([20, 30, 40, 50])
b = np.arange(4)

print(b)

c = a - b
print(c)

d = b ** 2
print(d)

e = np.sin(a)
print(e)

print(a < 25)

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[2, 0],
              [3, 4]])

print(A * B)
print()

C = A.dot(B)
print(C)

D = np.dot(A, B)
print(D)
print()

e = A.sum()
print(e)
print(A.min())
print(A.max())
print()

b = np.arange(12).reshape(3, 4)
print(b)

print(b.sum(axis=0))  # axis 0 is the column
print(b.min(axis=1))  # axis 1 is the row

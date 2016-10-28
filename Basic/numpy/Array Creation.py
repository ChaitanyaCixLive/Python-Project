import numpy as np
from numpy import pi

a = np.array([1, 2, 3, 5, 4])
print(a)

print(a.dtype)

b = np.array([1, 2.5, 3.5, 2])
print(b)
print(b.dtype)

c = np.array([[1, 2, 3], [4, 5, 6]])
print(c)

print(c[1][2])

# Complex Array
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print()

# Initialized specific sized array
d = np.zeros((3, 4))
print(d)
print()

e = np.ones((2,3))
print(e)
print()

f = np.empty((3,3))
print(f)
print()

# Size of the data type can also be selected
g = np.empty( (3,4), dtype = np.int16)

f = np.arange(10, 30, 5)
print(f)

g = np.arange(0, 2, 0.3)
print(g)


# number of element in a certain range
h = np.linspace(0, 2, 9)
print(h)
print()

x = np.linspace(0, 2*pi, 100)
print(x)
print()

f = np.sin(x)
print(f)
print()

g = np.random.random((3,3))
print(g)



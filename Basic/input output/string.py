hello = 'hello, \nworld'
hellos = repr(hello)
print(hellos)

helloStr = str(hello)
print(helloStr)
print()

for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end='')
    print(str(x*x*x).rjust(4))      # We also have ljust and center


for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


print('{0} and {1}'.format('bikash', 'roy'))
print('{firstname} and {lastname}'.format(firstname='bikash', lastname='roy'))
print('{0} and {1} who has other name {name}'.format('bikash', 'roy', name='Shuvo'))


# using dictionary
table = {'bikash': 1, 'roy': 2, 'shuvo':3}
print('Bikash : {0[bikash]:d};  Roy : {0[roy]:d};  Shuvo : {0[shuvo]:d}'.format(table))

print('Bikash: {bikash:d}; Roy: {roy:d}; Shuvo: {shuvo:d}'.format(**table))

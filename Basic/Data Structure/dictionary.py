tel = {'jack': 4098, 'sape': 4139}
print(tel)

tel['bikahs'] = 2050;
print(tel)
print()


for u,v in tel.items():
    print(u, v)
print()


newDic = {x: x**2 for x in (2, 4, 6)}
print(newDic)
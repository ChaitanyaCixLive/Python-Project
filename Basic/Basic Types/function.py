# this function has some important behaviour
# L is initialized once and appending in every cal


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# function with default arguments
def multiplaArg(name='bikash', roll=1407001, dept='CSE'):
    print(name, roll, dept)

multiplaArg()
multiplaArg(name='roy') # look at the calling, it is the most important part
multiplaArg(roll=1)


print()
# *** very very important ***
# *inside a function parameter means it receive as many parameter will be passes
# **inside a funciton parameter means it receive dictionary


def bossFunction(name, *arguments, **keys):
    print(name)
    print('-'*40)

    print(type(arguments))
    for i in arguments:
        print(i, type(i))
    print('-'*40)

    print(type(keys))
    for i in keys:
        print(i, '->', keys[i])


bossFunction("Limburger", "It's very runny, sir.",
             "It's really very, VERY runny, sir.",
             5, 40,
             shopkeeper="Michael Palin",
             client="John Cleese",
             sketch="Cheese Shop Sketch")
print()


def fun(*arg, sep='/'):
    print(sep.join(arg))

fun('10', '24', '2016')

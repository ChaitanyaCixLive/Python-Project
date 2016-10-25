class Complex:
    def f(self):
        return "This is a mathod object"


x = Complex()
xf = x.f
print(xf())
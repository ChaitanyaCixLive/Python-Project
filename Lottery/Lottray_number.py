import random
from tkinter import *


def lotto_no():
    x = random.randint(1,49)
    q = random.randint(1,49)
    w = random.randint(1,49)
    e = random.randint(1,49)
    r = random.randint(1,49)
    t = random.randint(1,49)

    num1.set(x)
    num2.set(q)
    num3.set(w)
    num4.set(e)
    num5.set(r)
    num6.set(t)
    return


Lottary = Tk()
Lottary.geometry('800x360')
frame = Frame(Lottary)
frame.pack()

Lottary.title('Lottray Numbers Generators')

num1 = StringVar()
num2 = StringVar()
num3 = StringVar()
num4 = StringVar()
num5 = StringVar()
num6 = StringVar()

var = StringVar()
var.set("Lotto Nnumber generator")
frame1 = Frame(Lottary)
frame1.pack()
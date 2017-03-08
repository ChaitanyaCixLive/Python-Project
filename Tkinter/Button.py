from tkinter import *
from tkinter import ttk


def callback():
    print('Clicked!')


root = Tk()

button = ttk.Button(root, text="Click me")
button.pack()
button.config(command=callback)

# button click simulation
button.invoke()

button.state(['disabled'])
print(button.instate(['disabled']))
button.state(['!disabled'])

logo = PhotoImage(file="img/python_logo.gif")
button.config(image=logo, compound=LEFT)
small_logo = logo.subsample(5,5)
button.config(image=small_logo, compound=LEFT)

root.mainloop()



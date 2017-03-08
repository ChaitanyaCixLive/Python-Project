from tkinter import *
from tkinter import ttk


def callback():
    print('Clicked!')


root = Tk()

button = ttk.Button(root, text="Click me")
button.pack()
button.config(command=callback)

root.mainloop()



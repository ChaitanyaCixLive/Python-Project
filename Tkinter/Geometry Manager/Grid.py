from tkinter import *
from tkinter import ttk


root = Tk()

ttk.Label(root, text="Yellow", background='yellow').grid(row=0, column=0, stick='nsew')
ttk.Label(root, text="blue", background='blue').grid(row=0, column=1, stick='nsew')
ttk.Label(root, text="Orange", background='orange').grid(row=1, column=0, stick='nsew')
ttk.Label(root, text="Green", background='green').grid(row=1, column=1, stick='nsew')

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)

root.mainloop()
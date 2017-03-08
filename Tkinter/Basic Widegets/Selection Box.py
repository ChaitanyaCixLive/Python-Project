from tkinter import *
from tkinter import ttk


root = Tk()
month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()
combobox.config(values=['jan', 'feb'])

root.mainloop()
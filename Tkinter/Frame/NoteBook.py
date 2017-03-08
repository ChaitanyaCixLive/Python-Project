from tkinter import *
from tkinter import ttk


root = Tk()
notebook = ttk.Notebook(root)
notebook.pack()

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='One')
notebook.add(frame2, text='Two')

ttk.Button(frame1, text='Click Me').pack()

notebook.tab(1, state='disabled')


root.mainloop()
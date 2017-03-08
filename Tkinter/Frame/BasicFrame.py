from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
frame.pack()
frame.config(height=100, width=200)

# Setting the border
frame.config(relief=RIDGE)

ttk.Button(frame, text='Click Me').pack()


root.mainloop()
from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Hello Tkinter")
label.pack()
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 18, 'bold'))

logo = PhotoImage(file="img/python_logo.gif")
label.config(image = logo)

root.mainloop()

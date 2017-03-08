from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root, text="Hello Tkinter")
label.pack()
label.config(foreground='blue', background='yellow')
label.config(font=('Courier', 18, 'bold'))

logo = PhotoImage(file="img/python_logo.gif")
label.config(image=logo)

label.config(compound='text')
label.config(compound='center')
label.config(compound='left')

# the previous image has scope issue
# so keep a reference of it to save it from garbage collected when goes out of scope
label.img = logo
label.config(image=label.img)

root.mainloop()

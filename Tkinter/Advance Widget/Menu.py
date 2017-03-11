from tkinter import *


root = Tk()

# TearOff is a default behavious which does not go with modern GUI
root.option_add('*tearOff', False)

# Creating a menu bar
menubar = Menu(root)
root.config(menu=menubar)

file = Menu(menubar)
edit = Menu(menubar)
help_ = Menu(menubar)
menubar.add_cascade(menu=file, label="File")
menubar.add_cascade(menu=edit, label="Edit")
menubar.add_cascade(menu=help_, label="Help")

file.add_command(label='New', command=lambda : print('New file'))
file.entryconfig('New', accelerator='Ctrl + N')
file.add_separator()

file.add_command(label='Open..', command=lambda : print('Open file'))
file.add_command(label='Save', command=lambda : print('Save file'))

logo = PhotoImage(file='img/python_logo.gif').subsample(10,10)
file.entryconfig('Open..', image=logo, compound='left')


root.mainloop()
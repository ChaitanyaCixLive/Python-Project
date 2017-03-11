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

file.add_command(label='New', command=lambda: print('New file'))
file.entryconfig('New', accelerator='Ctrl + N')
file.add_separator()

file.add_command(label='Open..', command=lambda: print('Open file'))

open_recent = Menu(file)
file.add_cascade(menu=open_recent, label="Open Recent")
open_recent.add_command(label="file_1")

file.add_command(label='Save', command=lambda: print('Save file'))

logo = PhotoImage(file='img/python_logo.gif').subsample(10, 10)
file.entryconfig('Open..', image=logo, compound='left')

choice = IntVar()
edit.add_radiobutton(label='One', variable=choice, value=1)
edit.add_radiobutton(label='Two', variable=choice, value=2)
edit.add_radiobutton(label='Three', variable=choice, value=3)

file.post(300, 400)


root.mainloop()
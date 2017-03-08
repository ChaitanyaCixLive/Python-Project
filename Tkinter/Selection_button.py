from tkinter import *
from tkinter import ttk

root = Tk()

check_botton = ttk.Checkbutton(root, text='Spam?')
check_botton.pack()

root.mainloop()
from tkinter import *
from tkinter import ttk

root = Tk()

check_botton = ttk.Checkbutton(root, text='Spam?')
check_botton.pack()

spam = StringVar()

check_botton.config(variable=spam, onvalue='spam', offvalue='not a spam')
print(spam.get())

breakfast=StringVar()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value="SPAM").pack()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value="Eggs").pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value="Sausage").pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value="Sausage").pack()

root.mainloop()
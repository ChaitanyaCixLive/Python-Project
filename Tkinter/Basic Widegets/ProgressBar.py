from tkinter import *
from tkinter import ttk


root = Tk()
progressBar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressBar.pack()
progressBar.config(mode='indeterminate')
progressBar.start()
progressBar.stop()

progressBar.config(mode='determinate', maximum=11.0, value=4.2)

# this value can be taken from a variable
value = DoubleVar()
progressBar.config(variable=value)

scale = ttk.Scale(root, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=11.0)
scale.pack()

root.mainloop()
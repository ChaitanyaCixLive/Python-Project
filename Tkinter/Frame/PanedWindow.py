from tkinter import *
from tkinter import ttk

root = Tk()
panedwindow = ttk.PanedWindow(root, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)

frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)

# add will by default add it to the right
panedwindow.add(frame1, weight=1)
panedwindow.add(frame2, weight=4)

# to addd it in any specific place use insert
panedwindow.insert(1, frame3)
# here first parameter is the column number
# one more thing to notice, here the weight is not specified. so it will take the default weight of 0
# which means it is a fixed pixel width and no relation with other


# to delete a frame use forget
panedwindow.forget(1)
# it will exist in back ground though


root.mainloop()
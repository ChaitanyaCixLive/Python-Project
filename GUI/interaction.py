from tkinter import *

root = Tk()

def printName():
    print("I am Bikash")

button_1 = Button(root, text="Print Name", command=printName)
button_1.pack()

root.mainloop()
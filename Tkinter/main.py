from tkinter import *


root = Tk()

""" Simple layout """
# theLabel = Label(root, text="this is the label")
# theLabel.pack()


"""use of frame"""
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# buttom1 = Button(topFrame,text="Button 1", fg="red")
# buttom2 = Button(topFrame,text="Button 2", fg="blue")
# buttom3 = Button(topFrame,text="Button 3", fg="green")
# buttom4 = Button(bottomFrame,text="Button 4", fg="purple")
#
# buttom1.pack(side=LEFT)
# buttom2.pack(side=LEFT)
# buttom3.pack(side=LEFT)
# buttom4.pack(side=BOTTOM)


""" Fitting widgets """
one = Label(root, text="One", bg="red", fg="white")
one.pack()
two = Label(root, text="One", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="One", bg="blue", fg="white")
three.pack(fill=Y, side=LEFT)

root.mainloop()
from tkinter import *


#main window
root = Tk()

#Frame is an in visiable container
topFrame = Frame(root)
topFrame.pack()
#pack means give this a place where possible

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Button1", fg="green")
button2 = Button(topFrame, text="Button2", fg="red")
button3 = Button(topFrame, text="Button3", fg="blue")
button4 = Button(bottomFrame, text="Button4", fg="purple")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)


#contimus stay
root.mainloop()


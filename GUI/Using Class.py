from tkinter import *



class newButton:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = "Print message", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.QuiteButton = Button(frame, text = "Quit", command=frame.quit)
        self.QuiteButton.pack(side=LEFT)

    
    def printMessage(self):
        print("worked!!")

root = Tk()

b = newButton(root)


root.mainloop()
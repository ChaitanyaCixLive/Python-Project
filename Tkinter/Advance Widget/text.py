from tkinter import *

root = Tk()
text = Text(root, width=40, height=10)
text.pack()

# Stop breaking word
text.config(wrap='word')

# getting the first lines of text
text.get('1.0', '1.end')

# inserting text in specific line
text.insert('1.0 + 2 lines', 'Inserted text')


root.mainloop()
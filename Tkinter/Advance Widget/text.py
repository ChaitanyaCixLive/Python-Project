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

# adding tag
text.tag_add('my_tag', '1.0', '1.0 wordend')
text.tag_configure('my_tag', background='yellow')

# removing tag from some area
text.tag_remove('my_tag', '1.1', '1.3')

# deleting a tag
text.tag_delete('my_tag')


root.mainloop()
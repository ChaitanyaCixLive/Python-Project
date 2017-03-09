from tkinter import *
from tkinter import ttk

root = Tk()

treeview = ttk.Treeview(root)
treeview.pack()
treeview.insert('', '0', 'item1', text='First Item')
treeview.insert('', '1', 'item2', text='Second Item')
treeview.insert('', 'end', 'item3', text='Third Item')

logo = PhotoImage(file='img/python_logo.gif').subsample(10, 10)
treeview.insert('item2', 'end', 'python', text='python', image=logo)

# move
treeview.move('item2', 'item1', 'end')

# Adding column
treeview.config(columns='version')
treeview.column('version', width=50, anchor='center')
treeview.column('#0', width=150)
treeview.heading('version', text='Version')

treeview.set('python', 'version', '3.5.1')
treeview.item('python', tags='software')
treeview.tag_configure('software', background='yellow')


def callback(event):
    print(treeview.selection())

treeview.bind('<<TreeViewSelect>>', callable)


root.mainloop()

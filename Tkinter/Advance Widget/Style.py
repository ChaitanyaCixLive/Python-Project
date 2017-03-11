from tkinter import *
from tkinter import ttk

root = Tk()
button1 = ttk.Button(root, text='Button1')
button2 = ttk.Button(root, text='Button2')
button1.pack()
button2.pack()

style = ttk.Style()
print(style.theme_names())
print(style.theme_use())

print(button1.winfo_class()) # TButton

style.configure('Alarm.TButton', foreground='orange', font=('Arial', 24, 'bold'))
button2.config(style='Alarm.TButton')

style.map('Alarm.TButton', foreground=[('pressed', 'pink'), ('disabled', 'yellow')])

root.mainloop()
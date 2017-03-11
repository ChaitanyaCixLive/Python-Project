from tkinter import *

root = Tk()

canvas = Canvas(root)
canvas.pack()
canvas.config(width=640, height=480)

line = canvas.create_line(160,360, 480, 120, fill='blue')
canvas.itemconfig(line, fill = 'green', width=5)

canvas.coords(line, 0, 0, 320, 240, 640, 0)

# making the line full smooth
canvas.itemconfig(line, smooth=True)

# making it 5 break smooth
canvas.itemconfig(line, splinesteps=5)

root.mainloop()
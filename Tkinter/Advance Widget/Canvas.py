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

rect = canvas.create_rectangle(160, 120, 480, 360)
canvas.itemconfig(rect, fill='yellow')

oval = canvas.create_oval(160, 120, 480, 360)
arc = canvas.create_arc(160, 1, 480, 240)
canvas.itemconfig(arc, start=0, extent=180, fill='green')

poly = canvas.create_polygon(160,360,320,480,480,360, fill='blue')
text = canvas.create_text(320, 240, text='Python', font=('Courier', 32, 'bold'))

logo = PhotoImage(file='img/python_logo.gif')
image = canvas.create_image(320, 240, image=logo)
canvas.lift(text)

root.mainloop()
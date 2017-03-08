from tkinter import *

root = Tk()
window = Toplevel(root)
window.title('New Window')

# Moving window up and down
window.lower()
window.lift(root)

# Making a window full screen
window.state('zoomed')

# making windows invisible and working in background
window.state('withdrawn')

# keeping window minimized
window.state('iconic')
# or window.iconify()

window.geometry('640x480+50+100')

# Stop resize
window.resizable(False, False) # x ans y direstion

window.maxsize(640, 480)
window.minsize(200, 200)
window.resizable(True, True)

root.destroy()

root.mainloop()


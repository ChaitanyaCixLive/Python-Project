from PIL import Image


img = Image.open('robot.jpg')
r, g, b = img.split()

r.show()
g.show()
b.show()
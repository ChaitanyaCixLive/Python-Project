from PIL import Image

img = Image.open('robot.jpg')
r, g, b = img.split()

new_img = Image.merge("RGB", (b,r,g))
new_img.show()
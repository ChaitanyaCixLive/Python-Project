from PIL import Image


img = Image.open('robot.jpg')
img1 = Image.open('python_logo.gif')

area = (100, 100, 300, 300)

img.paste(img1, area)
img.show()

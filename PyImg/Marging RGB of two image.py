from PIL import Image

img = Image.open('time.jpg')
r1, g1, b1 = img.split()
print(img.size)

img = Image.open('robot.jpg')
size = (200, 200, 950, 950)
img1 = img.crop(size)
print(img1.size)
r, g, b = img1.split()


new_img = Image.merge("RGB", (b1, r, g1))
new_img.show()
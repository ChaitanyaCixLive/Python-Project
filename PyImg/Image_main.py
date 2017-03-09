from PIL import Image

img = Image.open('python_logo.gif')

# Printing size and showing it in viewer
# print(img.size)
# img.show()

# Cropping an image

area = (100, 100, 200, 200)     # First two are upper co-ordinate other two are lower coordinate
cropped_image = img.crop(area)

cropped_image.show()
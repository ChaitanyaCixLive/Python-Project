from PIL import Image

img = Image.open('robot.jpg')

square = img.resize((350, 250))
# square.show()

flip = img.transpose(Image.FLIP_LEFT_RIGHT)
flip.show()

flip.save('new_image.jpg')
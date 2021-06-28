from PIL import Image, ImageDraw
import numpy

image = Image.open("TEST IMAGES/withBears/2016-05-18 12-39-15_2042_r_3C.JPG")
pix = image.load()
width = image.size[0]
height = image.size[1]
draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования

# for x in range(width):
#     for y in range(height):
#         pix[x, y] =
#         print(f"\rX: {x / width * 100}%", end="")

for x in range(width):
    for y in range(height):
       image.putpixel((x, y), (0, 0, image.getpixel((x, y))[2]))
       print(f"\rX: {x / width * 100}%", end="")

image.save('test2.JPG')

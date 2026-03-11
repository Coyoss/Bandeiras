from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"



'''def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

image = Image.open(in_path("atena.png"))
print(image.getpixel((30, 30)))
image.show()'''






'''def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

novaimage = Image.new("RGB", (1000, 1000),  (25, 25, 75))
novaimage.show()
novaimage = Image.new("RGB", (1000, 1000), (255, 255, 0))
novaimage.show()
'''
def triangle(size):
    BIA = (41, 23, 10)
    RYAN = (5, 141, 252)
    image = Image.new("RGB", (size, size), RYAN)
    for x in range(size):
        for y in range(size):
            if x > y:
                image.putpixel((x, y), BIA)
    return image
if __name__ == "__main__":
    t=triangle(700)
    t.show()

from PIL import Image
import os

INPUT_FOLDER = "input"
OUTPUT_FOLDER = "output"

def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)



def bandeira_franca(height):
    width = 3*height//2
     #  ratio = 3/2
     # width = int(height * ratio)
    BLUE = (0, 85, 164)
    WHITE = (255, 255, 255)
    RED = (239, 65, 53)
    image = Image.new("RGB", (width, height), WHITE)
     
    offset = width//3
    for x in range(offset):
          for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2*offset, y), RED)
    return image


def bandeira_romenia(height):
    width = 3*height//2
     #  ratio = 3/2
     # width = int(height * ratio)
    BLUE = (0,43,127)
    WHITE = (252,209,22)
    RED = (206,17,38)
    image = Image.new("RGB", (width, height), WHITE)
     
    offset = width//3
    for x in range(offset):
          for y in range(height):
            image.putpixel((x, y), BLUE)
            image.putpixel((x + 2*offset, y), RED)
    return image
   
def bandeira_japao_circulo(height):
    width = 3*height//2
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)

    raio = 3*height//10
    centro = (width//2, height//2)
    image = Image.new("RGB", (width, height), WHITE)
    for x in range(centro[0] - raio, centro[0] + raio):
        for y in range(centro[1] - raio, centro[1] + raio):
            if (x - centro[0]) ** 2 + (y - centro[1]) ** 2 <= raio ** 2:
                image.putpixel((x, y), RED)
   
    return image



def bandeira_japao_losango(height):
    width = 3 * height // 2
    WHITE = (255, 255, 255)
    RED = (173, 35, 51)

    raio = 3 * height // 10
    centro = (width // 2, height // 2)
    image = Image.new("RGB", (width, height), WHITE)
    
    for x in range(centro[0] - raio, centro[0] + raio):
        for y in range(centro[1] - raio, centro[1] + raio):
            # Equação da distância de Manhattan para formar um losango:
            # |x - x0| + |y - y0| <= raio
            if abs(x - centro[0]) + abs(y - centro[1]) <= raio:
                image.putpixel((x, y), RED)
    
    return image
   

if __name__ == "__main__":
    #bandeira = bandeira_franca(700)
    #bandeira = bandeira_romenia(700)
    bandeira= bandeira_japao_losango(700)
    bandeira.show()
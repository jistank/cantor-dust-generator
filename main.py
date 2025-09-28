import images
import os

def create_image(length = 600, height = 600, color = (0,0,0)):
    ''' Creating an image and setting the coordinates '''
    assert length == height, "length and Height must be equal"
    return [[color for w in range(length)] for h in range(height)]


def color_pixel(img, x, y, color):
    ''' Coloring a specific pixel by inserting coordinates '''
    height, length = len(img), len(img[0])
    assert 0 <= x < length and 0 <= y < height
    img[y][x] = color


def color_full_rectangle(img, x1, y1, x2, y2, color):
    ''' Coloring a rectangle by setting the coordinates '''
    [[color_pixel(img, x, y, color) for y in range(y1, y2 + 1)] for x in range(x1, x2 + 1)]


def division(img, x1 = 0, y1 = 0, x2 = 599, y2 = 599, current_layer = 1, layer = 0):
    ''' Recursively divide the image, subtracting one third of each square's length to form a cross '''
    if current_layer == layer:
        return img 
    else:
        if current_layer == 1: # if we don't want to split the entire black image even once
            color_full_rectangle(img, x1, y1, x2, y2, (0,0,0))
        
        length = x2 - x1 +1 # +1 to return to the initial image size
        third = length // 3

        color_full_rectangle(img, x1 + third, y1, x1 + 2*third - 1, y2, (255,255,255))
        color_full_rectangle(img, x1, y1 + third, x2, y1 + 2*third - 1, (255,255,255))
        
        # square top left
        division(img, x1, y1, x1 + third - 1, y1 + third - 1, current_layer + 1, layer)
        # square top right
        division(img, x2 - third + 1, y1, x2, y1 + third - 1, current_layer + 1, layer)
        # square at the bottom left
        division(img, x1, y2 - third + 1, x1 + third - 1, y2, current_layer + 1, layer)
        # square at the bottom right
        division(img, x2 - third + 1, y2 - third + 1, x2, y2, current_layer + 1, layer)
    return img


def rotate_left(lista):
    ''' Rotate the img to the left'''
    return [[riga[i] for riga in lista] for i in range(len(lista[0]))][::-1]


def clean(img, n_layer):
    ''' due to the division between itegers there may be 1px line left connecting the generated squares, this function draws white lines based on the number of possible lines they could generate'''
    for i in (range(len(img))):
        if img[i].count((0,0,0)) <= 2**n_layer/2: # if the number of pixels is less than or equal to the number of squares in the first sequence
            img[i] = [(255,255,255) for px in range(len(img[i]))]
    return img


def set_img(division_n):
    ''' Generates a sequence of images based on the specified number of layers '''
    os.makedirs("images")
    for n_layer in range(1, division_n + 1):
        img = create_image()
        img = division(img, layer = n_layer)  
        clean(img, n_layer)
        img = rotate_left(img)
        clean(img, n_layer)
        name_img = "images/layer" + str(n_layer) + ".png"
        images.save_image(img, name_img)


if __name__ == "__main__":
    set_img(6)

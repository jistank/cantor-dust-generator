import png
import io

class Image:
    ''' Matrix displayed '''
    def __init__(self, img):
        self.pixels = img

    def _repr_png_(self):
        ''' PNG binary representation '''
        img = png.from_array(self.pixels, 'RGB')
        b = io.BytesIO()
        img.save(b)

def save_image(img, filename="output.png"):
    ''' Save the image '''
    flat_img = []
    for row in img:
        flat_row = []
        for pixel in row:
            flat_row.extend(pixel)
        flat_img.append(flat_row)
    png.from_array(flat_img, 'RGB').save(filename)

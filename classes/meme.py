"Meme image class"
from PIL import Image


class Meme:
    def __init__(self, pasted_image_coordinates: tuple,
                 pasted_image_size: tuple, text_coordinates: tuple, image: str):

        self.pasted_image_coordinates = pasted_image_coordinates
        self.pasted_image_size = pasted_image_size
        self.text_coordinates = text_coordinates
        try:
            self.image = Image.open(image)
        except AttributeError:
            print("a")

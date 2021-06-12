"""Meme Command"""
from .command import Command
from PIL import Image, ImageDraw, ImageFont
import random

class MemeCommand(Command):
    """Command class"""
    def __init__(self, message: str, name: str, assets: list, uses_args: bool,
                 description: str, pasted_image_coordinates: tuple,
                 pasted_image_size: tuple, text_coordinates: tuple, meme_text: str):

        super().__init__(message, name, assets, uses_args, description)
        self.pasted_image_coordinates = pasted_image_coordinates
        self.pasted_image_size = pasted_image_size
        self.text_coordinates = text_coordinates

        self.meme_text = meme_text

    def paste_image(self):
        """Pastes an image over other"""
        font =ImageFont.truetype("../fonts/DroidSans.ttf")
        images = self.assets

        print(images)
        canvas = random.choice(images[0])
        image = images[1].resize(self.pasted_image_size)

        canvas.paste(image, self.pasted_image_coordinates)

        draw = ImageDraw.Draw(canvas)
        draw.text(self.text_coordinates, self.meme_text, "black", font)
        return canvas

"""Meme Command"""
from .command import Command
from .meme import Meme
import random
from PIL import Image, ImageDraw, ImageFont

class MemeCommand(Command):
    """Command class"""
    def __init__(self, message: str, name: str, assets: list, uses_args: bool,
                 description: str):
        super().__init__(message, name, assets, uses_args, description)


    def paste_image(self, profilepic, text: str):
        """Pastes an image over other"""
        font =ImageFont.truetype("./fonts/DroidSans.ttf", 96)
        memes = self.assets

        meme = random.choice(memes)
        canvas = meme.image
        image = profilepic.resize(meme.pasted_image_size)

        canvas.paste(image, meme.pasted_image_coordinates)

        draw = ImageDraw.Draw(canvas)
        draw.text(meme.text_coordinates, text, "black", font)
        return canvas
    def put_text(self, user1='', user2=''):
        """Just puts text over an image"""
        font =ImageFont.truetype("./fonts/DroidSans.ttf")
        memes = self.assets
        meme = random.choice(memes)
        canvas = meme.image
        img_fraction = 0.85
        fontsize= 1
        space = ' '
        txt = f"the virgin {user2} {space*50} the chad {user1}"
        while font.getsize(txt)[0] < img_fraction*canvas.size[0]:
            # iterate until the text size is just larger than the criteria
            fontsize += 1
            font = ImageFont.truetype("./fonts/DroidSans.ttf", fontsize)
        white = Image.open("./assets/white.png")
        white = white.resize((int(canvas.size[0]), fontsize +10))
        white.show()
        draw = ImageDraw.Draw(canvas)
        canvas.paste(white, meme.text_coordinates)
        draw.text(meme.text_coordinates, txt, "black", font=font)
        return canvas

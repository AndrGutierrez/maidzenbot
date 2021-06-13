"""Bot model"""

import random
from io import BytesIO
import discord
from discord.ext.commands import MemberConverter
from discord.ext.commands.errors import MemberNotFound
from discord.ext import commands as discord_commands
from discord import Embed

import requests

from .command import Command
from .meme import Meme
from .api_command import ApiCommand
from .meme_command import MemeCommand

from PIL import Image

class Bot(discord_commands.Bot):
    """Bot class"""
    def __init__(self, command_prefix, token):
        self.__token = token
        super().__init__(command_prefix)

    def start_connection(self):
        """starts the connection"""
        @self.event
        async def on_ready():
            print(f"{self.user} has connected to discord")

        try:
            self.run(self.__token)
        except ConnectionError:
            print(" Hubo un error al conectar.")

    def listen_normal_commands(self, command: Command):
        """registers the commands in the bot"""
        @self.command(name=command.name)
        async def send_reply(ctx, *args):
            """Sends the reply when command is executed"""
            response = command.message
            users = []
            if command.uses_args:
                for arg in args:
                    try:
                        user = await MemberConverter().convert(ctx, arg)
                        users.append(user.name)
                    except MemberNotFound:
                        pass
                if users == []:
                    command.message = ' '

            response = f'**_{ctx.author.name}_**{command.message} **_{users} _**'.replace(
                "'", '').replace("]", '').replace("[", '')

            if command.assets != []:
                request = requests.get(random.choice(command.assets))
                image_url = request.url
                embed = Embed(title=response, color=3447003)
                embed.set_image(url=image_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f">>> {response}")

    def listen_api_commands(self, command: ApiCommand):
        """Replies to commands that need to consume an api"""
        @self.command(name=command.name)
        async def send_reply(ctx, arg):
            options = range(50)[4:]
            options3 = range(300)[51:]
            switcher = {
                'masterpiece': random.choice([1, 2]),
                'god': 2,
                'nice': 3,
                'meh': random.choice(options),
                'zzz': random.choice(options3)
            }
            arg = str(switcher.get(arg))
            response = command.get_api(arg)
            list_range = range(50)
            response = response['top'][random.choice(list_range)]
            await ctx.send(response['url'])

    def listen_meme_commands(self, command: MemeCommand):
        """Creates meme"""
        @self.command(name=command.name)
        async def send_reply(ctx, *args):
            response = command.message
            try:
                arg = args[0]
            except IndexError:
                embed = Embed(title="Tienes que mencionar a un usuario :ShioEmbarrass:", color=3447003)
                await ctx.send(embed=embed)
            try:
                user = await MemberConverter().convert(ctx, arg)
                avatar_bytes = await user.avatar_url.read()
                profilepic = Image.open(BytesIO(avatar_bytes))

                if command.assets[0].pasted_image_size[0] <=1:
                    image = command.put_text(ctx.author.name, user.name)
                else:
                    image = command.paste_image(profilepic, user.name)
                with BytesIO() as image_binary:
                    image.save(image_binary, 'PNG')
                    image_binary.seek(0)

                    await ctx.send(f">>> **_{ctx.author.name}_** {command.message} **_{user.name}_**", file=discord.File(fp=image_binary, filename='image.png'))
            except MemberNotFound:
                pass

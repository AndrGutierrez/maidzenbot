"""Bot model"""

from discord.ext.commands import MemberConverter
from discord.ext.commands.errors import MemberNotFound
from discord.ext import commands as discord_commands
from discord import Embed

import requests

from .command import Command


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

            response = f'**_{users}_** {command.message} **_{ctx.author.name}_**'.replace(
                "'", '').replace("]", '').replace("[", '')

            if command.assets != '':
                request = requests.get(command.assets)
                image_url = request.url
                embed = Embed(title=response, color=3447003)
                embed.set_image(url=image_url)
                await ctx.send(embed=embed)

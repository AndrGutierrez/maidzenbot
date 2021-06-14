"""Run bot"""
import os
from dotenv import load_dotenv
# from discord.ext.commands import Bot
from classes.bot import Bot
from classes.command import Command
from classes.api_command import ApiCommand
from classes.meme_command import MemeCommand
from commands import commands as command_list
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = Bot(command_prefix='%', token=TOKEN)
for command in command_list:
    if type(command) == Command:
        bot.listen_normal_commands(command)
    elif type(command) == ApiCommand:
        bot.listen_api_commands(command)
    elif type(command) == MemeCommand:
        bot.listen_meme_commands(command)

keep_alive()
bot.start_connection()

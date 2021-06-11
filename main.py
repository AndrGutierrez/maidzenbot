"""Run bot"""
import os
from dotenv import load_dotenv
# from discord.ext.commands import Bot
from classes.bot import Bot
from classes.command import Command
from classes.api_command import ApiCommand
from commands import commands as command_list

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = Bot(command_prefix='%', token=TOKEN)
for command in command_list:
    if type(command) == Command:
        print(command.name)
        bot.listen_normal_commands(command)
    elif type(command) == ApiCommand:
        bot.listen_api_commands(command)
bot.start_connection()

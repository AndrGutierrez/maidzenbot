"""Run bot"""
import os
from dotenv import load_dotenv
# from discord.ext.commands import Bot
from classes.bot import Bot
from classes.command import Command
from commands import commands as command_list

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = Bot(command_prefix='%', token=TOKEN)
for command in command_list:
    if isinstance(command, Command):
        bot.listen_normal_commands(command)
bot.start_connection()

"""Run bot"""
import os
from dotenv import load_dotenv
from discord.ext.commands import Bot
from classes.Connection import Connection

load_dotenv()
TOKEN = os.environ.get("TOKEN")
bot = Bot(command_prefix='$')
connection = Connection(bot, TOKEN)
connection.start()

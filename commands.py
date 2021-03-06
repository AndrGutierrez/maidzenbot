"""Customized commands are created here"""
from classes.command import Command
from classes.api_command import ApiCommand
from classes.meme_command import MemeCommand
from memes import memes
from PIL import Image

commands = []

hug = Command("abraza a", "hug",
              ["https://imgur.com/Ty1Q5XN"], True,
              'Abraza a un ser querido :3')

wednesday = Command("Hoy es miércoles :sunglasses:", "miercoles",
                    ["https://imgur.com/Ty1Q5XN"], False,
                    "Celebra los miércoles :sunglasses:")

wakeup = Command("despierta al dormilón de", "wakeup",
                 ["https://imgur.com/96UoWK2"], True,
                 "Despierta a los flojos jeje")

attack = Command("ataca a", "attack", [
    "https://imgur.com/bGBwXkF", "https://imgur.com/g1z2Bn9",
    "https://imgur.com/F5h2SFQ"
], True, "Ataca a alguien")

pat = Command("le da cariño a", "pat",
              ["https://imgur.com/xeEWmyq", "https://imgur.com/RrRYsZW"], True,
              "Das cariño a un amigo :D")

smile = Command("sonrie jeje :)", "smile", ["https://imgur.com/WgChzZ7"],
                False, "sonries mucho jaja :D")

dance = Command("se pone a bailar :sunglasses:", "dance",
                ["https://imgur.com/ETUfuGo"], False, "baile feliz yeee")

mimir = Command("se fue a mimir~", "mimir", ["https://imgur.com/rqrRNjN"],
                False, "a mimir~")
spawn = Command("* Entra épicamente al chat *", "spawn", ["https://media.discordapp.net/attachments/790362546049515551/998766590281650227/bondrewd-madeinabyss.gif"], False, "Entra con estilo")

recommend = ApiCommand("Esto es una recomendación", "recommend", [], True,
                       "Te recomienda una obra maestra",
                       "https://api.jikan.moe/v3/top/anime/")

simping = MemeCommand("tiene pensamientos impuros sobre", "simp",
                      memes["simp"], True, "simpea a alguien")

chadvsvirgin = MemeCommand("el chad vs el virgen", "virgin", memes["chadvsvirgin"], True, "god vs zzz")
commands.extend(
    [hug, wednesday, wakeup, attack, pat, smile, dance, mimir, simping, chadvsvirgin, recommend, spawn])

HELP_TEXT = "Lista de comandos: \n\n" + \
            ''.join([f"  -{command.name} \n" for command in commands]) + \
            '\nEspero que esto te haya sido de ayuda'

command_help = Command(HELP_TEXT, "ayuda", [], False,
                       "Muestra la lista de comandos")


commands.append(command_help)
# commands.extend([hug])

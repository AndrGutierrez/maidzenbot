"""Customized commands are created here"""
from classes.command import Command
from classes.api_command import ApiCommand
from classes.meme_command import MemeCommand
from memes import memes
from PIL import Image

commands = []

hug = Command("abraza a", "hug", ["https://i.imgur.com/Ty1Q5XN.gif", "https://i.pinimg.com/originals/7e/0d/ab/7e0dab2e79d4d508110aa56ff9970f3c.gif  "], True,
              'Abraza a un ser querido :3 (ping)')

wednesday = Command("Hoy es miércoles :sunglasses:", "miercoles",
                    ["https://media.tenor.com/images/ad8b2f9769a4d2354b50299c55a2f5d3/tenor.gif"], False,
                    "Celebra los miércoles :sunglasses:")

wakeup = Command("despierta al dormilón de", "wakeup",
                 ["https://i.imgur.com/96UoWK2.gif", "http://pa1.narvii.com/6592/c6db621e46b6ed9ca2b463263b4d697b28990475_00.gif"], True,
                 "Despierta a los flojos jeje (ping)")

attack = Command("ataca a", "attack", [
    "https://i.imgur.com/bGBwXkF.gif", "http://akimonogatari.es/wp-content/uploads/2017/11/re1.gif",
    "https://imgur.com/F5h2SFQ"
], True, "Ataca a alguien (ping)")

pat = Command("le da cariño a", "pat",
              ["https://i.kym-cdn.com/photos/images/original/001/300/413/38e.gif", "https://www.otakuwall.com/wp-content/uploads/76t554s22u661.gif"], True,
              "Das cariño a un amigo :D (ping)")

smile = Command("sonrie jeje :)", "smile", ["https://i.imgur.com/WgChzZ7.gif", "https://www.anacronico-fansub.es/wp-content/uploads/2017/09/tumblr_oukhatgbHH1qc8w4vo1_500.gif", "https://memestatic.fjcdn.com/gifs/Made_74ee26_6503893.gif", "https://memestatic.fjcdn.com/gifs/Made_74ee26_6503893.gif"],
                False, "sonries mucho jaja :D")

dance = Command("se pone a bailar :sunglasses:", "dance",
                ["https://i.imgur.com/ETUfuGo.gif"], False, "baile feliz yeee")

mimir = Command("se fue a mimir~", "mimir", ["https://i.imgur.com/rqrRNjN.gif"],
                False, "a mimir~")

yn = Command("yo opino que...", "yn",
             ["https://i.imgur.com/5uhujGH.gif", "https://i.kym-cdn.com/photos/images/newsfeed/001/712/799/f68.gif"], False,
             "Decide entre sí o no")
punish = Command("castiga a alguien que se portó muy mal", "punish",
                 ["https://i.imgur.com/x6PEBz0.gif", ], True,
                 "castiga a alguien (ping)")
cry = Command("llora :(", "cry", ["https://otakustreintaneras.files.wordpress.com/2017/10/anime_74cf76_63409711.gif?w=300", "https://data.whicdn.com/images/296796968/original.gif"], False, "llora mucho :(")

perdon= Command("pide perdón, meperd0nas?", "perd0n",["https://i0.wp.com/blackandyellowotakugamers.com/wp-content/uploads/2017/08/bow.gif?resize=640%2C511&ssl=1"], True, "pide clemencia (ping)")


recommend = ApiCommand("Esto es una recomendación", "recommend", [], True,
                       "Te recomienda una obra maestra",
                       "https://api.jikan.moe/v3/top/anime/")

simping = MemeCommand("tiene pensamientos impuros sobre", "simp",
                      memes["simp"], True, "simpea a alguien")

chadvsvirgin = MemeCommand("el chad vs el virgen", "virgin",
                           memes["chadvsvirgin"], True, "god vs zzz")

commands.extend([
    hug, wednesday, wakeup, attack, pat, smile, dance, mimir, simping, punish,
    yn, chadvsvirgin, recommend
])

HELP_TEXT = "Lista de comandos: \n\n" + \
            ''.join([f"  -{command.name} \n" for command in commands]) + \
            '\nEspero que esto te haya sido de ayuda'

command_help = Command(HELP_TEXT, "ayuda", [], False,
                       "Muestra la lista de comandos")

commands.append(command_help)
# commands.extend([hug])

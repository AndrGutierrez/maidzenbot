from classes.command import Command

commands = []
hug = Command("es espojos@ y es abrazado por", "abrazo",
              "https://imgur.com/Ty1Q5XN", True, 'Abraza a un ser querido :3')

wednesday = Command("Hoy es miércoles :sunglasses:", "miercoles",
                    "https://imgur.com/Ty1Q5XN", False,
                    "Celebra los miércoles :sunglasses:")

ayuda = Command("these are commands", "ayuda", '', False, 'a')

commands.extend([hug, wednesday])
# commands.extend([hug])

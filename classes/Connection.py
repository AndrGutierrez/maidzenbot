"""Start bot connection"""


class Connection:
    """Discord bot connection Class"""
    def __init__(self, bot, token):
        self.__token = token
        self.__bot = bot

    def start(self):
        """Start connection"""
        try:

            @self.__bot.event
            async def on_ready():
                print(f"{self.__bot.user} has connected to discord")

            @self.__bot.command()
            async def test(ctx):
                await ctx.send('Hello')

            self.__bot.run(self.__token)
        except TypeError:
            print(" Hubo un error al conectar.")

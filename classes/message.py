"""Message model"""
from discord.ext.commands import MemberConverter


class Message():
    """Message model class"""
    def __init__(self, ctx, args):
        self.ctx = ctx
        self.args = args


    async def send(self, ctx, args):
        """Send nessages"""
        users = []
        for arg in args:
            try:
                user = await MemberConverter().convert(ctx, arg)
                users.append(user.mention)
            except:
                pass

        message = '{}'.format(users).replace("'", '').strip('[]')
        await ctx.send(message)

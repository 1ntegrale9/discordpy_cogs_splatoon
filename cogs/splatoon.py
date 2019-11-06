from discord.ext import commands

class Spla2API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api = 'https://spla2.yuu26.com/'

    @commands.command()
    async def api(self, ctx):
        await ctx.send(self.api)

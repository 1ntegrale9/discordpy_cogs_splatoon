from discord.ext import commands
import aiohttp
import io

class Spla2API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.api = 'https://spla2.yuu26.com/'
        self.message_failure = '取得に失敗しました'

    @commands.command()
    async def api(self, ctx):
        await ctx.send(self.api)

    @commands.command()
    async def stage(self, ctx, p1='regular', p2='now'):
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.api}/{p1}/{p2}') as resp:
                if resp.status != 200:
                    return await ctx.send(self.message_failure)
                stages = await resp.json()
                await ctx.send('\n'.join(stages['result'][0]['maps']))

from discord.ext import commands
from cogs.splatoon import Spla2API
import os

bot = commands.Bot(command_prefix='s!')
bot.add_cog(Spla2API(bot))
bot.run(os.getenv('DISCORD_BOT_TOKEN'))

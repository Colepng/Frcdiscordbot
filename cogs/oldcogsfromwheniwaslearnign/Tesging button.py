from sqlite3 import Timestamp
import time
from unicodedata import name
import discord

from discord.ext import commands
from datetime import datetime


class TringToMakeMyOwnThing(commands.Cog):

    def __init__(self, bot: commands.bot):
        self.bot = bot
        self.last_msg = None
    
    @commands.command(name="bouutn")
    async def bouutn(self, ctx:  commands.context):
        embed = discord.Embed(title = "tbutton", description = "Buttton pls work", colour =0x724CF9, timestamp = datetime.utcnow())
        embed.set_author(name = "frcbot")
        embed.add_field(name = "epic gamer", value = "epic hgsamer t69", inline = True)
        embed.set_image(url="https://i.redd.it/2hjf45caleo11.jpg")
        await ctx.send(embed = embed)

def setup(bot: commands.Bot):
    bot.add_cog(TringToMakeMyOwnThing(bot))

from sqlite3 import Timestamp
import time
from unicodedata import name
import discord

from discord.ext import commands
from datetime import datetime

class SomeCommands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        start_time = time.time()
        message = await ctx.send("testing ping...")
        end_time = time.time()
        await message.edit(content = f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")
    
    @commands.command(name="setstatus")
    @commands.cooldown(rate = 1, per = 5)
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """sets the bots status"""
        await self.bot.change_presence(activity=discord.Game(name=text))
    
    @setstatus.error
    async def setstatus_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown, try again after {round(error.retry_after)} seconds.", delete_after = 5)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channnel = self.bot.get_channel(952299094196510811)

        if not channnel:
            return

        await channnel.send(f"Welcome to the cum zone where we cum in anime girls, {member}!")
    
    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        self.last_msg = message

    @commands.command(name="snipe")
    async def snipe(self, ctx: commands.Context):
        """A command to snipe delete messages."""
        if not self.last_msg:  # on_message_delete hasn't been triggered since the bot started
            await ctx.send("There is no message to snipe!")
            return

        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"Message from {author}", description=content)
        await ctx.send(embed=embed)

    @commands.command(name="test_embed")
    async def test_embed(self, ctx: commands.context):
        embed = discord.Embed(title="hello, world!", description = ":D", colour = 0x724CF9, timestamp = datetime.utcnow())
        embed.set_author(name="epic gamer 69 420", icon_url = "https://i.redd.it/2hjf45caleo11.jpg")
        embed.add_field(name="Field 1", value = "Not an inline field!", inline = False)
        embed.add_field(name = "Field 2", value = "An inline field!", inline = True)
        embed.add_field(name = "Field 3", value = "Look I'm inline with field 2!", inline = True)
        embed.set_footer(text="Wow! A fotter!", icon_url = "https://i.redd.it/2hjf45caleo11.jpg")
        await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))

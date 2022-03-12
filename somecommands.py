import discord

from discord.ext import commands # Again, we need this imported


class SomeCommands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms") # It's now self.bot.latency
    
    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """sets the bots status"""
        await self.bot.change_presence(activity=discord.Game(name=text))
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channnel = self.bot.get_channel(952299094196510811)

        if not channnel:
            return

        await channnel.send(f"Welcome to the cum zone where we cum in anime girls, {member}!")

def setup(bot: commands.Bot):
    bot.add_cog(SomeCommands(bot))
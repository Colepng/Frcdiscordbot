import discord   
from discord.ext import commands #Importing what I need'

intents = discord.Intents.all()
intents.voice_states = True

client = discord.Client(intents = intents)
class VoiceChannel(commands.Cog): #Making a class that containts a command that gets all online users

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channnel = self.bot.get_channel(952728011629817856)
        if before.self_mute == False and after.self_mute == True: 
            if not channnel:
                return
            await channnel.send(content = f"{member} has muted")
            return 
        else:
            if not channnel:
                return
            await channnel.send(f"{member} has unmuted")
            return

def setup(bot: commands.Bot):
    bot.add_cog(VoiceChannel(bot))
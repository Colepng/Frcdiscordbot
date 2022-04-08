from os import getenv
import discord
from discord import app_commands
from dotenv import load_dotenv
from discord import app_commands 
import typing

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class dis_drop_down(discord.ui.Select):
    def __init__(self):

        option=[
            discord.SelectOption(Label="ONT",description="Ontairo distrect"),
            discord.SelectOption(Label="FID",description="df"),
        ]
        super().__init__(placeholder="none dis",max_values=1,min_values=1,options=option)




    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Your favoutire colour is {self.values[0]}")


    
class dis_drop_down_view(discord.ui.View):
     def __init__(self):
        super().__init__()

        self.add_item(dis_drop_down())

class bot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=952981899876384778)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

bot = bot()
tree = app_commands.CommandTree(bot)

@tree.command(guild = discord.Object(id=952981899876384778), name = 'tester', description='testing') #guild specific slash command
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"I am working! I was made with Discord.py!", ephemeral = True) 

@tree.command(guild=discord.Object(id=952981899876384778))
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message('test')

@tree.command(guild = discord.Object(id=952981899876384778), name = "district_info", description="Outputs all information about a district")
async def dis_rank(intereraction: discord.Interaction):
    await intereraction.response.send_message(content = "yesst",view = dis_drop_down_view)

load_dotenv()
TOKEN = getenv("TOKEN")
bot.run(TOKEN)

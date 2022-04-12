from os import getenv
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import *

import asyncio

from dropdown_menus import *

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
AUTHY = getenv('AUTHY')

payload={}
headers = {
'Authorization': 'Basic ' + str(AUTHY),
'If-Modified-Since': ''

}

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


tree = app_commands.CommandTree(bot())

@tree.command(guild = discord.Object(id=952981899876384778), name = 'tester', description='testing') #guild specific slash command
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"I am working! I was made with Discord.py!", ephemeral = True) 

@tree.command(guild=discord.Object(id=952981899876384778))
async def slash(interaction: discord.Interaction):
    await interaction.response.send_message('test')

@tree.command(guild = discord.Object(id=952981899876384778), name = "district_info", description="Outputs all information about a district")
async def dis_rank(intereraction: discord.Interaction):
    view = dis_drop_down_view()
    await intereraction.response.send_message(content = "Please select a FRC disrict", view = view)

load_dotenv()
TOKEN = getenv("TOKEN")

async def main():
    async with bot():
        await bot().start(TOKEN)

asyncio.run(main())
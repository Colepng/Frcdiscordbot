from os import environ, unsetenv
from dotenv import load_dotenv

import discord
from discord import app_commands
#from discord.ext import commands

import asyncio

from dropdown_menus import *

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
AUTHY = getenv('AUTHY')

payload={}
headers = {
'Authorization': 'Basic ' + str(AUTHY),
'If-Modified-Since': ''

}

unsetenv("TOKEN")

#class text_input_team_info(discord.ui.Text_input):
   # def __init__(self) -> None:
      #  super().__init__(label="Team Number")

   # async def callback(self, interaction: discord.Interaction):
      #  await interaction


class bot(discord.Client):
    def __init__(self):

        super().__init__(intents=intents,application_id=951567133169557544)
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=952981899876384778)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")
abot = bot()
tree = app_commands.CommandTree(abot)

@tree.command(guild = discord.Object(id=952981899876384778), name = "district_info", description="Outputs all information about a district")
async def dis_rank(intereraction: discord.Interaction):
    view = dis_drop_down_view()
    await intereraction.response.send_message(content = "Please select a FRC disrict", view = view) 

load_dotenv()
TOKEN = getenv("TOKEN")

async def main():
    async with abot:
        print(TOKEN)
        await abot.start(TOKEN)
        

asyncio.run(main())
from os import getenv
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands
import requests

from dropdown_menus import *
from coaskldm import *

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

bot  = commands.Bot(command_prefix="!", intents = intents)

async def main():
    async with bot:
        await bot.load_extension("cogs.dropdown menus")

class bot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        tree = app_commands.CommandTree(bot())
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=952981899876384778)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

load_dotenv()
TOKEN = getenv("TOKEN")
bot.run(TOKEN)
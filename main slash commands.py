import discord          

from dotenv import load_dotenv
from os import getenv 
from discord.ext import commands
from discord import app_commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents = intents)
client = discord.Client(intents=intents,command_prefix="!")
tree = app_commands.CommandTree(client)

load_dotenv()
TOKEN = getenv("TOKEN")

async def main():
    async with bot:
        await bot.load_extension("cogs.FrcAPI slash commands")
        await bot.load_extension("cogs.Commands")
        await bot.start(TOKEN)

asyncio.run(main())
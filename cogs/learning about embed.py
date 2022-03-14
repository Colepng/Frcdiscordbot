from email import message
import discord
import json

from discord.ext import commands
bot = commands.Bot(command_prefix="!")

def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None



f = open("C:\\Users\gamin\\OneDrive\\Documents\\GitHub\\Frcdiscordbot\\config.json",)
config_file = json.load(f)
TOKEN = config_file["token"]
bot.run(TOKEN)
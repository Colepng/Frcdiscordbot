import discord
import json

from discord.ext import commands

intents = discord.Intents.default()
intents.members = True



bot = commands.Bot(command_prefix="!", intents = intents)

bot.load_extension("somecommands")

f = open("C:\\Users\gamin\\OneDrive\\Documents\\GitHub\\Frcdiscordbot\\config.json",)
config_file = json.load(f)
TOKEN = config_file["token"]
bot.run(TOKEN)
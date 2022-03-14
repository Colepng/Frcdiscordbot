import discord
import json

from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents = intents)

bot.load_extension("cogs.somecommands")
bot.load_extension("cogs.Tesging button")
bot.load_extension("cogs.newcommands")
bot.load_extension("cogs.FrcAPI")

f = open("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\config.json",)
config_file = json.load(f)
TOKEN = config_file["token"]
bot.run(TOKEN)
import discord
import json

from discord.ext import commands
<<<<<<< Updated upstream

intents = discord.Intents.default()
intents.members = True


=======

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
>>>>>>> Stashed changes

bot = commands.Bot(command_prefix="!", intents = intents)

bot.load_extension("somecommands")
<<<<<<< Updated upstream

f = open("C:\\Users\gamin\\OneDrive\\Documents\\GitHub\\Frcdiscordbot\\config.json",)
=======
bot.load_extension("Tesging button")
bot.load_extension("newcommands")

f = open("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\config.json",)
>>>>>>> Stashed changes
config_file = json.load(f)
TOKEN = config_file["token"]
bot.run(TOKEN)
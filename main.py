#Here I was importing the json libary to hide keys and importing discord.ext commands moudle and discord.py itself
import discord          

from dotenv import load_dotenv
from os import getenv 
from discord.ext import commands

#Here I am allowing my bot to see the members in a server and there voice status
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

#Here I am setting the command prefix to !

bot = commands.Bot(command_prefix="!", intents = intents)

#Here I'm loading the python files where I stored my commands

bot.load_extension("cogs.somecommands")
bot.load_extension("cogs.Tesging button")
bot.load_extension("cogs.newcommands")
bot.load_extension("cogs.FrcAPI")


#Here I am opening a json file that has my discord bot token and getting that token and puting it into a constent


load_dotenv()
TOKEN = getenv("TOKEN")
print(str(TOKEN) * 20)
bot.run(TOKEN)
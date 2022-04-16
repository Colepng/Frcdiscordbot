#Here I was importing the json libary to hide keys and importing discord.ext commands moudle and discord.py itself
import discord          

from dotenv import load_dotenv
from os import getenv 
from discord.ext import commands
from discord import app_commands

#Here I am allowing my bot to see the members in a server and there voice status
intents = discord.Intents.default()
intents.message_content = True
#Here I am setting the command prefix to !

bot = discord.Client(intents=intents,command_prefix="!")
tree = app_commands.CommandTree(bot)

bot.load_extension("cogs.FrcAPI")
#Here I'm loading the python files where I stored my commands


#Here I am opening a json file that has my discord bot token and getting that token and puting it into a constent
 
load_dotenv()
TOKEN = getenv("TOKEN")
bot.run(TOKEN)
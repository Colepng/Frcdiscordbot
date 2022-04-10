from os import getenv
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord.ext import commands
import requests

from dropdown_menus import *
from Commands import bot


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
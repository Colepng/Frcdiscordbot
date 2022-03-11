from http import client
from pydoc import cli
import discord

TOKEN  = 'OTUxNTY3MTMzMTY5NTU3NTQ0.YipV8w.rZ443vqdMei0mNGoK2suIEAknkI'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.run(TOKEN)

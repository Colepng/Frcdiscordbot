import discord
import json

f = open("C:\\Users\gamin\\OneDrive\\Documents\\GitHub\\Frcdiscordbot\\config.json",)

get_token = json.load(f)
TOKEN = get_token["token"]
TEST = get_token["test"]
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(TEST)

client.run(TOKEN)

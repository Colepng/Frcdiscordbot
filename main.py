import discord
import json

f = open("C:\\Users\gamin\\OneDrive\\Documents\\GitHub\\Frcdiscordbot\\config.json",)

config = json.load(f)
TOKEN = config["token"]
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:
        return

    if user_message.lower() == "hello":
        await message.channel.send(f"Hello {username}!")
        return
    if user_message.lower() == "fuck you":
        await message.channel.send(f"No fuck you {username}!")
        return
client.run(TOKEN)

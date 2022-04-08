from os import getenv
from dotenv import load_dotenv

import discord
from discord import app_commands
from discord import app_commands 

import requests
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

load_dotenv()
AUTHY = getenv('AUTHY')

payload={}
headers = {
'Authorization': 'Basic ' + str(AUTHY),
'If-Modified-Since': ''
}

class dis_drop_down(discord.ui.Select):
    def __init__(self):

        option=[
            discord.SelectOption(label="CHS",description="FIRST Chesapeake District"),
            discord.SelectOption(label="FIM",description="FIRST In Michigan District"),
            discord.SelectOption(label="TX",description="FIRST In Texas District"),
            discord.SelectOption(label="IN",description="FIRST Indiana Robotics District"),
            discord.SelectOption(label="ISR",description="FIRST Israel District"),
            discord.SelectOption(label="FMA",description="FIRST Mid-Atlantic District"),
            discord.SelectOption(label="FNC",description="FIRST North Carolina District"),
            discord.SelectOption(label="NE",description="New England District"),
            discord.SelectOption(label="ONT",description="Ontario District"),
            discord.SelectOption(label="PNW",description="Pacific Northwest District"),
            discord.SelectOption(label="PCH",description="Peachtree District")
        ]
        super().__init__(placeholder="No district selected",max_values=1,min_values=1,options=option)

    async def callback(self, interaction: discord.Interaction):
        dis_code = self.values[0] 
        dis_rank = f"https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCode={dis_code}"
        response = requests.request("GET", dis_rank, headers=headers, data=payload)

        trans_table = response.text.maketrans(",:","\n ",'}{]["')
        response = response.text.translate(trans_table)

        file = open("write_to.txt","w")
        file.write(response)
        file.close()

        await interaction.response.send_message(f"test", file=discord.File("write_to.txt",))

class dis_drop_down_view(discord.ui.View):
     def __init__(self):
        super().__init__()

        self.add_item(dis_drop_down())

class bot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.synced = False #we use this so the bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #check if slash commands have been synced 
            await tree.sync(guild = discord.Object(id=952981899876384778)) #guild specific: leave blank if global (global registration can take 1-24 hours)
            self.synced = True
        print(f"We have logged in as {self.user}.")

bot = bot()
tree = app_commands.CommandTree(bot)

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


load_dotenv()
TOKEN = getenv("TOKEN")
bot.run(TOKEN)

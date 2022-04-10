import requests

import discord

from os import getenv
from dotenv import load_dotenv

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

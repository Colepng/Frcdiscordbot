#I'm importign the requests, json and discord library and also the commands extenstion for discord.py

import os
import requests
import discord

from dotenv import load_dotenv
from discord.ext import commands


#Here Im doing the same thing as in main.py. I am opning the config file and I am geting my key for the frc api and putting it into a constnet

load_dotenv()

AUTHY = os.getenv('AUTHY')

client = discord.Client

#Here I am making a class that goes into commands.Cog which is how discord.py finds its commands
class FrcApi(commands.Cog):
    """Commands that use the Frc API"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    #Here I am making a new command and naming it dis_ranking
    @commands.command(name="dis_ranking")
    #Here I am getting self which is ________, then im getting im setting the varible ctx as commands.Context, I'm also getting the word after the commands and seeting as the varible arg
    async def dis_rank(self, ctx: commands.Context, dis_code):  
        """Outputs the district ranking"""


        payload={}
        headers = {
            'Authorization': 'Basic ' + str(AUTHY),
             'If-Modified-Since': ''
        }
        
        dis_rank = "https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCode=" + str(dis_code)
        response = requests.request("GET", dis_rank, headers=headers, data=payload)  

        file = open("dis_rank.txt","w")
        file.write(response.text.replace(",","\n" ))
        file.close()
        await ctx.send(f"test", file=discord.File("dis_rank.txt",))



       # @dis_rank.error
       # async def dis_ranking_error(self, ctx: commands.Context, error: commands.CommandError): do error handling later
        #    """Handles errors for dis_ranking"""


    @commands.command(name="dis_ranking_team")
    async def dis_rank_team(self, ctx: commands.Context, team_num):
        """Outputs the district ranking"""


        payload={}
        headers = {
            'Authorization': 'Basic ' + str(AUTHY),
             'If-Modified-Since': ''
        }
        
        dis_rank = "https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCode=&teamNumber=" + str(team_num)
        response = requests.request("GET", dis_rank, headers=headers, data=payload)  

        file = open("dis_rank.txt","w")
        file.write(response.text.replace(",","\n" ))
        file.close()
        await ctx.send(f"test", file=discord.File("dis_rank.txt",))

        




def setup(bot: commands.Bot):
    bot.add_cog(FrcApi(bot))
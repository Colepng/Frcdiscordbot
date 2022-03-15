#I'm importign the requests, json and discord library and also the commands extenstion for discord.py

from fnmatch import translate
from gettext import translation
import os
from turtle import title
import requests
import discord

from dotenv import load_dotenv
from discord.ext import commands


#Here Im doing the same thing as in main.py. I am opning the config file and I am geting my key for the frc api and putting it into a constnet

load_dotenv()

AUTHY = os.getenv('AUTHY')

payload={}
headers = {
'Authorization': 'Basic ' + str(AUTHY),
'If-Modified-Since': ''
}

c_year = "2022"


client = discord.Client

#Here I am making a class that goes into commands.Cog which is how discord.py finds its commands
class FrcApi(commands.Cog):
    """Commands that use the Frc API"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    #Here I am making a new command and naming it dis_ranking
    @commands.command(name="district_info")
    #Here I am getting self which is ________, then im getting im setting the varible ctx as commands.Context, I'm also getting the word after the commands and seeting as the varible arg
    async def dis_rank(self, ctx: commands.Context, dis_code, year=None):  
        """Outputs all information about a disrict"""
        if year == None:
            year = c_year

        dis_rank = "https://frc-api.firstinspires.org/v3.0/" + str(year)  + "/rankings/district?districtCode=" + str(dis_code)
        response = requests.request("GET", dis_rank, headers=headers, data=payload)  
        print(AUTHY)
        file = open("dis_rank.txt","w")
        file.write(response.text.replace(",","\n" ))
        file.close()
        await ctx.send(f"Here is the {dis_code} district info", file=discord.File("dis_rank.txt",))



       # @dis_rank.error
       # async def dis_ranking_error(self, ctx: commands.Context, error: commands.CommandError): do error handling later
        #    """Handles errors for dis_ranking"""


    @commands.command(name="team_info")
    async def dis_rank_team(self, ctx: commands.Context, team_num, year=None):
        """Gets teams ranking in there district"""

        if year == None:
            year = c_year

        dis_rank = "https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCode=&teamNumber=" + str(team_num)
        response = requests.request("GET", dis_rank, headers=headers, data=payload) 

        trans_table = response.text.maketrans(",","\n",'"}{][')
        response = response.text.translate(trans_table)
        
        file = open("dis_rank.txt","w")
        file.write(response)
        file.close()
        
        await ctx.send(f"Here is the team {team_num} info", file=discord.File("dis_rank.txt",))
        await ctx.send(f"Here is the team {team_num} info \n" + response)

    @commands.command(name="get_districts")
    async def get_dis(self, ctx:commands.Context, year=None):
        if year == None:
            year = c_year
            
        frc_districts = "https://frc-api.firstinspires.org/v3.0/" + str(year) + "/districts"
        response = requests.request("GET", frc_districts, headers=headers, data=payload) 

        trans_table = response.text.maketrans("{,","\n ",'}]["')
        response = response.text.translate(trans_table)

        file = open("dis_rank.txt", "w")
        file.write(response)
        file.close()

        await ctx.send(f"Here is all frc districts", file=discord.File("dis_rank.txt",))

    @commands.command(name="score")
    async def score(self, ctx: commands.Context):
        """Gets all score info of a """

        
def setup(bot: commands.Bot):
    bot.add_cog(FrcApi(bot))
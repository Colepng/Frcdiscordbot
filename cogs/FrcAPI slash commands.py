#I'm importign the requests, json and discord library and also the commands extenstion for discord.py
import os
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
    async def dis_rank(self, ctx: commands.Context, dis_code=None, year=None):  
        """Outputs all information about a district"""
        if dis_code == None:
            await ctx.send(f"Please input a district code, if your don't know one you can use the !districts command")
        else:
            if year == None:
                year = c_year

            dis_rank = f"https://frc-api.firstinspires.org/v3.0/{year}/rankings/district?districtCode={dis_code}"
            response = requests.request("GET", dis_rank, headers=headers, data=payload)
            file = open("write_to.txt","w")
            file.write(response.text.replace(",","\n" ))
            file.close()
            await ctx.send(f"Here is the {dis_code} district info", file=discord.File("write_to.txt",))



       # @dis_rank.error
       # async def dis_ranking_error(self, ctx: commands.Context, error: commands.CommandError): do error handling later
        #    """Handles errors for dis_ranking"""


    @commands.command(name="team_info")
    async def dis_rank_team(self, ctx: commands.Context, team_num=None, year=None):
        """Gets teams ranking in there district"""

        if team_num == None:
            await ctx.send(f"Please input a team number after the command")
        else:

            if year == None:
                year = c_year

            dis_rank = f"https://frc-api.firstinspires.org/v3.0/{year}/rankings/district?districtCode=&teamNumber={team_num}"
            response = requests.request("GET", dis_rank, headers=headers, data=payload) 

            trans_table = response.text.maketrans(",","\n",'"}{][')
            response = response.text.translate(trans_table)
        
            file = open("write_to.txt","w")
            file.write(response)
            file.close()
        
            await ctx.send(f"Here is the team {team_num} info", file=discord.File("write_to.txt",))
       # await ctx.send(f"Here is the team {team_num} info \n" + response)

    @commands.command(name="districts")
    async def get_dis(self, ctx:commands.Context, year=None):
        """Gets all frc districts"""
        
        if year == None:
            year = c_year

        frc_districts = f"https://frc-api.firstinspires.org/v3.0/{year}/districts"
        response = requests.request("GET", frc_districts, headers=headers, data=payload) 


        trans_table = response.text.maketrans("{,","\n ",'}]["')
        response = response.text.translate(trans_table)

        file = open("write_to.txt", "w")
        file.write(response)
        file.close()

        await ctx.send(f"Here is all frc districts", file=discord.File("write_to.txt",))

    @commands.command(name="score")
    async def score(self, ctx: commands.Context, eventcode, tour_level, team_num=None, start=None, end=None):
        #if year == None:
        year = c_year

        if team_num == None:
                frc_score = f"https://frc-api.firstinspires.org/v3.0/{year}/scores/{eventcode}/{tour_level}?"


        elif team_num == "match":
            frc_score = f"https://frc-api.firstinspires.org/v3.0/{year}/scores/{eventcode}/{tour_level}?matchnumber={start}"

  
        elif team_num != None and start != None and end == None:
            frc_score = f"https://frc-api.firstinspires.org/v3.0/{year}/scores/{eventcode}/{tour_level}?start={team_num}&end={start}"

        else:
            if end == None:
                frc_score = f"https://frc-api.firstinspires.org/v3.0/{year}/scores/{eventcode}/{tour_level}?teamnumber={team_num}"
            else:
                frc_score = f"https://frc-api.firstinspires.org/v3.0/{year}/scores/{eventcode}/{tour_level}?teamnumber={team_num}&start={start}&end={end}"

    
        response = requests.request("GET", frc_score, headers=headers, data=payload)

        trans_table = response.text.maketrans(",","\n",'}{]["')
        response = response.text.translate(trans_table)
        response = response.replace("matchNumber","\n\nmatchNumber")

        file = open("write_to.txt", "w")
        file.write(response)
        file.close()

        await ctx.send(f"The score info you requested", file=discord.File("write_to.txt",) )



async def setup(bot: commands.Bot):
    await bot.add_cog(FrcApi(bot))
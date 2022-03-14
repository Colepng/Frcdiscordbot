import requests
import json
import discord

from discord.ext import commands

con = open("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\config.json",)
config_file = json.load(con)
authy = config_file["key_frc"]
team_num = 0 #team number
dis_rank_with_team = "https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCode{dis}=&teamNumber={tean_num}"

client = discord.Client
class FrcApi(commands.Cog):
    """Commands that use the Frc API"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        from cogs import FrcAPI
    @commands.command(name="dis_ranking")
    async def dis_rank(self, ctx: commands.Context, arg):
        """Outputs the district ranking"""


        payload={}
        headers = {
            'Authorization': 'Basic' + str(authy),
             'If-Modified-Since': ''
        }
        
        dis_rank = "https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCode=" + str(arg)
        response = requests.request("GET", dis_rank, headers=headers, data=payload)  

        file = open("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\dis_rank.txt","w")
        file.write(response.text.replace(",","\n" ))
        file.close()
        await ctx.send(f"test", file=discord.File("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\dis_rank.txt",))

    @commands.command(name="dis_ranking_team")
    async def dis_rank_team(self, ctx: commands.Context, arg):
        """Outputs the district ranking"""


        payload={}
        headers = {
            'Authorization': 'Basic' + str(authy),
             'If-Modified-Since': ''
        }
        
        dis_rank = "https://frc-api.firstinspires.org/v3.0/2022/rankings/district?districtCode=&teamNumber=" + str(arg)
        response = requests.request("GET", dis_rank, headers=headers, data=payload)  

        file = open("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\dis_rank.txt","w")
        file.write(response.text.replace(",","\n" ))
        file.close()
        await ctx.send(f"test", file=discord.File("C:\\Users\\gamin\\OneDrive\\Documents\\Code\\Frcbot\\dis_rank.txt",))

        

def setup(bot: commands.Bot):
    bot.add_cog(FrcApi(bot))
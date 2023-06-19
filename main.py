import discord 
import os 
os.system("pip install -r requirements.txt")
from discord.ext import commands 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="?",intents=intents)


@bot.command()
async def hi(ctx):
 await ctx.send("👋")

bot.run("")

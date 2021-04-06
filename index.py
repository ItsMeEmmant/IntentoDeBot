import discord
from discord.ext import commands
import datetime

from urllib import parse, request
import re


bot = commands.Bot(command_prefix='*')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int): 
    await ctx.send(numOne + numTwo)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Esta es la información de tu server", timestamp=datetime.datetime.utcnow(), color=discord.Color.purple())
    embed.add_field(name="Fecha de creación", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Dueño sel server", value=f"{ctx.guild.owner}")
    embed.add_field(name="Región", value=f"{ctx.guild.region}")
    embed.add_field(name="ID del Server", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url="https://a.ppy.sh/9886340")

    await ctx.send(embed=embed)
    
@bot.command()
async def love(ctx, nombre1: str, nombre2: str): 
    await ctx.send(nombre1 + " y " + nombre2 + " se aman mucho OwO" )

@bot.command()
async def youtube(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html = request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall('href=\"\\/watch\\?v=(.{11})', html.read().decode())
    print(search_results)
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events

@bot.event

async def on_ready():
    print('Que quieres puta')



bot.run('ODI4NDkxODkxNzg3MDM4NzQx.YGqXMw.IMVOllN1ScWWbIC15TkDJmkEM1M')


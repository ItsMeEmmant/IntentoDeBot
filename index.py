import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='*')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int): 
    await ctx.send(numOne + numTwo)

@bot.command()
async def love(ctx, nombre1: str, nombre2: str): 
    await ctx.send(nombre1 + " y " + nombre2 + " se aman mucho OwO" )
# Events

@bot.event

async def on_ready():
    print('Que quieres puta')


bot.run('ODI4NDkxODkxNzg3MDM4NzQx.YGqXMw.IMVOllN1ScWWbIC15TkDJmkEM1M')


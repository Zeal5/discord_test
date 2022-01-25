import discord 
import random
from discord.ext import commands


client = commands.Bot(command_prefix='?')

@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)





client.run('OTM1MzEwNDE2NjY4Njg0NDA4.Ye8xtA.fPZNMJOl6xS2IBDS2pqmY8DSSUg')
    




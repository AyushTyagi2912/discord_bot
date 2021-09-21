import discord
from discord.ext import commands, tasks
import random
from itertools import cycle 

client = commands.Bot(command_prefix='.')
status = cycle(['sleeping','In coma'])
#Events

@client.event
async def on_ready():
    activity = discord.Game(name="DED", type=3)
    await client.change_presence(activity=activity)
    print("Bot is ready!")


#Commands

@client.command()
async def intro(ctx):
    await ctx.send(f"Hello Iam wankstabot my ping is...{round(client.latency * 1000)} ms")

@client.command()
async def Ques(ctx, *, question):
    responses = ['No', 'Yes']
    
    await ctx.send(f"Question: {question}\nAnswer:{random.choice(responses)}")


@client.command()
async def kick(ctx,Member : discord.Member, *, reason=None):
    await Member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'The Ban Hammer has Spoken! {member.display_name} has been banned!')


@client.event
async def on_command_error(ctx,error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('please pass in an amount')  

@client.command()
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit = amount)













client.run('TOKEN')

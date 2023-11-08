import os

import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix='/', intents=intents)

DAILY_LIMIT = 30

levels_to_review = []
has_requested = []

@client.command()
async def request(ctx, id: int, description: str, video: str = None):
   if ctx.author.id in has_requested or len(levels_to_review) >= DAILY_LIMIT:
       await ctx.send("You have reached the daily limit for this command.")
       return

   # Add the level to the list to be reviewed
   level = {
       'id': id,
       'description': description,
       'video': video,
       'user': ctx.author.id
   }
   levels_to_review.append(level)
   has_requested.append(ctx.author.id)

   await ctx.send("Your request has been submitted!")


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

discord_token = os.getenv('DISCORD_TOKEN')

client.run(discord_token)

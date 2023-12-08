import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from button import request_message
import constant
from constant import g_channels, g_roles

load_dotenv()  
SERVER_ID = os.getenv("SERVER_ID")

intents = discord.Intents.default()
client = commands.Bot(command_prefix='/', intents=intents)

DAILY_LIMIT = 30

levels_to_review = []
has_requested = []



@client.tree.command(name = "define_channel", description = "Define channel", guild=discord.Object(id=SERVER_ID))
async def define_channel(inter, channel: discord.TextChannel, channel_type: constant.ChannelType):
    if g_channels.set_channel(channel_type, channel):
        return await inter.response.send_message("Invalid channel type")
    await inter.response.send_message("Channel defined " + str(channel_type) + " in channel #" + str(channel.name))
    


@client.tree.command(name = "define_role", description = "Define role", guild=discord.Object(id=SERVER_ID))
async def define_role(inter, role: discord.Role, role_type: constant.RoleType):
    if g_roles.set_role(role_type, role):
        return await inter.response.send_message("Invalid channel type")
    await inter.response.send_message("Channel defined" + str(role_type) + " in channel #" + str(role.name))
    


@client.tree.command(name = "request", description = "Request a level", guild=discord.Object(id=SERVER_ID))
async def request(inter: discord.Interaction, id: int, description: str = None, video: str = None):
   if g_channels.get_channel(constant.ChannelType.HELPER) is None:
        return await inter.response.send_message("Helper channel not defined")
   if inter.user.id in has_requested or len(levels_to_review) >= DAILY_LIMIT:
        return await inter.response.send_message("You have reached the daily limit for this command.")

   # Add the level to the list to be reviewed
   level = constant.Level(id, description, video, inter.user.id)

   levels_to_review.append(level)
   has_requested.append(inter.user.id)

   if await request_message(level, constant.ChannelType.HELPER):
       return await inter.response.send_message("Helper channel not defined")
   await inter.response.send_message("Your request has been submitted!")


@client.tree.command(name = "list", description = "List", guild=discord.Object(id=SERVER_ID))
async def list(inter: discord.Interaction):
    if len(levels_to_review) == 0:
         await inter.response.send_message("There are no levels to review.")
         return
    
    message = "Levels to review:\n"
    for level in levels_to_review:
         message += f"{level}\n"
    
    await inter.response.send_message(message)


@client.event
async def on_ready():
    await client.tree.sync(guild=discord.Object(id=SERVER_ID))
    print(f'We have logged in as {client.user}')


discord_token = os.getenv('DISCORD_TOKEN')

client.run(discord_token)

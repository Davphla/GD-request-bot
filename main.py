import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
import constant
from discord import Embed, ui, ButtonStyle

load_dotenv()  
SERVER_ID = os.getenv("SERVER_ID")

intents = discord.Intents.default()
client = commands.Bot(command_prefix='/', intents=intents)

DAILY_LIMIT = 30

levels_to_review = []
has_requested = []

helper_channel = None
moderator_channel = None
announcement_channel = None
helper_role = None
moderator_role = None

@client.tree.command(name = "define_channel", description = "Define channel", guild=discord.Object(id=SERVER_ID))
async def define_channel(inter, channel: discord.TextChannel, channel_type: constant.ChannelType):
    if channel_type == constant.ChannelType.HELPER:
        helper_channel = channel.id
    elif channel_type == constant.ChannelType.MODERATOR:
        moderator_channel = channel.id
    elif channel_type == constant.ChannelType.ANNOUNCEMENT:
        announcement_channel = channel.id
    else :
        await inter.response.send_message("Invalid channel type")
    await inter.response.send_message("Channel defined " + str(channel_type))
    

class CoolButton(ui.Button):
    async def callback(self, inter: discord.Interaction):
        await inter.response.send_message('Button clicked!')

@client.tree.command(name = "define_role", description = "Define role", guild=discord.Object(id=SERVER_ID))
async def define_role(inter, role: discord.Role, role_type: constant.RoleType):
    if role_type == constant.RoleType.HELPER:
        helper_role = role.id
    elif role_type == constant.RoleType.MODERATOR:
        moderator_role = role.id
    else :
        await inter.response.send_message("Invalid channel type")
    await inter.response.send_message("Channel defined" + str(role_type))
    


@client.tree.command(name = "approve", description = "Approve a level", guild=discord.Object(id=SERVER_ID))
async def cool_message(inter: discord.Interaction):
    channel = client.get_channel(helper_channel)
    if channel is None:
        await inter.response.send_message("Helper channel not defined")
        return
    
    embed = Embed(title="Level Title", description="This is level description", color=0x00ff00)
    embed.add_field(name="ID", value="40410233", inline=True)
    embed.add_field(name="Video", value="https://www.youtube.com/watch?v=dQw4w9WgXcQ", inline=False)
    embed.set_author(name="MrSpaghetti", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url="https://media.discordapp.net/attachments/1162809730876571839/1177970334314549309/20.png?ex=6574715d&is=6561fc5d&hm=52553fc2ee63c024f3afbec257591cba41bd845e76bf16ca61ba2c72374654bb?size=128")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/852576596949657088/9b7b9b7b7b7b7b7b7b7b7b7b7b7b7b7.png?size=128")
    embed.set_image(url="https://cdn.discordapp.com/avatars/852576596949657088/9b7b9b7b7b7b7b7b7b7b7b7b7b7b7b7.png?size=128")

    view = ui.View()
    button_send = CoolButton(label='Send', style=discord.ButtonStyle.success)
    button_send_feature = CoolButton(label='Send feature', style=discord.ButtonStyle.success)
    button_cancel = CoolButton(label='Reject', style=discord.ButtonStyle.danger)

    view.add_item(button_send)
    view.add_item(button_send_feature)
    view.add_item(button_cancel)

    await inter.response.send_message(embed=embed, view=view)

@client.tree.command(name = "request", description = "Request a level", guild=discord.Object(id=SERVER_ID))
async def request(inter: discord.Interaction, id: int, description: str = None, video: str = None):
   if inter.user.id in has_requested or len(levels_to_review) >= DAILY_LIMIT:
       await inter.response.send_message("You have reached the daily limit for this command.")
       return

   # Add the level to the list to be reviewed
   level = {
       'id': id,
       'description': description,
       'video': video,
       'user': inter.user.id
   }
   levels_to_review.append(level)
   has_requested.append(inter.user.id)

   await inter.response.send_message("Your request has been submitted!")

@client.tree.command(name = "list", description = "List", guild=discord.Object(id=SERVER_ID))
async def list(inter: discord.Interaction):
    print(inter)
    if len(levels_to_review) == 0:
         await inter.response.send_message("There are no levels to review.")
         return
    
    message = "Levels to review:\n"
    for level in levels_to_review:
         message += f"{level['id']} - {level['note']}\n"
    
    await inter.response.send_message(message)


@client.event
async def on_ready():
    await client.tree.sync(guild=discord.Object(id=SERVER_ID))
    print(f'We have logged in as {client.user}')


discord_token = os.getenv('DISCORD_TOKEN')

client.run(discord_token)

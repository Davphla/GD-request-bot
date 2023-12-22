from discord import Embed, ui, ButtonStyle
import discord

import constant
from constant import g_channels, g_roles


class SendButton(ui.Button):
    def __init__(self, level, label, channel_type: constant.ChannelType, feature=False):
        if feature:
            emoji = '<:check:1145070237776105503>'
        else:
            emoji = '<:cross:1145070198269956236>'

        super().__init__(style=ButtonStyle.success, label=label, emoji=emoji)
        self.level = level
        self.feature = feature
        self.channel_type = channel_type
        self.channel_to_send = constant.ChannelType.MODERATOR if channel_type == constant.ChannelType.HELPER else constant.ChannelType.ANNOUNCEMENT

    async def callback(self, inter: discord.Interaction):
        mention = inter.user.mention if self.channel_type != constant.ChannelType.ANNOUNCEMENT else None
            
        if await request_message(self.level, self.channel_to_send, mention=mention, feature=self.feature):
            return await inter.response.send_message(self.channel_type + " channel not defined")

        self.disabled = True
        embed = embed_level(self.level, 0x00ff00)
        embed.add_field(name="Sent for ", value=("feature" if self.feature else "rate"), inline=False)
        embed.add_field(name="Sent by", value=inter.user.mention, inline=False)

        await inter.response.edit_message(embed=embed, view=None)
                     

class RejectButton(ui.Button):
    def __init__(self, level, label):
        super().__init__(style=ButtonStyle.danger, label=label, emoji='👍')
        self.level = level

    async def callback(self, inter: discord.Interaction):
        await inter.response.send_message('Button clicked!')



def embed_level(level: constant.Level, color=0xff0000):
    embed = Embed(title="Level Title", description="This is level description", color=color)
    embed.add_field(name="ID", value=level.id, inline=False)
    embed.add_field(name="Video", value=level.video, inline=False)

    # embed.set_author(name=level.user, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=level.user.avatar_url)
    #embed.set_thumbnail(url=level.user.avatar_url)
    #embed.set_image(url=level.user.avatar_url)

    return embed


async def request_message(level: constant.Level, channel_type: constant.ChannelType, mention=None, feature=None):
    channel = g_channels.get_channel(channel_type)
    if channel is None:
        return True
    
    # Change color of the embed if its an announcement
    if channel_type == constant.ChannelType.ANNOUNCEMENT:
        embed = embed_level(level, 0x00ff00)
    else:
        embed = embed_level(level)
        embed.add_field(name="Previous sent by", value=mention, inline=False)
    if feature is not None:
        embed.add_field(name="Sent for ", value=("feature" if feature else "rate"), inline=False)
    
    view = ui.View()

    
    if channel_type != constant.ChannelType.ANNOUNCEMENT:
        button_send = SendButton(level, 'Send', channel_type)
        button_send_feature = SendButton(level, 'Send feature', channel_type, True)
        button_cancel = RejectButton(level, 'Reject')

        view.add_item(button_send)
        view.add_item(button_send_feature)
        view.add_item(button_cancel)

    await channel.send(embed=embed, view=view)
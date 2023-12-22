
import json
import atexit

import discord
import constant

FILEPATH = 'cache/constants.json'

    
class SaveState:
    def __init__(self, guild: discord.Guild):
        atexit.register(self.save_constants)
        self.guild = guild

    async def create_channel_objects(guild: discord.Guild, channel_ids: dict):
        channels = {}
        for channel_type, channel_id in channel_ids.items():
            channel = guild.get_channel(int(channel_id))
            if channel is not None:
                channels[channel_type] = channel
        return channels

    async def create_role_objects(guild: discord.Guild, role_ids: dict):
        roles = {}
        for role_type, role_id in role_ids.items():
            role = guild.get_role(int(role_id))
            if role is not None:
                roles[role_type] = role
        return roles

    def save_constants(self):
        with open(FILEPATH, 'w') as f:
            json.dump({
                'g_channels': {k: v.id if v else None for k, v in constant.g_channels.data.items()},
                'g_roles': {k: v.id if v else None for k, v in constant.g_roles.data.items()},
            }, f)

    async def load_constants(self):
        global g_channels
        global g_roles

        try:
            with open(FILEPATH, 'r') as f:
                data = json.load(f)
                channel = await self.create_channel_objects(self.guild, data['g_channels'])
                roles = await self.create_role_objects(self.guild, data['g_roles'])
                print(channel)
                g_channels = constant.Channels(channel)
                g_roles = constant.Roles(roles)
        except:
            print("Error loading constants")
            pass

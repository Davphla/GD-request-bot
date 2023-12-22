import dataclasses
from enum import Enum
import discord


class RoleType(Enum):
    HELPER = 0
    MODERATOR = 1

class LevelStatus(Enum):
    PENDING = 0
    APPROVED = 1
    DENIED = 2

class ChannelType(Enum):
    HELPER = 0
    MODERATOR = 1
    ANNOUNCEMENT = 2
    LOG = 3

class Level:
    def __init__(self, id, description, video, user, status: LevelStatus = LevelStatus.PENDING):
        self.id = id
        self.description = description
        self.video = video
        self.user = user
        self.status = status

class LevelRequest:
    def __init__(self, id, description, video, user):
        self.id = id
        self.description = description
        self.video = video
        self.user = user

@dataclasses.dataclass
class Channels:
    data = {
        'helper_channel': None,
        'moderator_channel': None,
        'announcement_channel': None,
        'log_channel': None,
    }

    def __init__(self, dict = None):
        if dict:
            self.data = dict


            
    
    def get_channel(self, channel_type: ChannelType):
        channel_map = {
            ChannelType.HELPER: self.helper_channel,
            ChannelType.MODERATOR: self.moderator_channel,
            ChannelType.ANNOUNCEMENT: self.announcement_channel,
            ChannelType.LOG: self.log_channel,
        }
        return channel_map.get(channel_type, None)
        
    def set_channel(self, channel_type: ChannelType, channel):
        channel_map = {
            ChannelType.HELPER: 'helper_channel',
            ChannelType.MODERATOR: 'moderator_channel',
            ChannelType.ANNOUNCEMENT: 'announcement_channel',
            ChannelType.LOG: 'log_channel',
        }
        self.data[channel_map.get(channel_type)] = channel

@dataclasses.dataclass      
class Roles:
    data = {
        'helper_role': None,
        'moderator_role': None,
    }

    def __init__(self, dict = None):
        if dict:
            self.data = dict

    def get_role(self, role_type: RoleType):
        role_map = {
            RoleType.HELPER: self.helper_role,
            RoleType.MODERATOR: self.moderator_role,
        }
        return role_map.get(role_type, None)
    
    def set_role(self, role_type: RoleType, role):
        role_map = {
            RoleType.HELPER: 'helper_role',
            RoleType.MODERATOR: 'moderator_role',
        }
        self.data[role_map.get(role_type)] = role
        


g_channels = Channels()
g_roles = Roles()

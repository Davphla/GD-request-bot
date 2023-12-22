import dataclasses
from enum import Enum

import json
import atexit

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

class Level:
    def __init__(self, id, description, video, user, status: LevelStatus = LevelStatus.PENDING):
        self.id = id
        self.description = description
        self.video = video
        self.user = user
        self.status = status

@dataclasses.dataclass
class LevelRequest:
    def __init__(self, id, description, video, user):
        self.id = id
        self.description = description
        self.video = video
        self.user = user

@dataclasses.dataclass
class Channels:
    def __init__(self, helper_channel, moderator_channel, announcement_channel, log_channel):
        self.helper_channel = helper_channel
        self.moderator_channel = moderator_channel
        self.announcement_channel = announcement_channel
        self.log_channel = log_channel

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
        setattr(self, channel_map.get(channel_type), channel)
        
class Roles:
    def __init__(self, helper_role, moderator_role):
        self.helper_role = helper_role
        self.moderator_role = moderator_role

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
        setattr(self, role_map.get(role_type), role)


def save_constants():
    with open('cache/constants.json', 'w') as f:
        json.dump({
            'g_channels': g_channels,
            'g_roles': g_roles,
        }, f)

def load_constants():
    global g_channels
    global g_roles

    try:
        with open('cache/constants.json', 'r') as f:
            data = json.load(f)
            g_channels = data['g_channels']
            g_roles = data['g_roles']
    except:
        pass
    
g_channels = Channels(None, None, None, None)
g_roles = Roles(None, None)

load_constants()

atexit.register(save_constants)
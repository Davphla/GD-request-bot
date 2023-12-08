from enum import Enum

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

class LevelRequest:
    def __init__(self, id, description, video, user):
        self.id = id
        self.description = description
        self.video = video
        self.user = user

class Channels:
    def __init__(self, helper_channel, moderator_channel, announcement_channel, log_channel):
        self.helper_channel = helper_channel
        self.moderator_channel = moderator_channel
        self.announcement_channel = announcement_channel
        self.log_channel = log_channel

    def get_channel(self, channel_type: ChannelType):
        if channel_type == ChannelType.HELPER:
            return self.helper_channel
        elif channel_type == ChannelType.MODERATOR:
            return self.moderator_channel
        elif channel_type == ChannelType.ANNOUNCEMENT:
            return self.announcement_channel
        elif channel_type == ChannelType.LOG:
            return self.log_channel
        else:
            return None
        
    def set_channel(self, channel_type: ChannelType, channel):
        if channel_type == ChannelType.HELPER:
            self.helper_channel = channel
        elif channel_type == ChannelType.MODERATOR:
            self.moderator_channel = channel
        elif channel_type == ChannelType.ANNOUNCEMENT:
            self.announcement_channel = channel
        elif channel_type == ChannelType.LOG:
            self.log_channel = channel
        else:
            return True
        
class Roles:
    def __init__(self, helper_role, moderator_role):
        self.helper_role = helper_role
        self.moderator_role = moderator_role

    def get_role(self, role_type: RoleType):
        if role_type == RoleType.HELPER:
            return self.helper_role
        elif role_type == RoleType.MODERATOR:
            return self.moderator_role
        else:
            return None
    
    def set_role(self, role_type: RoleType, role):
        if role_type == RoleType.HELPER:
            self.helper_role = role
        elif role_type == RoleType.MODERATOR:
            self.moderator_role = role
        else:
            return True


g_channels = Channels(None, None, None, None)
g_roles = Roles(None, None)

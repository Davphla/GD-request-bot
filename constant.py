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
    def __init__(self, id, description, video, user, status):
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

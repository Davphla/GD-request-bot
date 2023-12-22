
import dataclasses
import json
import atexit
import constant

FILEPATH = 'cache/constants.json'

    
class SaveState:
    def __init__(self):
        self.load_constants()
        atexit.register(self.save_constants)

    def save_constants(self):
        with open('constants.json', 'w') as f:
            json.dump({
                'g_channels': constant.g_channels,
                'g_roles': constant.g_roles,
            }, f)

    def load_constants(self):
        global g_channels
        global g_roles

        try:
            with open(FILEPATH, 'r') as f:
                data = json.load(f)
                g_channels = constant.Channels(data['g_channels'])
                g_roles = constant.Roles(data['g_roles'])
        except:
            pass

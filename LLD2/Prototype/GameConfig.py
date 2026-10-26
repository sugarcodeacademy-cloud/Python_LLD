from LLD2.Prototype.Cloneable import Cloneable
from copy import deepcopy

class GameConfig(Cloneable):
    def __init__(self, game_map, version, max_players, weapons_enabled, weather_type, health, server_region):
        self.game_map = game_map
        self.version = version
        self.max_players = max_players
        self.weapons_enabled = weapons_enabled
        self.weather_type = weather_type
        self.health = health
        self.server_region = server_region

    def clone(self):
        # clone_object = GameConfig(self.game_map, self.version, self.max_players, self.weapons_enabled, self.weather_type, self.health, self.server_region)
        # return clone_object

        '''
        Problems with passing values to constructor
        1.only primitive data types are deep copied
        2.Non primitive data types like arrays , maps, sets, tuples will point to memory location
        '''
        return deepcopy(self)


from LLD2.Prototype.GameConfigTemplates import GameConfigTemplates
from LLD2.Prototype.GameConfigRegistry import GameConfigRegistry
from LLD2.Prototype.GameConfig import GameConfig
from LLD2.Prototype.GameConfigType import GameConfigType

#self, game_map, version, max_players, weapons_enabled, weather_type, health, server_region)
# erangel_game_config = GameConfig("Erangel", "2.1.3", 100, ["AKM","Shotgun","apples"], "clear", 100, "Asia")
#
# #erangel_game_config_europe = erangel_game_config #shallow_copy
# erangel_game_config_europe = GameConfig("Erangel", "2.1.3", 100, ["AKM","Shotgun","apples"], "clear", 100, "Europe")
# erangel_game_config_europe_rain = GameConfig("Erangel", "2.1.3", 100, ["AKM","Shotgun","apples"], "rainy", 100, "Europe")
# print(erangel_game_config_europe_rain)
# print(erangel_game_config_europe)
# print(erangel_game_config)

'''
Problems with above approach
1. Both Asia and Europe configs are pointing to same memory location, cant copy
2. creating objects manually even if there is only one change or few changes

Solution
1.we have to clone exiting object and customize it but it shouldn't affect existing object
'''

# erangel_game_config = GameConfig("Erangel", "2.1.3", 100, ["AKM","Shotgun","apples"], "clear", 100, "Asia")
#
# erangel_game_config_ranked = erangel_game_config.clone()
# erangel_game_config_ranked.max_players = 50
# erangel_game_config_ranked.weapons_enabled[1] = "Pan"

'''
Problems with above approach
1.client has to populate all the values for the first time 
2.if client closes the app, next time he has to repopulate the config again because the object is lost in the memory 
'''

register = GameConfigTemplates.load_templates()

erangel_battle_royale: GameConfig = register.get_template(GameConfigType.BRERANGEL).clone()
miramar_battle_royale = register.get_template(GameConfigType.BRMIRAMAR).clone()

erangel_battle_royale.server_region = "Europe"
print(erangel_battle_royale)





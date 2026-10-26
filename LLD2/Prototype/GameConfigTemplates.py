from LLD2.Prototype.GameConfigType import GameConfigType
from LLD2.Prototype.GameConfigRegistry import GameConfigRegistry
from LLD2.Prototype.GameConfig import GameConfig
class GameConfigTemplates:
        @staticmethod
        def load_templates():
            erangel_template = GameConfig("Erangel", "2.1.3", 100, ["AKM","Shotgun","apples"], "clear", 100, "Asia")
            miramar_template = GameConfig("Miramar", "2.1.3", 100, ["AKM","Shotgun","apples"], "clear", 100, "Asia")
            ranked_erangel = GameConfig("Erangel", "2.1.3", 50, ["Sniper","AKM", "Pan"], "Rain", 100, "Asia")
            ranked_miramar = GameConfig("Miramar", "2.1.3", 50, ["Sniper","AKM", "Pan"], "Rain", 100, "Asia")
            zombie_mode = GameConfig("ZombieLand", "2.1.3", 10, ["AWM","M16", "AKM"], "Cloudy", 100, "Asia")

            game_config_register = GameConfigRegistry()
            game_config_register.add_template(GameConfigType.BRERANGEL, erangel_template)
            game_config_register.add_template(GameConfigType.BRMIRAMAR, miramar_template)
            game_config_register.add_template(GameConfigType.RANKED_ERANGEL, ranked_erangel)
            game_config_register.add_template(GameConfigType.RANKED_MIRAMAR, ranked_miramar)
            game_config_register.add_template(GameConfigType.ZOMBIE_MODE, zombie_mode)

            return game_config_register
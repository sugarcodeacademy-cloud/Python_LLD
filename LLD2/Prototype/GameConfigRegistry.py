from LLD2.Prototype.Registry import Registry


class GameConfigRegistry(Registry):
    def __init__(self):
        self.registery = {}

    def add_template(self,key,game_config):
        self.registery[key] = game_config

    def get_template(self, key):
        return self.registery.get(key)
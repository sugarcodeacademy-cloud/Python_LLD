from abc import ABC


class Registry(ABC):
    def add_template(self,key,game_config):
        pass

    def get_template(self, key):
        pass


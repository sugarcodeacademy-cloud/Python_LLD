from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def change_pool_size(self):
        pass

    @abstractmethod
    def get_version(self):
        pass

    @abstractmethod
    def create_database_factory(self):
        pass


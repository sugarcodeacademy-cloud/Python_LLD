from abc import ABC, abstractmethod


class Channel(ABC):
    @abstractmethod
    def subscribe(self, subscriber):
        pass

    @abstractmethod
    def unscribe(self, subscriber):
        pass

    @abstractmethod
    def notifyUsers(self):
        pass
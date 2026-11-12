from abc import ABC, abstractmethod


class IceCream(ABC):
    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

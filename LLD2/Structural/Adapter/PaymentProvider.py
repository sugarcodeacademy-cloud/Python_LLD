#This class contains methods related to my application
#PaymentProvider class in Amazon
from abc import ABC, abstractmethod


class PaymentProvider(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

    @abstractmethod
    def get_status(self):
        pass


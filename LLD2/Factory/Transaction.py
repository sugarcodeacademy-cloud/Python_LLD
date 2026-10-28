from abc import ABC, abstractmethod


class Transaction(ABC):
    @abstractmethod
    def begin(self):
        pass

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass
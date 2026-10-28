from abc import ABC, abstractmethod


class Query(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def get_query_string(self):
        pass
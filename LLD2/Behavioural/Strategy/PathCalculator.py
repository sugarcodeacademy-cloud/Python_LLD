from abc import ABC, abstractmethod


class PathCalculator(ABC):
    @abstractmethod
    def findPath(self, source, destination):
        pass
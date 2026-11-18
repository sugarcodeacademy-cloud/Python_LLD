from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, video_name):
        pass
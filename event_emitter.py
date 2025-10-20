from custom_types import EventUUID
from abc import ABC, abstractmethod

class EventEmitter(ABC):

    @abstractmethod
    def initialize():
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def register_event(self, eventID:EventUUID):
        pass

    @abstractmethod
    def action(self, eventID:EventUUID):
        pass

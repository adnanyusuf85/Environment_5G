from abc import ABC, abstractmethod

class TrafficSenseInterface(ABC):

    @abstractmethod
    def get_trafficstate_segment(self):
        pass

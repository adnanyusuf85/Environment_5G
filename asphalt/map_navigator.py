from abc import ABC, abstractmethod
from typing import Dict
from .directions import Directions
from .custom_types import UserUUID, RoadspaceUUID

class MapNavigator(ABC):

    @abstractmethod 
    def request_position(self) -> UserUUID:
        pass
    
    @abstractmethod 
    def request_move(self, user: UserUUID, direction: Directions) -> bool:
        pass

    @abstractmethod
    def request_navigation_options(self, user: UserUUID) -> Dict[Directions, RoadspaceUUID]:
        pass

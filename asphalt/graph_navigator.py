from abc import ABC, abstractmethod
from typing import Dict
from networkx import Graph
from .directions import Directions
from .custom_types import UserUUID, RoadspaceUUID
from .map_navigator import MapNavigator
from .user import User

class GraphNavigator(MapNavigator):

    def __init__(self):
        self.roadspaces: Dict[RoadspaceUUID, Roadspace] = {}
        self.users: Dict[UserUUID, User] = {}
        self.user_position_table: Dict[UserUUID, RoadspaceUUID] = {}
        self.graph:Graph = Graph()
        self.map_navigator = map_navigator


    def request_position(self) -> UserUUID:


    def request_move(self, user: UserUUID, direction: Directions) -> bool:
        pass

    def request_navigation_options(self, user: UserUUID) -> Dict[Directions, RoadspaceUUID]:
        pass

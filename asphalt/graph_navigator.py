from abc import ABC, abstractmethod
from typing import Dict
from networkx import Graph
from .directions import Directions
from .custom_types import UserUUID, RoadspaceUUID
from .map_navigator import MapNavigator
from .user import User
from .roadspace import Roadspace

class GraphNavigator(MapNavigator):

    def __init__(self):
        self.roadspaces: Dict[RoadspaceUUID, Roadspace] = {}
        self.users: Dict[UserUUID, User] = {}
        self.user_position_table: Dict[UserUUID, RoadspaceUUID] = {}
        self.graph:Graph = Graph()




"""
Module defining the User class
"""
from typing import Optional, Dict, List
from uuid import uuid4, UUID
from .directions import Directions
from mapworld import Mapworld
from custom_types import RoadspaceUUID, UserUUID
from map_navigator import MapNavigator

class User():
    """
    A placeholder class for User entities in the road network simulation.
    """
    def __init__(self):
        self.id:UserUUID = uuid4()
        self._heading:Directions = None
        self._map:Optional[MapNavigator] = None
        #self.mobilityProfile = Pedestrian() #Future

    @property
    def location(self) -> RoadspaceUUID:
        return self._location

    @location.setter
    def location(self, value:RoadspaceUUID):
        self._location = value

    @property
    def target_location(self) -> RoadspaceUUID:
        return self._target_location

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value:Directions):
        self._heading = value

    def decide_next_navigation_step(self):
        # Checks what options are available from the map
        # Sets opposite of present heading as last resort
        # Checks distance to destination at egress point
        # Checks turn direction with highest SINR
        #### (lets assume that the AV has 8 direction SINR sensing)
        #### But this would mean that if has to translate own heading based references
        #### back to global directions, which the agent shall use
        # Chooses best egress point based on policy

        raise NotImplementedError()

    ##########################
    # MapNavigator Functions #
    ##########################
    #
    def join_map(self, map_world: MapNavigator):
        self._map = map_world

    def request_position(self) -> UserUUID:
        self._map.request_position(self.id)

    def request_move(self, user, direction) -> bool:
        self._map.request_move(user, direction)

    def request_navigation_options(self) -> Dict[Directions, RoadspaceUUID]:
        self._map.request_navigation_options()

    def request_shortest_path_to_destination(self, target_position: RoadspaceUUID):
        raise NotImplementedError()


    ########################
    # RadioSense Functions #
    ########################

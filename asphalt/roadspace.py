"""
Module defining the Roadspace class, representing a segment of road with 
connections to neighboring segments.
"""
from uuid import UUID, uuid4
from typing import Optional, Dict
from .roadspacetype import RoadSpaceType
from .directions import Directions
from .user import User


class Roadspace:
    """
    Initialize a Roadspace instance.
    A Roadspace represents a segment of road with connections to neighboring segments in various directions.
    It is characterized by its type (e.g., GENERIC, INTERSECTION, ROADSEGMENT) and a unique identifier (UUID).
    """
    def __init__(self, roadspace_type:RoadSpaceType=RoadSpaceType.GENERIC, length:int = 1):
        self.uuid: UUID = uuid4()
        self.neighborhood: Dict[Directions, Optional[UUID]] = {}
        self.roadspace_type: RoadSpaceType = roadspace_type
        self.users: set[User] = set()
        self.length: int = length 
        #self.road_condition = smooth() #Future

    def add_neighbor(self, direction:Directions, neighbor:UUID):
        """
        Link this roadspace to a neighboring roadspace in a specified direction.
        Args:
            direction (Directions): The direction in which to link the neighboring roadspace.   
            neighbor (Roadspace): The neighboring roadspace to link.
        """
        self.neighborhood[direction] = neighbor 
    
    def get_neighbors(self) -> Dict[Directions, Optional[UUID]] :
       """
       Return the neighbors (roadspace) of this roadspace 
       """ 
       available_neighbors = {}

       for direction, neighbor in self.neighborhood:
           if (neighbor is not None):
               available_neighbors[direction] = neighbor
       
       return available_neighbors

    def exists_neighbor(self, direction:Directions) -> bool:
        """
        Check if there is a neighboring roadspace in the specified direction.
        Args:
            direction (Directions): The direction to check for a neighboring roadspace.
        Returns:
            bool: True if a neighboring roadspace exists in the specified direction, False otherwise.
        """
        if (self.neighborhood[direction] is not None):
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        """Return the developer-friendly string representation of the object."""
        return "Roadspace"

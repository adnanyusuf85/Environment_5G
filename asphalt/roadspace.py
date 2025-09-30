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
    def __init__(self, roadspace_type:RoadSpaceType=RoadSpaceType.GENERIC):
        self.neighborhood: Dict[Directions, Optional[Roadspace]] = {d: None for d in Directions}
        self.uuid: UUID = uuid4()
        self.roadspace_type: RoadSpaceType = roadspace_type
        self.users: set[User] = set()


    def set_link_segment(self, direction:Directions, neighbor:'Roadspace', reciprocal:bool=True):
        """
        Link this roadspace to a neighboring roadspace in a specified direction.
        Args:
            direction (Directions): The direction in which to link the neighboring roadspace.   
            neighbor (Roadspace): The neighboring roadspace to link.
            reciprocal (bool): If True, also link the neighbor back to this roadspace in the opposite direction.        
        """
        self.neighborhood[direction] = neighbor 

        if reciprocal:
            neighbor.set_link_segment(direction.opposite, self, False)
    
    def add_user(self, user:User):
        """
        Add a user to the road segment.
        Args:
            user (User): The user to be added to the road segment.
        """
        self.users.add(user)
        
    def remove_user(self, user:User):
        """
        Remove a user from the road segment.
        Args:
            user (User): The user to be removed from the road segment.
        """
        self.users.remove(user)
    
    def get_neighbors(self) -> Dict[Directions, Optional['Roadspace']] :
       """
       Return the neighbors (roadspace) of this roadspace 
       """ 
       return self.neighborhood

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

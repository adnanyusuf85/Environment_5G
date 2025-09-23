"""
Module defining the RoadSegment class, a specialized type of Roadspace.
"""
from typing import Set
from .roadspacetype import RoadSpaceType
from .roadspace import Roadspace
from .user import User


class RoadSegment(Roadspace):
    """
    Initialize a RoadSegment instance.
    A RoadSegment is a specialized type of Roadspace representing a segment of road where users can be present.
    It inherits from the Roadspace class and is characterized by its type being set to ROADSEGMENT
    """
    def __init__(self):
        super().__init__(roadspace_type=RoadSpaceType.ROADSEGMENT)
        self.users: Set[User] = set()
  
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
        
    def __repr__(self) -> str:
        """Return the developer-friendly string representation of the object."""
        return "RoadSegment"
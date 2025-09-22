from .roadspacetype import RoadSpaceType
from .roadspace import Roadspace
from .user import User
from typing import Set

class RoadSegment(Roadspace):
    def __init__(self):
        super().__init__(roadspace_type=RoadSpaceType.ROADSEGMENT)
        self.users: Set[User] = set()
  
    def addUser(self, user:User):
        self.users.add(user)
        
    def removeUser(self, user:User):
        self.users.remove(user)
        
    def __repr__(self) -> str:
        """Return the developer-friendly string representation of the object."""
        return "RoadSegment"
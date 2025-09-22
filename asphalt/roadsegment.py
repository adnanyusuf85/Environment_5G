from roadspacetype import RoadSpaceType
from roadspace import Roadspace
from directions import Directions
from user import User
from typing import Set

class RoadSegment(Roadspace):
    def __init__(self):
        self.users: Set[User] = set()
        self.roadspace_type = RoadSpaceType.ROADSEGMENT
        self.serving_sector = None
        self.serving_sector_sinr = 0

    def linkSegment(self, direction:Directions, road_space:Roadspace, reciprocal=True):
        self.neighborhood[direction] = road_space

        if reciprocal:
            road_space.linkSegment(direction.opposite, self, False)

    def addUser(self, user):
        # Adding a car here, will result in checking the serving sector, and adding a car there
        # and recalculating the PRBs for all user connected to the serving sector
        self.users.add(user)
        self.serving.sector.add_user(user) #TODO

    def removeUser(self, user):
        self.users.remove(user)
        self.serving.sector.add_user(user) #TODO

    def __repr__(self):
        """Return the developer-friendly string representation of the object."""
        return "RoadSegment"

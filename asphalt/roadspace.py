from roadspace import Roadspace
from typing import List
from roadspacetype import RoadSpaceType

class Roadspace:
    def __init__(self):
        self.neighborhood: List[Roadspace] = [None] * 8
        self.roadspace_type = RoadSpaceType.GENERIC

    def __repr__(self):
        """Return the developer-friendly string representation of the object."""
        return "Roadspace"

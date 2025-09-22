from .roadspacetype import RoadSpaceType
from .roadspace import Roadspace

class Intersection(Roadspace):
    def __init__(self):
        super().__init__(roadspace_type=RoadSpaceType.INTERSECTION)

    def __repr__(self) -> str:
        """Return the developer-friendly string representation of the object."""
        return "Intersection"
        


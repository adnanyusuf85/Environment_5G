from typing import Optional, Dict
from .roadspacetype import RoadSpaceType
from .directions import Directions

class Roadspace:
   
    def __init__(self, roadspace_type:RoadSpaceType=RoadSpaceType.GENERIC):
        self.neighborhood: Dict[Directions, Optional[Roadspace]] = {d: None for d in Directions}

    def linkSegment(self, direction:Directions, neighbor:'Roadspace', reciprocal:bool=True):
        self.neighborhood[direction] = neighbor 

        if reciprocal:
            neighbor.linkSegment(direction.opposite, self, False)
    

    def __repr__(self) -> str:
        """Return the developer-friendly string representation of the object."""
        return "Roadspace"

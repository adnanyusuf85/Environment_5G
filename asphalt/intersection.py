"""
Module defining the Intersection class, a specialized type of Roadspace.
"""
from .roadspacetype import RoadSpaceType
from .roadspace import Roadspace

class Intersection(Roadspace):
    """
    Initialize an Intersection instance.
    An Intersection is a specialized type of Roadspace representing a junction where multiple road segments meet.
    It inherits from the Roadspace class and is characterized by its type being set to INTERSECTION
    """
    def __init__(self):
        super().__init__(roadspace_type=RoadSpaceType.INTERSECTION)

    def __repr__(self) -> str:
        """Return the developer-friendly string representation of the object."""
        return "Intersection"
        


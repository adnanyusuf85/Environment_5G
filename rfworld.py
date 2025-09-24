"""
Module defining the CoverageMap class, which manages a mapping between 
Roadspace UUIDs and CoverageTile objects.
"""
from typing import Dict
from uuid import UUID
from asphalt import Roadspace
from asphalt import Mapworld
from fiveg import CoverageTile
from .asphalt.user import User


class RFWorld(Mapworld):
    """
    Manages a mapping between Roadspace UUIDs and their corresponding 
    RFSegment objects.
    Attributes:
        rf_segments (Dict[UUID, RFSegment]): A dictionary mapping Roadspace
        UUIDs to CoverageTile objects.
    Methods:
        add_tile(roadspace: Roadspace, coveragetile: CoverageTile): Adds 
        a CoverageTile to the map associated with a specific Roadspace.
    """

    def __init__(self, name:str="Untitled"):
        """
        Initializes an empty CoverageMap.
        """
        self.name = name
        self.tiles: Dict[UUID, CoverageTile] = {}
        self.roadspaces: Dict[UUID, Roadspace] = {}

    def add_tile(self, roadspace:Roadspace, coveragetile:CoverageTile):
        """
        Adds a CoverageTile to the map associated with a specific Roadspace.
        Args:
            roadspace (Roadspace): The Roadspace object whose UUID will be 
            used as the key.
            coveragetile (CoverageTile): The CoverageTile object to be added 
            to the map.
        """
        self.tiles[roadspace.uuid] = coveragetile
        self.roadspaces[roadspace.uuid] = roadspace

    def add_user_to_roadspace(self, user:User, roadspace:Roadspace):
        """
        Adds a User to a specified Roadspace and updates the User's current
        Roadspace reference."""
        roadspace.add_user(user)
        user.set_current_roadspace(roadspace)
    
    def remove_user_from_roadspace(self, user:User):
        roadspace:Roadspace = user.get_current_roadspace()
        roadspace.remove_user(user)
        user.leave_current_roadspace()
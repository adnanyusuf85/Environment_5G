"""
Module defining the CoverageMap class, which manages a mapping between 
Roadspace UUIDs and CoverageTile objects.
"""
from typing import Dict
from uuid import UUID
from asphalt import Roadspace
from fiveg import CoverageTile


class CoverageMap:
    """
    Manages a mapping between Roadspace UUIDs and their corresponding 
    CoverageTile objects.
    Attributes:
        tiles (Dict[UUID, CoverageTile]): A dictionary mapping Roadspace
        UUIDs to CoverageTile objects.
    Methods:
        add_tile(roadspace: Roadspace, coveragetile: CoverageTile): Adds 
        a CoverageTile to the map associated with a specific Roadspace.
    """

    def __init__(self):
        '''
        Initializes an empty CoverageMap.
        '''
        self.tiles: Dict[UUID, CoverageTile] = {}

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

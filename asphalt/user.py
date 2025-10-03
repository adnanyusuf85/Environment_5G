"""
Module defining the User class
"""
from typing import Optional, Dict, List
from uuid import uuid4, UUID
from .directions import Directions

class User:
    """
    A placeholder class for User entities in the road network simulation.
    """
    def __init__(self):
        self.id:UUID = uuid4()
        self._roadspace_uuid:UUID = None
        self._heading:Directions = None
        #self.mobilityProfile = Pedestrian() #Future

    @property
    def position(self):
        return self._roadspace_uuid
    
    @position.setter
    def position(self, value:uuid4):
        self._roadspace_uuid = value

    @property
    def heading(self):
        return self._heading

    @heading.setter
    def heading(self, value:Directions):
        self._heading = value 
       
 
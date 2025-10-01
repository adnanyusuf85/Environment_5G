"""
Module defining the User class, currently a placeholder.
"""
from typing import Optional, Dict
from uuid import uuid4
from .directions import Directions

class User:
    """
    A placeholder class for User entities in the road network simulation.
    """
    def __init__(self):
        self.id = uuid4()
        self.position_uuid:uuid4 = None
        self.heading:Directions = None
        self.Directions = Directions()

    def teleport(self, roadspace: Roadspace):
        """
        Teleport the user to a specified roadspace.
        Args:   
            roadspace (Roadspace): The roadspace to which the user will be teleported.
        """
        self.position = roadspace

    def leave_mapworld(self):
        """
        Remove the user from the mapworld.
        Args:
            None        
        """
        self.mapworld.leave(self)

    def place_randomly(self):
        """
        Place the user at a random position within the mapworld.
        Args:
            None        
        """
        position:Roadspace = self.mapworld.get_random_position()
        self.teleport(position)

    def get_neighbors(self):
        """
        Return the neighbors (roadspace) of the user's current position.
        """
        return self.position.neighborhood()

    def move(self, direction):
        """
        Move the user in a specified direction if a neighboring roadspace exists.
        Args:
            direction (Directions): The direction in which to move the user.
        """
        neighborhood:Dict[Directions, Optional[Roadspace]] = self.get_neighbors()
        self.position = neighborhood[direction]
 
    def step_ahead(self):
        if self.position.exists_neighbor(self.heading):
            self.position = self.position.neighborhood[self.heading]
        
 
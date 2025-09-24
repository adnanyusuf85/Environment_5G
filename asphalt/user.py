"""
Module defining the User class, currently a placeholder.
"""
from uuid import uuid4
from asphalt import Roadspace
from asphalt import Directions

class User:
    """
    A placeholder class for User entities in the road network simulation.
    """
    def __init__(self, mapworld):
        self.id = uuid4()
        self.position:Roadspace = None
        self.heading:Directions = None
        self.mapworld = mapworld

    def teleport(self, roadspace: Roadspace):
        self.position = roadspace

    
    def leave_mapworld(self):
        self.mapworld.leave(self)
    
    def place_randomly(self):
        position = self.mapworld.get_random_position()
        self.teleport(position)

    def get_neighbors(self):
        return self.position.neighborhood() 

    def move(self, direction):
        neighborhood = self.get_neighbors()
        self.position = neighborhood[direction]

    
    def step_ahead(self):
        if self.position.exists_neighbor(self.heading):
            self.position = self.position.neighborhood[self.heading]
        
    
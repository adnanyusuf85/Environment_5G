import uuid
from geopy.distance import great_circle
from asphalt.directions import Directions, RoadSpace
from typing import Set

class Position:
    def __init__(self, lat, lng):
        self.latitude = lat
        self.longitude = lng

    def distance_to(self, other_position):
        """Calculates the distance to another Position object in kilometers."""
        coords_1 = (self.latitude, self.longitude)
        coords_2 = (other_position.latitude, other_position.longitude)
        return great_circle(coords_1, coords_2).kilometers
    

    def __repr__(self):
        """Provides a clean string representation of the object."""
        return f"Position(lat={self.latitude}, lng={self.longitude})"
    
class User:

    def __init__(self, position:Position):
        self.id = uuid.uuid4()
        self.position = position
        self.segment = None


class MobileUser(User):

    def __init__(self, speedProfile:'SpeedProfileBase'):
        self.speedProfile = speedProfile


class AutonomousVehicle(MobileUser):

    def __init__(self, tile):
        super().__init__(TileHopper())
        self.rf_road_segment = tile
        self.canMoveBackward = False
        self.direction = Directions['East']
    
    def intersection_start():
        self.road_segment_sinr = 0

    def intersection_end():
        self.path_travelled_minimum_sinr.append()    

    
    

class SpeedProfileBase:
    def __init__(self):
        self.max = None
        self.min = None
        self.avg = None


class TileHopper:
    def __init__(self):
        self.direction = None
        
    
    




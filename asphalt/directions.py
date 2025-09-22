from enum import Enum

_opposite_map = {
    0: 3, # Directions.NORTH: Directions.SOUTH
    3: 0, # Directions.SOUTH: Directions.NORTH
    1: 2, # Directions.EAST: Directions.WEST
    2: 1, # Directions.WEST: Directions.EAST
    4: 7, # Directions.NORTHEAST: Directions.SOUTHWEST
    7: 4, # Directions.SOUTHWEST: Directions.NORTHEAST
    6: 5, # Directions.NORTHWEST: Directions.SOUTHEAST
    5: 6 # Directions.SOUTHEAST: Directions.NORTHWEST
}

class Directions(Enum):
    NORTH = 0
    EAST = 1
    WEST = 2
    SOUTH = 3
    NORTHEAST = 4
    SOUTHEAST = 5
    NORTHWEST = 6
    SOUTHWEST = 7

    

    @property
    def opposite(self) -> 'Directions':
        # 1. Get the integer value of the current member (e.g., self.value for NORTH is 0)
        opposite_value:int = _opposite_map[self.value] # type: ignore
        
        # 2. Convert that integer value back into a Directions member (e.g., Directions(2) becomes Directions.SOUTH)
        return Directions(opposite_value)

    


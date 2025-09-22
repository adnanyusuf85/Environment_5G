from enum import Enum

class Directions(Enum):
    NORTH = 0
    EAST = 1
    WEST = 2
    SOUTH = 3
    NORTHEAST = 4
    SOUTHEAST = 5
    NORTHWEST = 6
    SOUTHWEST = 7

    _opposite_map = {
        NORTH: SOUTH,
        SOUTH: NORTH,
        EAST: WEST,
        WEST: EAST,
        NORTHEAST: SOUTHWEST,
        SOUTHWEST: NORTHEAST,
        NORTHWEST: SOUTHEAST,
        SOUTHEAST: NORTHWEST
    }

    @property
    def opposite(self):
        return self._opposite_map[self]



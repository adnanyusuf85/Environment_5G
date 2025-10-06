# mapworld.py
# from __future__ import annotations
from typing import Dict, List, Optional, Set, NewType
import random
from uuid import UUID
from networkx import Graph
from .user import User
from .roadspace import Roadspace
from .directions import Directions
from custom_types import RoadspaceUUID, UserUUID

class Mapworld:
    """Manages all users, roadspaces, and their relationships."""

    def __init__(self):
        self.roadspaces: Dict[RoadspaceUUID, Roadspace] = {}
        self.users: Dict[UserUUID, User] = {}
        self.user_position_table: Dict[UserUUID, RoadspaceUUID] = {}
        self.graph:Graph = Graph()

    def get_roadspace_users(self, uuid:RoadspaceUUID):
        return self.roadspace_occupancy_table[uuid]
    
    def get_user_position(self, uuid: UserUUID):
        return self.user_position_table[uuid]
    
    def add_space(self, space: Roadspace):
        """Adds a roadspace to the world."""
        self.spaces[space.id] = space

    def place_user_randomly(self, user: User):
        """Places a user on a random roadspace."""
        if not self.spaces:
            return # No spaces to place user on
        random_space = random.choice(list(self.spaces.values()))
        self.user_positions[user.id] = random_space

    def get_users_in_space(self, space: Roadspace) -> List[User]:
        """Finds all users in a specific roadspace (less efficient but flexible)."""
        # This is a query, calculated when needed, not stored state.
        # For performance, you might invert the user_positions dict.
        return [user for user_id, user_space in self.user_positions.items()
                if user_space.id == space.id and (user := self._get_user_by_id(user_id))]

    def move_user(self, user: User, direction: Directions):
        """Moves a user to an adjacent space if possible."""
        current_position = self.get_user_position(user)
        if not current_position:
            return # User is not on the map

        next_position = current_position.neighbors.get(direction)
        if next_position:
            self.user_positions[user.id] = next_position
            print(f"Moved user {user.id} to space {next_position.id}")

    # Helper method might be needed to get user object from ID
    def _get_user_by_id(self, user_id: UUID) -> Optional[User]:
        # This part depends on how you store your main list of users.
        # For this example, we assume you have a way to look them up.
        pass
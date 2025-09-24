"""
Defines the Sector class representing a sector in a 5G network.
"""
from typing import List
from .fivegee_user import FiveGUser
class Sector:
    """
    A class representing a sector in a 5G network.
    """
    # Fields/Properties
    ## connected_users: List[User]
    ## totalPRBSlots
    ## FilledPRBSlots
    ## Available
    ## datarate_per_user
    def __init__(self):
        self.connected_users:List[FiveGUser] = []
        self.total_prb_slots = 100

    def connect_user(self, user:FiveGUser):
        """
        Connect a user to the sector.
        Args:    
            user (FiveGUser): The user to be connected to the sector.
        """
        self.connected_users.append(user)

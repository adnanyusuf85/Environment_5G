from uuid import uuid4
from simulator_subscriber import SimulatorSubscriber
from custom_types import RoadspaceUUID, UserUUID, EventUUID
from directions import Directions
from event import Event

class NetworkUser(SimulatorSubscriber):

    def __init__(self):
        super().__init__() # gives NetworkUser access to SimulatorSubscriber's init
        self.id: UserUUID = uuid4()
        self.location: RoadspaceUUID
        self.heading: Directions
        self.speed: float = 10
        self.drive_event: Drive = Drive(1, self.uuid, self.speed)
        self.generic_event: Event = Event(0, self.uuid)
        #self.mobility_profile: MobilityProfile
        #self.navigation_api: NavigationInterface
        #self.road_environment: RoadEnvironment
        #self._active_rf_profile: RFProfile
        # super().???????????????????

    def act(self):
        if (self.goal == self.location):
            pass
        else:
            self.location += self.speed

    # def join_environment(self, road_environment: RoadEnvironment):
    #     self.road_environment = road_environment

    # def set_rf_profile(self, rf_profile: RFProfile):
    #     self._active_rf_profile = rf_profile

    # # SimulatorCog Implementation
    # def initialize():
    #     pass

    # def reset():
    #     pass

    # ##############################


class Drive(Event):
    def __init__(self, timestamp: int, entity_uuid: UserUUID, speed: float = 10):
        super().__init__(timestamp, entity_uuid)
        self.speed = speed

    def execute(self):
         print(f"NetworkUser {self.entity_uuid} has driven at speed {self.speed} {self.timestamp}")
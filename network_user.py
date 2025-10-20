from uuid import uuid4
from event_emitter import SimulatorCog
from custom_types import RoadspaceUUID, UserUUID, EventUUID
from directions import Directions

class NetworkUser(SimulatorCog):

    def __init__(self):
        self.id: UserUUID = uuid4()
        self.location: RoadspaceUUID
        self.heading: Directions
        self.mobility_profile: MobilityProfile
        self.navigation_api: NavigationInterface
        self.road_environment: RoadEnvironment
        self._active_rf_profile: RFProfile

    def join_environment(self, road_environment: RoadEnvironment):
        self.road_environment = road_environment

    def set_rf_profile(self, rf_profile: RFProfile):
        self._active_rf_profile = rf_profile

    # SimulatorCog Implementation
    def initialize():
        pass

    def reset():
        pass

    def act(event_uuid:EventUUID):
        print("Executing", event_uuid)
    # ##############################
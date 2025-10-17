from typing import List
import heapq

class Simulator:

    def __init__(self):
        self.event_queue:List = heapq.heapify([])

    def load_environment(roadspace_environment):
        vehicles_events(world_environment.network_users)
        rf_propagation_events(world_environment.roadspaces)
        road_events(world.environment.roadspaces)
        sector_events()

    def initialize_entities():
        pass

    def step(self):
        event = heapq.heappop(self.event_queue)

    def add_event(self, event:Event):
        heapq.heappush(self.event_queue, event)
import networkx as nx
from typing import List
import heapq 

def add_traffic_signals(graph, traffic_signals):
    graph.add_node((5,0))

def add_autonomous_vehicles(graph, autonomous_vehicles):
    pass

def add_pedestrians(graph, pedestrians):
    pass

def assign_destinations(autonomous_vehicles):
    pass

class Event:
    def action(self):
        pass

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



roadspace_environment = None
roadspace_environment.add_traffic_signals(traffic_signals)
roadspace_environment.add_autonomous_vehicles(autonomous_vehicles)
roadspace_environment.add_pedestrians(pedestrians)
roadspace_environment.add_gnbs(gnbs)


simulator.add_environment(roadspace_environment)

while (True):
    simulation_step(None)

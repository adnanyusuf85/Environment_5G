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





roadspace_environment = None
roadspace_environment.add_traffic_signals(traffic_signals)
roadspace_environment.add_autonomous_vehicles(autonomous_vehicles)
roadspace_environment.add_pedestrians(pedestrians)
roadspace_environment.add_gnbs(gnbs)


simulator.add_environment(roadspace_environment)

while (True):
    simulation_step(None)

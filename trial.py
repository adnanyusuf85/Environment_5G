import networkx as nx
import uuid
from mobility import Position, SpeedProfileBase, TileHopper




class NodeCreator:
    def __init__(self):
        self.UUID

#class Sector:

#    def __init__(self):


    




class GraphElement:
    def __init__(self):
        self.name = True
        self.LeftNode = None
        self.RightNode = None
        self.BackNode = None
        self.FrontNode = None





#class Node(GraphElement):
#    def __init__(self):
        

class Segment(GraphElement):
    def __init__(self, edgeId):
       self.edgeId = edgeId

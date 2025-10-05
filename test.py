from asphalt.roadspace import Roadspace
from asphalt.directions import Directions

r1 = Roadspace()
r2 = Roadspace()

r1.add_neighbor(Directions.EAST, r2.uuid)

neighbors = r1.get_neighbors()
print(neighbors)
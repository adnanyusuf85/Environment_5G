from .rfworld import CoverageMap

area_map = CoverageMap()
road_spaces = []


# sinr, serving station, what neighbors are connected in all directions
# an intersection is a deciding point for which way to go
# at each place the AV can detect SINR/RSRP of neighbors
for i in range(number_of_measurements):
    # number_of_measurements comprises of number of measurments plus number of intersections plus 
    # 
area_map.add_tile()

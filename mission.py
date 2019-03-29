import matplotlib.pyplot as plt
from shapely.geometry.polygon import Polygon
from numpy import dtype
from Astar import astar

class MISSION:
    def __init__(self, discretization_distance=1, worldsize_x=100, worldsize_y=100):
        """
        discretization distance in meters
        worldsizes in meters
        """
        # TODO: Reduce to square exploration area (only one self.worldsize)
        self.worldsize_x = worldsize_x
        self.worldsize_y = worldsize_y
        self.discretization = int(round(worldsize_x / discretization_distance))+1

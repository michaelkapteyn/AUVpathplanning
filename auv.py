import matplotlib.pyplot as plt
from shapely.geometry.polygon import Polygon
from numpy import dtype
from Astar import astar
from dijkstra import global_planner
import numpy as np
import sys

class AUV:
    def __init__(self):
        import numpy as np
        import matplotlib.path as mpath
        from matplotlib.transforms import Affine2D
        from copy import deepcopy

        self.origin = (None,None,None)
        self.goal = (None,None,None)
        self.path = None
        self.mission = None
        self.speed = 10

        # define AUV body [m] (those coordinates are centered on (0,0))
        nose    = [0.    , +2.0]
        noseL   = [-0.25 , +1.5]
        noseR   = [+0.25 , +1.5]
        tailL   = [-0.25 , -1.0]
        tailR   = [+0.25 , -1.0]
        path_data = [
            (mpath.Path.MOVETO, nose),
            (mpath.Path.LINETO, noseR),
            (mpath.Path.LINETO, tailR),
            (mpath.Path.LINETO, tailL),
            (mpath.Path.LINETO, noseL),
            (mpath.Path.CLOSEPOLY, noseL)
            ]

        # store vehicle body data
        self.verts0 = Affine2D().rotate_deg(-90).transform( np.array(list(zip(*path_data))[1], float) )
        self.codes0 = list(zip(*path_data))[0]
        self.height = 0.30 # vehicle diameter (cylindrical body)

    # function for returning vehicle state
    def StateInfo(self):
        print('origin: ',self.origin)
        print('goal: ', self.goal)

    def PlanPath(self, env, alg, cost, heuristic, vis, alpha):
        '''
        This is our intelligent function that comes up with a path!
        '''

        collision_tolerance = 0.2

        if self.origin == None or self.goal == None:
            raise Exception("Path planner did not plan any path. Please specify the AUV's origin and goal first!")

        # select path planning algorithm/method
        if alg == "A*":
            self.path = astar(auv = self, env=env, cost=cost, heuristic=heuristic, vis=vis, alpha = alpha)
        elif alg == "Dijkstra":
            self.path = global_planner(auv=self, env=env, cost=cost, vis=vis, alpha=alpha)
        else:
            speed_x = 0.3
            speed_y = 0.20
            speed_z = 0.00
            vehicle_path = np.zeros((self.mission.discretization, 3))
            for timepoint in range(self.mission.discretization):
                x = self.origin[0] + speed_x * timepoint
                y = self.origin[1] + speed_y * timepoint
                z = self.origin[2] + speed_z * timepoint

                # check whether coordinates are valid or whether they cause a crash
                if env.collision_checker(x,y,z,collision_tolerance) == True:
                    sys.exit("Path planner failed. Your vehicle would have collided at X = " + str(x) + ", Y = " + str(y) + ", Z = " + str(z))

                vehicle_path[timepoint] = np.array([x,y,z])
            setattr(self,'path',vehicle_path)

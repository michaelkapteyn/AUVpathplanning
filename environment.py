import matplotlib.pyplot as plt
from shapely.geometry.polygon import Polygon
from numpy import dtype
from Astar import astar

class ENVIRONMENT:

    def __init__(self,Mission = None, ReefFunction=None, UnknownRegions={}, discretization_x=101, discretization_y=101, blur = False):
        import numpy as np
        # Standard values
        self.showcontours = None
        self.mission = Mission
        self.Dimension_x = self.mission.worldsize_x
        self.Dimension_y = self.mission.worldsize_y
        self.Reef = self.SetReef(ReefFunction)
        self.Current = [0.3,1.1,10]
        self.discretization_x = self.mission.discretization
        self.discretization_y = self.mission.discretization

        self.UnknownRegions = UnknownRegions
        
        # risk
        self.x = np.linspace(0, self.Dimension_x, self.discretization_x)
        self.y = np.linspace(0, self.Dimension_y, self.discretization_y)
        self.X, self.Y = np.meshgrid(self.x, self.y)


        # generate risk and current fields
        self.RiskField = self.GenerateRiskField()
        self.CurrentField_x, self.CurrentField_y = self.GenerateCurrentField(type="none")

        if blur:
            self.Blur()

    def Blur(self):
        self.blur=True
        self.std_dev = 0.0 # up to 1.5 possible
        # blur risk and current fields
        self.RiskField = self.BlurField(self.RiskField, sigma = self.std_dev, dx = self.x[1] - self.x[0], dy = self.y[1] - self.y[0])
        self.CurrentField_x = self.BlurField(self.CurrentField_x, sigma = self.std_dev, dx = self.x[1] - self.x[0], dy = self.y[1] - self.y[0])
        self.CurrentField_y = self.BlurField(self.CurrentField_y, sigma = self.std_dev, dx = self.x[1] - self.x[0], dy = self.y[1] - self.y[0])
    
    def actualRisk(self,x,y,z):
        return self.RiskField[x,y]

    def ReturnRisk(self,x,y,z):
        x = float(x)
        y = float(y)
        z = float(z)
        from shapely.geometry import Point
        from matplotlib import path as mpath
        risk = 0
        ctr = 0
        # step: loop over all unknown regions
        for risk_key in self.UnknownRegions:
            unknown_region = self.UnknownRegions[risk_key]
            region = mpath.Path(unknown_region)
            if region.contains_points([(x, y)]) == True:
                risk += risk_key
                ctr +=1

        # subtract independence P(A and B) = P(A) + P(B) - P(A U B)
        if ctr > 1:
            risk = risk * 0.9**ctr
        # step: check hard collisions with reef
        if self.collision_checker(x, y, z, tol = 0.2) == True:
            risk += 1
        else: pass

        # step: restrict risk to a maximum of 1
        if risk > 1:
            risk = 1
        else: pass

        return risk

    def GenerateCurrentField(self, type = "whirlpool", max_strength=10):
        # TODO: Do not loop over everything anymore but make meshgrid and zip the x and y meshgrids
        import numpy as np
        if type == "none":
            CurrentField_x = np.zeros((len(self.x),len(self.y)))
            CurrentField_y = np.zeros((len(self.x),len(self.y)))
        elif type == "whirlpool":
            X,Y = self.X, self.Y
            lenx = len(X)
            leny = len(Y)
            ind = np.meshgrid(np.arange(-lenx/2,lenx/2),np.arange(-leny/2,leny/2))
            direction = -np.ones(lenx*leny).reshape(lenx, leny)*np.arctan2(ind[0],ind[1])
            CurrentField_x, CurrentField_y = max_strength * np.cos(direction), max_strength * np.sin(direction)
        elif type == "uniformX":
            CurrentField_x = max_strength*np.ones_like(self.X)
            CurrentField_y = 0*np.ones_like(self.X)
        elif type == "uniformY":
            CurrentField_x = 0*np.ones_like(self.X)
            CurrentField_y = max_strength*np.ones_like(self.X)
        else:
            CurrentField_x = np.zeros((len(self.x),len(self.y)))
            CurrentField_y = np.zeros((len(self.x),len(self.y)))
            for i,x in enumerate(self.x):
                for j,y in enumerate(self.y):
                    CurrentField_x[i][j] = x
                    CurrentField_y[i][j] = y
        return CurrentField_x, CurrentField_y

    def GenerateRiskField(self):
        # TODO: Do not loop over everything anymore but make meshgrid and zip the x and y meshgrids
        import numpy as np
        RiskField = np.zeros((len(self.x),len(self.y)))
        for i,x in enumerate(self.x):
            for j,y in enumerate(self.y):
                RiskField[i][j] = self.ReturnRisk(x=x, y=y, z=-9.5)
        return RiskField

    def BlurField(self,r,sigma,dx,dy):
        import scipy.ndimage
        """
        > r is a 2D array of values r_ij = r(x_j, y_i) (could be risk, current, etc.)
        > sigma is the Gaussian std.dev. in meters (in the field)
        > dx, dy are grid spacing in meters (used to scale sigma)
        """
        sigma = (sigma/dx, sigma/dy)
        G = scipy.ndimage.gaussian_filter(r, sigma, mode='reflect', cval=0.0, truncate=4.0)
        return G


    def SetReef(self,ReefFunction):
        import numpy as np
        def StandardReefFunction(x, y):
                x = (x-0.5 *self.Dimension_x)/15
                y = (y-0.5 *self.Dimension_y)/15
                return (1.0 - x / 2.0 + x ** 5.0 + y ** 3.0) * np.exp(-x ** 2.0 - y ** 2.0) - 10.0
        
        def DeepPoolFunction(x, y):
            return -10
        
        # in case no reef function is specified take a standard reef function
        if ReefFunction == None:
            ReefFunction = StandardReefFunction
            self.showcontours = True
        elif ReefFunction == 'pool':
            ReefFunction = DeepPoolFunction
            self.showcontours = False
        else: pass

        return ReefFunction

    def collision_checker(self,x,y,z,tol):
        """
        Checks collisions with the reef
        Assumptions: The reef surface is the actual ground and not a layer. Hence, so far we are not including exploring caves (but maybe later we can).
        """
        from numpy import inf
        import bisect
        if z <= (self.Reef(float(x),float(y))+tol):
        # if (bisect.bisect_left([-inf,max(self.Reef(x,y) - tol, self.Reef(x,y) + tol)], z)) == 1:
            return True
        else: return False

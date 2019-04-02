import numpy as np
from utils import *
def cost(node1, node2, AUVspeed, alpha):
    timetodestination = dist(node1,node2)/AUVspeed
    
    s = computeunitvector(node1,node2)
    V_AUV = s*AUVspeed
    return timetodestination, V_AUV

def heuristic(node1, goalnode, AUVspeed):
    timetodestination = dist(node1,goalnode)/AUVspeed
    return timetodestination 

def costwithrisk(node1, node2, AUVspeed, alpha):
    timetodestination = dist(node1,node2)/AUVspeed
    riskfactor = (1/(1-alpha*node2.risk + 1e-10))
    
    s = computeunitvector(node1,node2)
    V_AUV = s*AUVspeed
    
    return riskfactor*timetodestination, V_AUV

def heuristicwithrisk(node1, node2, AUVspeed):
    timetodestination = dist(node1,node2)/AUVspeed
    return timetodestination 

def costwithcurrents(node1, node2, AUVspeed, alpha):
    S = AUVspeed
    #Use the current at the first node (could also use the average between node1 and node2)"
    V_current = node1.current

    #Unit vector from node1 to node2: use only x,y components
    s = np.array(node2.position)-np.array(node1.position)
    s = s[0:2].flatten()
    ns = np.linalg.norm(s)
    if ns < 1e-10:
        return (0, np.array((0,0)))
    s = s/ns


    c = -(V_current[0]*s[1]-V_current[1]*s[0])

    # Compute V_AUV - the required AUV velocity direction to get us from node1 to node2, accounting for the current
    # uses quadratic formula, so have to check if we want the negative or positive solution
    V_AUVy = (np.sqrt((s[0]**2)*(s[1]**2)*(S**2)+ (s[1]**4)*(S**2) -(s[1]**2)*c**2) -s[0]*c)

    V_AUVpp = np.array((np.sqrt(S**2 - V_AUVy**2),V_AUVy))
    V_AUVpn = np.array((np.sqrt(S**2 - V_AUVy**2),-V_AUVy))
    V_AUVnp = np.array((-np.sqrt(S**2 - V_AUVy**2),V_AUVy))
    V_AUVnn = np.array((-np.sqrt(S**2 - V_AUVy**2),-V_AUVy))

    list = [V_AUVpp,V_AUVpn, V_AUVnp,V_AUVnn]

    V_AUV = list[np.argmax([np.dot(V+V_current,s) for V in list])]

    # compute the speed we are travelling in the target direction, i.e. from node1 to node2
    SpeedInTargetDirection = np.dot(V_AUV,s) + np.dot(V_current,s)

    # compute the time it will take to travel from node1 to node2 - handle edge case that 0 speed=inf time
    time = dist(node1,node2)/SpeedInTargetDirection if SpeedInTargetDirection != 0 else 0
    timeToDestination = (time if time > 0  else np.inf)
    
    riskfactor = (1/(1-alpha*node2.risk + 1e-10))
    
    return riskfactor*timeToDestination, V_AUV

def heuristicwithcurrents(node1, node2, AUVspeed):
    timetodestination = dist(node1,node2)/AUVspeed
    return timetodestination 
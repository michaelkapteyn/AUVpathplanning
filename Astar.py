import numpy as np
import matplotlib.pyplot as plt
from utils import *
class Node:
    """A node class for Dijkstra Pathfinding"""
    def __init__(self, parent=None, position=None, U= None, V=None, current_cost=np.inf):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.current = currentAt(self, U, V)
        self.cost = current_cost
        self.transition_cost = None
        self.V_AUV = None
        self.V_AUVs = None
        self.risk = None
    def __str__(self):
        return str(self.position) + "," + str(self.parent) + "," + str(self.cost)
    def __repr__(self):
        return str(self.position)# + "," + str(self.parent) + "," + str(self.cost) + "," + str(self.transition_cost)
    def __eq__(self, other):
        return self.position == other.position
    def update_transitions(self, edges):
        self.transition_cost = edges
    def update_current_cost(self, new_cost):
        self.cost = new_cost
    def update_vauvs(self, vauvs):
        self.V_AUVs = vauvs

"""
Return a unit vector pointing from node1 to node2
"""
def unitVector(node1, node2): #from node1 to node2
    s =  np.array(node2.position) - np.array(node1.position)
    if np.linalg.norm(s) < 1e-8:
        return np.array((0,0))
    else:
        return s / np.linalg.norm(s)

"""
Compute current at the given node, using matrices U and V of X,Y velocity components respectively
"""
def currentAt(node, U, V):
    if U is None or V is None:
        return None
    return np.array((U[node.position[1], node.position[0]], V[node.position[1], node.position[0]]))

"""
The main astar algorithm.
Input: an AUV object and an Environment object
Output: the computed path as a list of Nodes, in the order they are visited
        each node has .VUAV attribute, which is the AUV velocity vector at that node
"""
def traversal(node1, node2, S):
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

    # V_AUV = S*s

    # compute the speed we are travelling in the target direction, i.e. from node1 to node2
    SpeedInTargetDirection = np.dot(V_AUV,s) + np.dot(V_current,s)

    # compute the time it will take to travel from node1 to node2 - handle edge case that 0 speed=inf time
    time = dist(node1,node2)/SpeedInTargetDirection if SpeedInTargetDirection != 0 else 0
    timeToDestination = (time if time > 0  else np.inf)
    return timeToDestination, V_AUV

"""
The main A* algorithm.
Input: an AUV object and an Environment object
Output: the computed path as a list of Nodes, in the order they are visited
        each node has .VUAV attribute, which is the AUV velocity vector at that node
"""
def astar(auv, env, cost, heuristic, alpha, vis):
    debug = False
    start = auv.origin
    end = auv.goal
    X = env.X
    Y = env.Y
    U, V = env.CurrentField_x, env.CurrentField_y
    # Create start and end node
    start_node = Node(None, start, U, V)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end, U, V)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    start_node.V_AUV = np.array((0,0))
    open_list.append(start_node)

    if vis is not None:
        vis.ax.scatter(start_node.position[0], start_node.position[1])
        vis.ax.scatter(end_node.position[0], end_node.position[1])
        # vis.ax.quiver(X,Y,U,V, alpha=.75)
    start_node.risk = 0
    start_node.timeToChild = 0.001
    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node (node with smallest f value i.e. cost-to-go)
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        if vis is not None:
            vis.ax.scatter(current_node.position[0], current_node.position[1], facecolors='g', edgecolors='g')
            plt.show()
            # vus.ax.quiver(current_node.position[0], current_node.position[1],current_node.V_AUV[0], current_node.V_AUV[1],units='width')

        # Found the goal
        if dist(current_node, end_node) < 1e-8:
            path = []
            current = current_node
            while current is not None:
                path.append(current)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2])

            # Make sure within range
            if node_position[0] > env.Dimension_x or node_position[0] < 0 or node_position[1] > env.Dimension_y or node_position[1] < 0:
                continue

            # # Make sure walkable terrain
            # if maze[node_position[0]][node_position[1]] != 0:
            #     continue

            # Create new node
            new_node = Node(current_node, node_position, U, V)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            S = auv.speed
            # Create the f, g, and h values
            child.risk = env.actualRisk(child.position[0],child.position[1],child.position[2])
            if cost.__name__ == "cost_no_current_no_risk":
                child.timeToChild, child.V_AUV = cost(current_node, child, S)
            else: 
                child.timeToChild, child.V_AUV = cost(current_node, child, S, alpha)
            child.g = current_node.g + child.timeToChild


            timeToGoal = heuristic(child, end_node, S)
            child.h = timeToGoal

            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)
            if vis is not None:
                vis.ax.scatter(child.position[0], child.position[1], facecolors='none', edgecolors='r')
        if vis is not None:
            plt.pause(0.01)
    if vis is not None:
        plt.show()


# def main():
#     X,Y,U,V = whirlpool_current(0, 100, 0, 100, 1, None)
#
#     start = (40, 50)
#     end = (75, 50)
#
#     path = astar(maze, start, end, X, Y, U, V)
#     # print(path)
#     plt.pause(100)
#
# if __name__ == '__main__':
#     main()

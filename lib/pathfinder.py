from Exceptions import *

def ShortestDistance(aX,aY,Points):
    Sorted = []
    Shortest = {'d': 99999}
    for P in Points:
        d = Distance(aX,aY,P['X'],P['Y'])
        Sorted['d'] = d
        Sorted.extend(P)
    for S in Sorted:
        if S['d'] < Shortest['d']:
            del Shortest[:]
            Shortest.append(S)
    return (Shortest['X'],Shortest['Y'])

def Neighbors(X,Y,RawGrid=None,RequirePassable=False):
    N = []
    for aX in (X, X-1, X+1):
        for aY in (Y, Y-1, Y+1):
            if not (aX == X and aY == Y):
                N.append({'X': aX, 'Y': aY})
    if RequirePassable:
        if RawGrid is None:
            raise PathfinderException
        N = [P for P in N if RawGrid[P['Y']][P['X']].IsPassable]
    return N

def Distance(aX,aY,bX,bY):
    return abs(aX-bX) + abs(aY-bY)

class Pathfinder(object):

    def __init__(self,RawGrid):
        self.RawGrid = RawGrid

    def path(self,aX,aY,bX,bY):
        if not (self.RawGrid[aY][aX].IsPassable and self.RawGrid[bY][bX].IsPassable):
            raise PathfinderException

        Finished = False

        Q = [] #node queue
        V = [] #visited nodes

        Start = {'X': aX, 'Y': aY}
        Goal  = {'X': bX, 'Y': bY}

        Cur = Start

        while not Finished:
            V.append(Cur)
            Q = Neighbors(Cur['X'],Cur['Y'],self.RawGrid,RequirePassable=True)
            Q = [P for P in Q if P not in V] #remove visited nodes from node queue
            if not Q:
                raise PathNotFoundException
            BestChoice = ShortestDistance(bX,bY,Q)
            if BestChoice == Goal:
                Finished = True
                break
            Cur = BestChoice







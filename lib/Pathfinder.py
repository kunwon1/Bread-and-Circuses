from Exceptions import *

from queue import Queue

def ShortestDistance(aX,aY,Points):

    # given a point 'a' and a list of Points, return the Point
    # with shortest manhattan distance from 'a'

    Sorted = []
    Shortest = {'d': 99999}
    for P in Points:
        d = Distance(aX,aY,P['X'],P['Y'])
        P['d'] = d
        Sorted.append(P)
    for S in Sorted:
        if S['d'] < Shortest['d']:
            Shortest = S
    Shortest.pop('d', None)
    return Shortest

def Neighbors(P,RawGrid=None,RequirePassable=False):
    N = []
    X = P[0]
    Y = P[1]
    for aX in (X, X-1, X+1):
        for aY in (Y, Y-1, Y+1):
            if not (aX == X and aY == Y):
                N.append((aX,aY))
    if RequirePassable:
        if RawGrid is None:
            raise PathfinderException
        N = [P for P in N if RawGrid[P[1]][P[0]].IsPassable()]
    return N

def Distance(aX,aY,bX,bY):
    return abs(aX-bX) + abs(aY-bY)

class Pathfinder(object):

    def __init__(self,RawGrid,debug=False):
        self.RawGrid = RawGrid
        self.debug = debug

    def path(self,aX,aY,bX,bY):
        if not (self.RawGrid[aY][aX].IsPassable() and self.RawGrid[bY][bX].IsPassable()):
            raise PathfinderException

        self.RawGrid[aY][aX].TileSymbol = 'S'
        self.RawGrid[bY][bX].TileSymbol = 'G'

        Start = (aX,aY)
        Goal = (bX,bY)

        Frontier = Queue()
        Frontier.put(Start)

        CameFrom = {}
        CameFrom[Start] = None

        Found = False

        while (not Frontier.empty() and not Found):
            Cur = Frontier.get()
            if not Cur == Start:
                self.RawGrid[Cur[1]][Cur[0]].TileSymbol = '*'
            for C in Neighbors(Cur,self.RawGrid,RequirePassable=True):
                if C == Goal:
                    Found = True
                if C not in CameFrom:
                    Frontier.put(C)
                    CameFrom[C] = Cur
        raise PathNotFoundException














from Exceptions import *

def ShortestDistance(aX,aY,Points):
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

def Neighbors(X,Y,RawGrid=None,RequirePassable=False):
    N = []
    for aX in (X, X-1, X+1):
        for aY in (Y, Y-1, Y+1):
            if not (aX == X and aY == Y):
                N.append({'X': aX, 'Y': aY})
    if RequirePassable:
        if RawGrid is None:
            raise PathfinderException
        N = [P for P in N if RawGrid[P['Y']][P['X']].IsPassable()]
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

        Finished = False
        Iterations = 0

        Q = [] #node queue
        V = [] #visited nodes

        Start = {'X': aX, 'Y': aY}
        Goal  = {'X': bX, 'Y': bY}

        if self.debug:
            self.RawGrid[Start['Y']][Start['X']].TileSymbol = 'S'
            self.RawGrid[Goal['Y']][Goal['X']].TileSymbol = 'G'

        Cur = Start

        while not Finished:
            Iterations = Iterations + 1
            V.append(Cur)
            if self.debug:
                if not Cur == Start:
                    self.RawGrid[Cur['Y']][Cur['X']].TileSymbol = '*'
            Q = Neighbors(Cur['X'],Cur['Y'],self.RawGrid,RequirePassable=True)
            OldQ = Q
            Q = [P for P in Q if P not in V] #remove visited nodes from node queue
            if not Q:
                if self.debug:
                    print('No path available, recycling')
                if Iterations > 1000:
                    if self.debug:
                        print('Took too long, bailing')
                    raise PathNotFoundException
                Q = OldQ
                V = []
            BestChoice = ShortestDistance(bX,bY,Q)
            if BestChoice == Goal:
                if self.debug:
                    print('Reached our goal')
                Finished = True
                break
            Cur = BestChoice
            if self.debug:
                pass
                #print('Now evaluating %s,%s' % (Cur['X'],Cur['Y']))







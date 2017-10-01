import random
from queue import PriorityQueue

from pyarena.Exceptions import *

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

def MoveCost(a,b):
    if a[0] == b[0] or a[1] == b[1]:
        return 5 
    else:
        return 6

class Pathfinder(object):

    def __init__(self,RawGrid,debug=False):
        self.RawGrid = RawGrid
        self.debug = debug

    def path(self,aX,aY,bX,bY):
        if not (self.RawGrid[aY][aX].IsPassable() and self.RawGrid[bY][bX].IsPassable()):
            raise PathfinderException

        Start = (aX,aY)
        Goal = (bX,bY)

        Frontier = PriorityQueue()
        Frontier.put(Start, 0)
        From = {}
        Cost = {}

        From[Start] = None
        Cost[Start] = 1

        Found = False

        while ((not Frontier.empty()) and (not Found)):
            Cur = Frontier.get()
            if Cur == Goal:
                Found = True

            for C in Neighbors(Cur,self.RawGrid,RequirePassable=True):
                if C == Goal:
                    Found = True
                NewCost = Cost[Cur] + MoveCost(Cur, C)
                if (C not in Cost) or (NewCost < Cost[C]):
                    Cost[C] = NewCost
                    Priority = NewCost + Distance(Goal[0],Goal[1],C[0],C[1])
                    Frontier.put(C, Priority)
                    From[C] = Cur

        if not Found:
            raise PathNotFoundException
        else:
            if self.debug:
                a = Goal
                while From[a] != None:
                    #print(From[a])
                    if a != Start and a != Goal:
                        self.RawGrid[a[1]][a[0]].TileSymbol = '*'
                    a = From[a]

    def RoomIsConnected(self,RoomA,RoomB):
        A = RoomA.RandomCellAddress()
        B = RoomB.RandomCellAddress()

        try:
            #print('Trying %s,%s to %s,%s' % (A[0],A[1],B[0],B[1]))
            self.path(A[0],A[1],B[0],B[1])
        except PathNotFoundException:
            #print('IND Returning false')
            return False
        else:
            #print('IND Returning True')
            return True



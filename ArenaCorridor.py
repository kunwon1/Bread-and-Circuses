import random
from Exceptions import *

class CorridorVal(object):

    def __init__(self,num):
        self.num = int(num)

    def __index__(self):
        return self.num

    def __repr__(self):
        return self.num

    def __str__(self):
        return str(self.num)

    def __add__(self,other):
        return CorridorVal(self.num + other)

    def __sub__(self,other):
        return CorridorVal(self.num - other)
    
    def __le__(self,other):
        return self.num <= other

    def __ge__(self,other):
        return self.num >= other

    def Approach(self,dest):
        if self.num < dest.num:
            return self.num + 1
        if self.num > dest.num:
            return self.num - 1
        if self.num == dest.num:
            raise CorridorDoneEception


class ArenaCorridor(object):

    def __init__(self,RawGrid,StartCell,EndCell):
        aX = CorridorVal(StartCell[0])
        aY = CorridorVal(StartCell[1])
        bX = CorridorVal(EndCell[0])
        bY = CorridorVal(EndCell[1])

        for y in (aY, bY):
            for x in (aX, bX):
                if y+1 >= len(RawGrid) or y-1 <= 1:
                    raise CorridorException
                if x+1 >= len(RawGrid[y]) or x-1 <= 1:
                    raise CorridorException

        r = random.randint(1,2)

        xDone = False
        yDone = False

        if r == 1:
            while xDone == False:
                try:
                    oldX = aX
                    aX = CorridorVal(aX.Approach(bX))
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[aY][oldX].TileSymbol = '.'
                except CorridorDoneEception:
                    xDone = True
            while yDone == False:
                try:
                    oldY = aY
                    aY = CorridorVal(aY.Approach(bY))
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[oldY][aX].TileSymbol = '.'
                except CorridorDoneEception:
                    yDone = True

        else:
             while yDone == False:
                try:
                    oldY = aY
                    aY = CorridorVal(aY.Approach(bY))
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[oldY][aX].TileSymbol = '.'
                except CorridorDoneEception:
                    yDone = True
             while xDone == False:
                try:
                    oldX = aX
                    aX = CorridorVal(aX.Approach(bX))
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[aY][oldX].TileSymbol = '.'
                except CorridorDoneEception:
                    xDone = True
  
           



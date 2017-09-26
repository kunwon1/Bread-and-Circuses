import random
from lib import Pathfinder
from Exceptions import *

def Approach(s,f):
    if f > s:
        return s + 1
    if f < s:
        return s - 1
    if f == s:
        raise CorridorDoneException

class ArenaCorridor(object):

    def __init__(self,RawGrid,StartCell,EndCell):
        aX = StartCell[0]
        aY = StartCell[1]
        bX = EndCell[0]
        bY = EndCell[1]

        self.RawGrid = RawGrid

        for y in (aY, bY):
            for x in (aX, bX):
                if y+1 >= len(RawGrid) or y-1 <= 1:
                    raise CorridorException
                if x+1 >= len(RawGrid[y]) or x-1 <= 1:
                    raise CorridorException

        r = random.randint(1,610)

        xDone = False
        yDone = False

        if r == 1:
            while xDone == False:
                if self.IsConnected(aX,aY,bX,bY):
                    break
                try:
                    oldX = aX
                    aX = Approach(aX,bX)
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[aY][oldX].TileSymbol = '.'
                except CorridorDoneException:
                    xDone = True
            while yDone == False:
                if self.IsConnected(aX,aY,bX,bY):
                    break
                try:
                    oldY = aY
                    aY = Approach(aY,bY) 
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[oldY][aX].TileSymbol = '.'
                except CorridorDoneException:
                    yDone = True

        if r == 2:
            while yDone == False:
                if self.IsConnected(aX,aY,bX,bY):
                    break
                try:
                    oldY = aY
                    aY = Approach(aY,bY)
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[oldY][aX].TileSymbol = '.'
                except CorridorDoneException:
                    yDone = True
            while xDone == False:
                if self.IsConnected(aX,aY,bX,bY):
                    break
                try:
                    oldX = aX
                    aX = Approach(aX,bX)
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[aY][oldX].TileSymbol = '.'
                except CorridorDoneException:
                    xDone = True
        else:
            while yDone == False and xDone == False:
                if self.IsConnected(aX,aY,bX,bY):
                    break
                try:
                    oldY = aY
                    oldX = aX
                    aY = Approach(aY,bY)
                    aX = Approach(aX,bX)
                    RawGrid[aY][aX].TileSymbol = '.'
                    RawGrid[oldY][oldX].TileSymbol = '.'
                except CorridorDoneException:
                    if aY == bY:
                        yDone = True
                    if aX == bX:
                        xDone = True
            r = random.randint(1,2)
    
            if r == 1:
                while xDone == False:
                    if self.IsConnected(aX,aY,bX,bY):
                        break
                    try:
                        oldX = aX
                        aX = Approach(aX,bX)
                        RawGrid[aY][aX].TileSymbol = '.'
                        RawGrid[aY][oldX].TileSymbol = '.'
                    except CorridorDoneException:
                        xDone = True
                while yDone == False:
                    if self.IsConnected(aX,aY,bX,bY):
                        break
                    try:
                        oldY = aY
                        aY = Approach(aY,bY) 
                        RawGrid[aY][aX].TileSymbol = '.'
                        RawGrid[oldY][aX].TileSymbol = '.'
                    except CorridorDoneException:
                        yDone = True
    
            if r == 2:
                while yDone == False:
                    if self.IsConnected(aX,aY,bX,bY):
                        break
                    try:
                        oldY = aY
                        aY = Approach(aY,bY)
                        RawGrid[aY][aX].TileSymbol = '.'
                        RawGrid[oldY][aX].TileSymbol = '.'
                    except CorridorDoneException:
                        yDone = True
                while xDone == False:
                    if self.IsConnected(aX,aY,bX,bY):
                        break
                    try:
                        oldX = aX
                        aX = Approach(aX,bX)
                        RawGrid[aY][aX].TileSymbol = '.'
                        RawGrid[aY][oldX].TileSymbol = '.'
                    except CorridorDoneException:
                        xDone = True
 

    def IsConnected(self,aX,aY,bX,bY):
        #print('Doing %s,%s %s,%s' % (aX,aY,bX,bY))
        finder = Pathfinder.Pathfinder(self.RawGrid)
        try:
            finder.path(aX,aY,bX,bY)
        except (PathNotFoundException,PathfinderException) as e:
            return False
        else:
            return True
  
           



import random

class CorridorException(Exception):
    pass

class CorridorValException(Exception):
    pass

class CorridorVal(object):

    def __init__(self,num):
        self.num = int(num)

    def __index__(self):
        return self.num

    def __repr__(self):
        return self.num

    def __str__(self):
        return str(self.num)

    def Approach(self,dest):
        if self.num < dest.num:
            return self.num + 1
        if self.num > dest.num:
            return self.num - 1
        if self.num == dest.num:
            raise CorridorValException


class ArenaCorridor(object):

    def __init__(self,RawGrid,StartCell,EndCell):
        aX = CorridorVal(StartCell[0])
        aY = CorridorVal(StartCell[1])
        bX = CorridorVal(EndCell[0])
        bY = CorridorVal(EndCell[1])

        r = random.randint(1,2)

        xDone = False
        yDone = False

        if r == 1:
            while xDone == False:
                try:
                    aX = CorridorVal(aX.Approach(bX))
                    RawGrid[aY][aX].TileSymbol = '.'
                except CorridorValException:
                    xDone = True
            while yDone == False:
                try:
                    aY = CorridorVal(aY.Approach(bY))
                    RawGrid[aY][aX].TileSymbol = '.'
                except CorridorValException:
                    yDone = True

        else:
             while yDone == False:
                try:
                    aY = CorridorVal(aY.Approach(bY))
                    RawGrid[aY][aX].TileSymbol = '.'
                except CorridorValException:
                    yDone = True
             while xDone == False:
                try:
                    aX = CorridorVal(aX.Approach(bX))
                    RawGrid[aY][aX].TileSymbol = '.'
                except CorridorValException:
                    xDone = True
  
           



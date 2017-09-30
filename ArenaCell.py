# Copyright (c) 2017 David J Moore

class ArenaCell(object):

    def __init__(self,myX,myY):

        self.X = myX
        self.Y = myY

        self.TileSymbol = '#'

    def __str__(self):
        #return '%s%s,%s%s' % (self.TileSymbol,self.X,self.Y,self.TileSymbol)
        return '%s' % self.TileSymbol

    def IsPassable(self):
        return self.TileSymbol != '#'


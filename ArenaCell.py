class ArenaCell(object):

    def __init__(self,myX,myY):

        self.MapX = myX
        self.MapY = myY

        self.TileSymbol = '#'

    def __str__(self):
        #return '%s%s,%s%s' % (self.TileSymbol,self.MapX,self.MapY,self.TileSymbol)
        return '%s' % self.TileSymbol


import random

class ArenaRoom(object):

    def __init__(self,StartCell,min=5,max=15):
        self.ROOM_OK             = 0;
        self.ARENA_OUT_OF_BOUNDS = 1;

        self.RoomX = random.randint(min,max)
        self.RoomY = random.randint(min,max)

        self.StartX = StartCell.X
        self.StartY = StartCell.Y
        self.EndX = self.StartX + self.RoomX
        self.EndY = self.StartY + self.RoomY

    def __eq__(self, other):
        return self.StartX == other.StartX and self.StartY == other.StartY

    def RandomCellAddress(self):
        rX = random.randint(self.StartX+1,self.EndX-1)
        rY = random.randint(self.StartY+1,self.EndY-1)
        return(rX,rY)

    def Paint(self, RawGrid):
        # do painting

        if self.EndY >= len(RawGrid) or self.EndX >= len(RawGrid[self.EndY]):
            return self.ARENA_OUT_OF_BOUNDS

        #print('drawing %s,%s to %s,%s' % (self.StartX,self.StartY,self.StartX+self.RoomX,self.StartY+self.RoomY))
        
        for y in range(self.StartY,self.StartY + self.RoomY):
            for x in range(self.StartX,self.StartX + self.RoomX):
                if RawGrid[y][x].TileSymbol != '#':
                    #print('nevermind, bad room')
                    return self.ARENA_OUT_OF_BOUNDS
                if RawGrid[y+1][x+1].TileSymbol != '#':
                    #print('nevermind, bad room')
                    return self.ARENA_OUT_OF_BOUNDS
                if RawGrid[y-1][x-1].TileSymbol != '#':
                    #print('nevermind, bad room')
                    return self.ARENA_OUT_OF_BOUNDS

        for y in range(self.StartY,self.StartY + self.RoomY):
            for x in range(self.StartX,self.StartX + self.RoomX):
                RawGrid[y][x].TileSymbol = '.'
 
        #print('yep, good room')
        return self.ROOM_OK



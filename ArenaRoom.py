import random

class ArenaRoom(object):

    def __init__(self,StartCell):
        self.ROOM_OK             = 0;
        self.ARENA_OUT_OF_BOUNDS = 1;

        self.RoomX = random.randint(2,20)
        self.RoomY = random.randint(2,20)

        self.StartX = StartCell.MapX
        self.StartY = StartCell.MapY
        self.EndX = self.StartX + self.RoomX
        self.EndY = self.StartY + self.RoomY

        #populated during corridor painting
        self.ConnectedRooms = []

    def __eq__(self, other):
        return self.StartX == other.StartX and self.StartY == other.StartY

    def RandomCellAddress(self):
        rX = random.randint(self.StartX,self.EndX)
        rY = random.randint(self.StartY,self.EndY)
        return (rX,rY)

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



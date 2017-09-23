import random

class ArenaRoom(object):

    def __init__(self,StartCell):
        self.ROOM_OK             = 0;
        self.ARENA_OUT_OF_BOUNDS = 1;

        self.RoomX = random.randint(2,20)
        self.RoomY = random.randint(2,20)

        self.StartX = StartCell.MapX
        self.StartY = StartCell.MapY

    def paint(self, RawGrid):
        # do painting

        BiggestX = self.StartX + self.RoomX
        BiggestY = self.StartY + self.RoomY

        if BiggestY >= len(RawGrid) or BiggestX >= len(RawGrid[BiggestY]):
            return self.ARENA_OUT_OF_BOUNDS

        for y in range(self.StartY,self.StartY + self.RoomY):
            for x in range(self.StartX,self.StartX + self.RoomX):
                RawGrid[y][x].TileSymbol = '.'
        return self.ROOM_OK



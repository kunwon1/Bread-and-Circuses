import ArenaCell
import ArenaRoom

class ArenaMap(object):

    def __init__(self,myX=30,myY=30):

        self.ArenaX = myX
        self.ArenaY = myY

        self.RawGrid = [[ArenaCell.ArenaCell(x,y) for x in range(self.ArenaY)] for y in range(self.ArenaX)]
        
        RoomTries = 0
        RoomsMade = 0
        MaxRoomTries = 3

        while RoomTries < MaxRoomTries and RoomsMade < 1:
            RoomTries = RoomTries + 1
            r = ArenaRoom.ArenaRoom(self.RawGrid[2][2])
            ret = r.paint(self.RawGrid)
            if ret == 0:
                RoomsMade = RoomsMade + 1

    def __str__(self):
        return '\n'.join(' '.join(str(x) for x in row) for row in self.RawGrid)



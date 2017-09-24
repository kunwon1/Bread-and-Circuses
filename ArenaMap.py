import random

from ArenaCell import ArenaCell
from ArenaRoom import ArenaRoom
from ArenaCorridor import ArenaCorridor
from Exceptions import *

class ArenaMap(object):

    def __init__(self,myX=40,myY=40):

        self.ArenaX = myX
        self.ArenaY = myY

        self.RawGrid = [[ArenaCell(x,y) for x in range(self.ArenaY)] for y in range(self.ArenaX)]
       
        self.Rooms = []
        self.Corridors = []

        RoomTries = 0
        RoomsMade = 0
        MaxRoomTries = 300

        MaxCorridorTries = 300

        while RoomTries < MaxRoomTries and RoomsMade < 4:
            RoomTries = RoomTries + 1
            RootX = random.randint(1,self.ArenaX)
            RootY = random.randint(1,self.ArenaY)
            try:
                r = ArenaRoom(self.RawGrid[RootY][RootX])
            except IndexError:
                continue
            ret = r.Paint(self.RawGrid)
            if ret == 0:
                self.Rooms.append(r)
                RoomsMade = RoomsMade + 1

        for Room in self.Rooms:
            for OtherRoom in self.Rooms:
                if Room == OtherRoom:
                    continue
                if Room in OtherRoom.ConnectedRooms:
                    continue

                corA = Room.RandomCellAddress()
                corB = OtherRoom.RandomCellAddress()
                
                CorridorTries = 0
                CorridorMade = False
                while CorridorTries < MaxCorridorTries and CorridorMade == False:
                    CorridorTries = CorridorTries + 1
                    try:
                        cor = ArenaCorridor(self.RawGrid,corA,corB)
                    except CorridorException:
                        continue
                    Room.ConnectedRooms.append(OtherRoom)
                    OtherRoom.ConnectedRooms.append(Room)
                    CorridorMade = True

                    self.Corridors.append(cor)


    def __str__(self):
        return '\n'.join(' '.join(str(x) for x in row) for row in self.RawGrid)



# Copyright (c) 2017 David J Moore

import random

from pyarena.ArenaCell import ArenaCell
from pyarena.ArenaRoom import ArenaRoom
from pyarena.ArenaCorridor import ArenaCorridor
from pyarena.Exceptions import *
from pyarena.Lib.Pathfinder import Pathfinder

class ArenaMap(object):

    def __init__(self,myX=40,myY=40,roomMin=5,roomMax=15,roomLimit=5):
        
        self.EliminateRedundantCorridors = True

        self.ArenaX = myX
        self.ArenaY = myY

        self.RoomMin = roomMin
        self.RoomMax = roomMax

        self.RawGrid = [[ArenaCell(x,y) for x in range(self.ArenaY)] for y in range(self.ArenaX)]
       
        self.Rooms = []
        self.Corridors = []
        self.Entities = []

        RoomTries = 0
        RoomsMade = 0
        MaxRoomTries = 300

        MaxCorridorTries = 300

        while RoomTries < MaxRoomTries and RoomsMade < roomLimit:
            RoomTries = RoomTries + 1
            RootX = random.randint(1,self.ArenaX)
            RootY = random.randint(1,self.ArenaY)
            try:
                r = ArenaRoom(self.RawGrid[RootY][RootX],self.RoomMin,self.RoomMax)
            except IndexError:
                continue
            ret = r.Paint(self.RawGrid)
            if ret == 0:
                self.Rooms.append(r)
                RoomsMade = RoomsMade + 1


        for Room in self.Rooms:
            if self.AllRoomsConnected():
                break
            for OtherRoom in self.Rooms:
                if Room == OtherRoom:
                    continue

                if self.AllRoomsConnected():
                    break

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
                    CorridorMade = True

                    self.Corridors.append(cor)


    def __str__(self):
        TempGrid = []
        for Y in self.RawGrid:
            TempSubGrid = []
            for X in Y:
                TempSubGrid.append(str(X.TileSymbol))
            TempGrid.append(TempSubGrid)
            
        for e in self.Entities:
            TempGrid[e.MapY][e.MapX] = e.GetGlyph()
        return '\n'.join(' '.join(str(x) for x in row) for row in TempGrid)

    def AllRoomsConnected(self):
        for Room in self.Rooms:
            for OtherRoom in self.Rooms:
                if Room == OtherRoom:
                    continue
                finder = Pathfinder(self.RawGrid)
                if not finder.RoomIsConnected(Room,OtherRoom):
                    #print('ALL Returning false')
                    return False
        #print('ALL Returning True')
        return True

    def HasEntities(self):
        if not self.Entities:
            return False
        else:
            return True






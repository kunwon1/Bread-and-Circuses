# Copyright (c) 2017 David J Moore

import ArenaMap
from lib import Pathfinder

TestFinder = False

# map x, map y, room min dimensional size, room max dimensional size, max number of rooms
a = ArenaMap.ArenaMap(50,50,5,15,12)
#a = ArenaMap.ArenaMap(20,35)
if TestFinder:
    finder = Pathfinder.Pathfinder(a.RawGrid,debug=True)
    Start = a.Rooms[0].RandomCellAddress()
    End = a.Rooms[1].RandomCellAddress()
    print(a)
    try:
        finder.path(Start[0],Start[1],End[0],End[1])
    except:
        pass
print(a)

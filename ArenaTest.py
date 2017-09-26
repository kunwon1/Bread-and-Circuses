import ArenaMap
from lib import Pathfinder

TestFinder = True

a = ArenaMap.ArenaMap(50,50)
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

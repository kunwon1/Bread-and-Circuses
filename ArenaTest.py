import ArenaMap
from lib import Pathfinder

a = ArenaMap.ArenaMap(30,30)
finder = Pathfinder.Pathfinder(a.RawGrid,debug=True)
Start = a.Rooms[0].RandomCellAddress()
End = a.Rooms[1].RandomCellAddress()
print(a)
finder.path(Start[0],Start[1],End[0],End[1])
print(a)

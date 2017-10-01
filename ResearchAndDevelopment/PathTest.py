# Copyright (c) 2017 David J Moore

#!/usr/bin/env python

import time
import random

from pyarena.ArenaMap import ArenaMap 
from pyarena.ArenaListener import ArenaListener
from pyarena.Lib.Pathfinder import Pathfinder
from pyarena.Components import *
from pyarena.Entities import *

AL = ArenaListener()
def main():
    a = ArenaMap(30,30,4,12,5)
    
    P = PlayerEntity.PlayerEntity()
    RandomCell = random.choice(a.Rooms).RandomCellAddress()
    P.SetMapPositionWithTuple(RandomCell)
    a.Entities.append(P)

    G = GladiatorEntity.GladiatorEntity()
    RandomCell2 = random.choice(a.Rooms).RandomCellAddress()
    while RandomCell2 == RandomCell:
        RandomCell2 = random.choice(a.Rooms).RandomCellAddress()
    G.SetMapPositionWithTuple(RandomCell2)
    a.Entities.append(G)

    finder = Pathfinder(a.RawGrid,True)
    try:
        finder.path(P.MapX,P.MapY,G.MapX,G.MapY)
    except (PathNotFoundException,PathfinderException) as e:
        pass
    print(a)

main()

























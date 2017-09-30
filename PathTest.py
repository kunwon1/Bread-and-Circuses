# Copyright (c) 2017 David J Moore

#!/usr/bin/env python

import time
import random

import ArenaMap
import ArenaListener

from lib import Pathfinder

from Components import *
from Entities import *
AL = ArenaListener.ArenaListener()
def main():
    a = ArenaMap.ArenaMap(30,30,4,12,5)
    
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

    finder = Pathfinder.Pathfinder(a.RawGrid,True)
    try:
        finder.path(P.MapX,P.MapY,G.MapX,G.MapY)
    except (PathNotFoundException,PathfinderException) as e:
        pass
    print(a)

main()

























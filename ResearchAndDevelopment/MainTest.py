# Copyright (c) 2017 David J Moore

#!/usr/bin/env python

import os
import sys
import time
import curses
import random
from curses import wrapper

from pyarena.ArenaMap import ArenaMap
from pyarena.Entities import *
from pyarena.ArenaTimer import ArenaTimer
from pyarena.Components import *
from pyarena.ArenaListener import ArenaListener
from pyarena.Lib.Pathfinder import Pathfinder

MapWindow = None
InfoWindow = None
StatusWindow = None

AL = ArenaListener()

def DrawWindows(stdscr):
    global MapWindow,StatusWindow,InfoWindow
    MapWindow = stdscr.subwin(curses.LINES - 1,
                              int(curses.COLS / 3 * 2),
                              0, 0)
    InfoWindow = stdscr.subwin(int(curses.LINES / 2 - 1),
                               54, 0,
                               int(curses.COLS / 3 * 2 + 1))
    StatusWindow = stdscr.subwin(int(curses.LINES / 2),
                                 54,
                                 int(curses.LINES / 2),
                                 int(curses.COLS / 3 * 2 + 1))

    AllWindows = (MapWindow, InfoWindow, StatusWindow)
    return AllWindows

def main(stdscr):
    stdscr.clear()
    curses.noecho()

    begin_x = 0
    begin_y = 0

    AllWindows = DrawWindows(stdscr)
    
    for w in AllWindows:
        w.box()

    MapWindow.addstr(0,2,"Map")
    InfoWindow.addstr(0,2,"Info")
    StatusWindow.addstr(0,2,"Status")

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

    for e in a.Entities:
        e._AIComponent = DumbAIComponent.DumbAIComponent(a.RawGrid)

    finder = Pathfinder(a.RawGrid,True)
    try:
        finder.path(P.MapX,P.MapY,G.MapX,G.MapY)
    except (PathNotFoundException,PathfinderException) as e:
        pass

    i = 1
    for line in iter(str(a).splitlines()):
        MapWindow.addstr(i, 2, line)
        i += 1
    MapWindow.addstr(i+1,2,"Turn 1")

    stdscr.refresh()
    
    #keep this right before the while loop
    AT = ArenaTimer()
    while 1:
        c = stdscr.getch()
        if c == ord('q'):
            break
        else:
            AT.Step()
            i = 1
            for line in iter(str(a).splitlines()):
                MapWindow.addstr(i, 2, line)
                i += 1
            MapWindow.addstr(i+1,2,"Turn %s" % str(AT.TotalSteps))
            MapWindow.refresh()


#    time.sleep(5)

    curses.endwin()

wrapper(main)

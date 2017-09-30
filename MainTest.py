#!/usr/bin/env python

import curses
import curses.textpad
from curses import wrapper
import time
import ArenaMap

MapWindow = None
InfoWindow = None
StatusWindow = None

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

    MapWindow.addstr(0,0,"Map")
    InfoWindow.addstr(0,0,"Info")
    StatusWindow.addstr(0,0,"Status")

    a = ArenaMap.ArenaMap(30,30,4,12,5)

    i = 2
    for line in iter(str(a).splitlines()):
        MapWindow.addstr(i, 2, line)
        i += 1


    stdscr.refresh()

    while 1:
        c = stdscr.getch()
        if c == ord('q'):
            break
        else:
            a = ArenaMap.ArenaMap(30,30,4,12,5)
            i = 2
            for line in iter(str(a).splitlines()):
                MapWindow.addstr(i, 2, line)
                i += 1

            MapWindow.refresh()


#    time.sleep(5)

    curses.endwin()

wrapper(main)

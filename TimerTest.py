# Copyright (c) 2017 David J Moore

from ArenaTimer import ArenaTimer

T = ArenaTimer()
i = 0

while 1:
    print('Loop %s !' % i)
    i += 1
    T.Step()


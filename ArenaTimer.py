# Copyright (c) 2017 David J Moore

import time

from pyarena.Config import Conf

class ArenaTimer(object):

    def __init__(self):
        self.Interval = Conf['ArenaTimer']['TurnInterval']
        self.LastTime = time.clock()
        self.TotalSteps = 1

    def Step(self):
        self.TotalSteps += 1
        cur = time.clock()
        elapsed = cur - self.LastTime
        remain = self.Interval - elapsed
        if remain > 0:
            self.LastTime = time.clock()
            time.sleep(remain)
            return
        else:
            self.LastTime = time.clock()
            return

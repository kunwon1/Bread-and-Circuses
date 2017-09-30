# Copyright (c) 2017 David J Moore

import time

class ArenaTimer(object):

    def __init__(self):
        self.Interval = 1.0
        self.LastTime = time.clock()

    def Step(self):
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

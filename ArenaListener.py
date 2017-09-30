# Copyright (c) 2017 David J Moore

import queue
import logging
from logging.handlers import QueueHandler

class ArenaListener(object):
    
    def __init__(self):
        self.Q = queue.Queue()

        self.Handler = QueueHandler(self.Q)

        l = logging.getLogger('ArenaListener')
        l.addHandler(self.Handler)
        l.setLevel(logging.DEBUG)

    def Pop(self):
        if self.Q.empty():
            return None
        else:
            try:
                return self.Q.get(False)
            except queue.Queue.Empty:
                return None

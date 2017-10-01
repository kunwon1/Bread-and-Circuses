# Copyright (c) 2017 David J Moore

import queue
import logging
from logging.handlers import QueueHandler

from pyarena.Config import Conf

class ArenaListener(object):
    
    def __init__(self):
        self.Q = queue.Queue()

        self.Handler = QueueHandler(self.Q)

        l = logging.getLogger(Conf['ArenaListener']['LoggerName'])
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

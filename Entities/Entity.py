# Copyright (c) 2017 David J Moore

import persistent

class Entity(persistent.Persistent):

    def __init__(self):
        self._RenderComponent = None
        self._StatsComponent = None
        self._AIComponent = None
        self._PlayerComponent = None

    def HasRenderComponent(self):
        return self._RenderComponent is not None

    def HasStatsComponent(self):
        return self._StatsComponent is not None

    def HasAIComponent(self):
        return self._AIComponent is not None

    def HasPlayerComponent(self):
        return self._PlayerComponent is not None



# Copyright (c) 2017 David J Moore

import persistent

class Entity(persistent.Persistent):

    def __init__(self):
        self._RenderComponent = None
        self._StatsComponent = None
        self._AIComponent = None
        self._PlayerComponent = None
        self._FactionComponent = None
        self._WeaponComponent = None
        self.MapX = 0
        self.MapY = 0
        self.Glyph = None

    def HasRenderComponent(self):
        return self._RenderComponent is not None

    def HasStatsComponent(self):
        return self._StatsComponent is not None

    def HasAIComponent(self):
        return self._AIComponent is not None

    def HasPlayerComponent(self):
        return self._PlayerComponent is not None

    def HasFactionComponent(self):
        return self._FactionComponent is not None

    def HasWeaponComponent(self):
        return self._WeaponComponent is not None

    def GetMapPositionTuple(self):
        return (self.MapX,self.MapY)

    def SetMapPositionWithTuple(self,tup):
        self.MapX = tup[0]
        self.MapY = tup[1]


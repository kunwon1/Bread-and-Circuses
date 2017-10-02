# Copyright (c) 2017 David J Moore

import random

from pyarena.Components.AIComponent import AIComponent
from pyarena.Lib.Pathfinder import Pathfinder,Neighbors

class DumbAIComponent(AIComponent):

    def __init__(self,MapGrid):
        self.Target = None
        self.MyLoc = None
        self.TargetLoc = None
        self.MapGrid = MapGrid

    def Step(self,Myself,Target):
        self.Target = Target
        self.Myself = Myself
        self.MyLoc = Myself.GetMapPositionTuple()
        self.TargetLoc = Target.GetMapPositionTuple()

        finder = Pathfinder(self.MapGrid)
        DMap = finder.DijkstraMap(self.TargetLoc[0],self.TargetLoc[1])
        best = [self.MyLoc]
        for N in Neighbors(self.MyLoc,self.MapGrid,True):
            if N == self.TargetLoc:
                if self.Myself.HasStatsComponent() \
                 & self.Myself.HasWeaponComponent():
                     self.TryToAttack(Myself,Target)
                     break
            if DMap[N] < DMap[best[0]]:
                best = [N]
            elif DMap[N] == DMap[best[0]]:
                best.append(N)
        L = random.choice(best)
        self.Myself.SetMapPositionWithTuple(L)

    def TryToAttack(self,Myself,Target):
        Stats = Myself._StatsComponent
        Weap = Myself._WeaponComponent

        EStats = Target._StatsComponent
        EWeap = Target._WeaponComponent

        # 10? ticks per game turn

        # actions make someone busy for X ticks

        # you can act again when you're not busy
        # as long as you still have stamina

        # if there's a tie, use initiative to break
        #

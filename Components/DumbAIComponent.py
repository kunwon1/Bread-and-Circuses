# Copyright (c) 2017 David J Moore

from pyarena.Components.AIComponent import AIComponent
from pyarena.Lib.Pathfinder import Pathfinder

class DumbAIComponent(AIComponent):

    def __init__(self,MapGrid):
        self.Target = None
        self.MyLoc = None
        self.TargetLoc = None

    def Step(self,Myself,Target):
        self.Target = Target
        self.Myself = Myself
        self.MyLoc = Myself.GetMapPositionTuple()
        self.TargetLoc = Target.GetMapPositionTuple()



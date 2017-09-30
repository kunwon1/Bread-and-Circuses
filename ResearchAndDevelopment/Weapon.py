import random
import persistent
from Materials import *

class Weapon(persistent.Persistent):

    def __init__(self):
        self.Material = None
        self.WeapType = None
        self.BaseSpeed = 0



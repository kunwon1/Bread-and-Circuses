# Copyright (c) 2017 David J Moore

from . import Entity

from pyarena.Config import Conf

class GladiatorEntity(Entity.Entity):

    def __init__(self):
        super(GladiatorEntity,self).__init__()
        self.Glyph = Conf['Entities']['GladiatorEntity']['Glyph']


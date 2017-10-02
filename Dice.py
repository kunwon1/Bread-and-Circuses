# Copyright (c) 2017 David J Moore

import random

def RollDice(diestring='1d20'):
    tot,sides = diestring.split('d')
    return Roll(int(tot),int(sides))

def Roll(TotalDice=1,DieSides=20):
    i = 0
    tot = 0
    while i < TotalDice:
        tot += random.randint(1,DieSides)
        i += 1
    return tot




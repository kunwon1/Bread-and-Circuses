# Copyright (c) 2017 David J Moore

from pyarena.Dice import RollDice
import pyarena.Components.Component as Component

class StatsComponent(Component.Component):

    def __init__(self):
        self.HP = RollDice('6d6')
        self.STAMINA = RollDice('8d3')

        self.SPD = RollDice('6d4')
        self.BRU = RollDice('6d4')
        self.POW = RollDice('6d4')
        self.TWI = RollDice('6d4')
        self.RES = RollDice('6d4')
        self.DIS = RollDice('6d4')
        self.WIT = RollDice('6d4')
        self.REC = RollDice('6d4')

        self.Intimidation = self.BRU + self.DIS
        self.Evasion = self.SPD + self.TWI
        self.Blocking = self.RES + self.POW
        self.Treatment = self.WIT + self.REC
        self.Initiative = self.SPD + self.DIS
        self.Counter = self.TWI + self.WIT
        self.Fury = self.BRU + self.POW
        self.Respite = self.RES + self.REC

    def __str__(self):
        L = ''

        L += 'HP:'.ljust(13) + str(self.HP) + "\n"
        L += 'STAM:'.ljust(13) + str(self.STAMINA) + "\n"
        L += 'Speed:'.ljust(13) + str(self.SPD) + "\n"
        L += 'Brutality:'.ljust(13) + str(self.BRU) + "\n"
        L += 'Power:'.ljust(13) + str(self.POW) + "\n"
        L += 'Twitch:'.ljust(13) + str(self.TWI) + "\n"
        L += 'Resistance:'.ljust(13) + str(self.RES) + "\n"
        L += 'Discipline:'.ljust(13) + str(self.DIS) + "\n"
        L += 'Wits:'.ljust(13) + str(self.WIT) + "\n"
        L += 'Recovery:'.ljust(13) + str(self.REC) 
       
        return L

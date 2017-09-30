import persistent

class PlayerStats(persistent.Persistent):

    def __init__(self):
        self.SPD = 20
        self.BRU = 20
        self.POW = 20
        self.TWI = 20
        self.RES = 20
        self.DIS = 20
        self.WIT = 20
        self.REC = 20

        self.Intimidation = self.BRU + self.DIS
        self.Evasion = self.SPD + self.TWI
        self.Blocking = self.RES + self.POW
        self.Treatment = self.WIT + self.REC
        self.Initiative = self.SPD + self.DIS
        self.Counter = self.TWI + self.WIT
        self.Fury = self.BRU + self.POW
        self.Respite = self.RES + self.REC

import persistent
import PlayerStats

class Player(persistent.Persistent):

    def __init__(self):
        self.Stats = PlayerStats.PlayerStats()

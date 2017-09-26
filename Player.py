import persistent
import PlayerStats

class Player(persistent.Persistent):

    def __init__(self):
        self.Stats = PlayerStats.PlayerStats()

        self.STATE_SEARCHING = 1
        self.STATE_CLOSING   = 2
        self.STATE_WANDERING = 3
        self.STATE_ATTACKING = 4


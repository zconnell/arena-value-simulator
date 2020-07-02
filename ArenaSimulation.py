# Create ArenaSimulation Class - Simulations are a series of events played with a given game win %
class ArenaSimulation:
    def __init__(self,ID,winPercent,startingGems,simEvent):
        self.ID = ID
        self.winPercent = winPercent
        self.startingGems = startingGems
        self.simEvent = simEvent
        self.gemHistory = []
        self.packHistory = []
        self.maxEvents = 500
    def runSim(self):
        gemBalance = self.startingGems
        packBalance = 0
        self.gemHistory = []
        self.packHistory = []
        ii = 0
        while ii < self.maxEvents:
            gemBalance -= self.simEvent.cost
            if gemBalance < 0:
                break
            matchWins = self.simEvent.play_event(self.winPercent)
            gemBalance += self.simEvent.prize["gems"][matchWins]
            packBalance += self.simEvent.prize["packs"][matchWins]
            ii += 1
            self.gemHistory.append(gemBalance)
            self.packHistory.append(packBalance)

import random
import numpy
import json

class Event:
    def __init__(self,name,maxMatchWins,maxMatchLosses,maxMatches,gamesToPlay,prize,cost):
        self.name = name
        self.maxMatchWins = maxMatchWins
        self.maxMatchLosses = maxMatchLosses
        self.maxMatches = maxMatches
        self.gamesToPlay = gamesToPlay
        self.prize = prize
        self.cost = cost
    def play_event(self, winPercent):
        matchWins = 0
        matchesPlayed = 0
        while matchWins < self.maxMatchWins and \
            (matchesPlayed - matchWins) < self.maxMatchLosses and \
            matchesPlayed < self.maxMatches:
                matchWins += self.play_match(winPercent)
                matchesPlayed += 1
        return matchWins
    def play_match(self, winPercent):
        gameWins = 0
        gamesPlayed = 0
        while gamesPlayed < self.gamesToPlay:
            gameWins += self.play_game(winPercent)
            gamesPlayed += 1
        if gameWins >= self.gamesToPlay / 2:
            return 1
        else:
            return 0
    def play_game(self, winPercent):
        result = random.uniform(0,1)
        if result <= winPercent:
            return 1
        else:
            return 0

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

prizeBO1 = {"gems":[50, 100, 250, 1000, 1400, 1600, 1800, 2200],
             "packs":[1,1,2,2,3,4,5,6]}
eventBO1 = Event("B01",7,3,10,1,prizeBO1,1500)

prizeBO3 = {"gems":[0,0,1000,3000],
             "packs":[1,1,4,6]}
eventBO3 = Event("B03",3,3,3,3,prizeBO3,1500)
eventTypes = [eventBO1,eventBO3]

ID = 0
simulations = {}
for thisEvent in eventTypes:
    for winPercent in numpy.arange(0.4,0.8,0.01):
        startingGems = 20000
        thisSim = ArenaSimulation(str(ID),winPercent,startingGems,thisEvent)
        for ii in range(100):
            thisSim.ID = str(ID) + "-" + str(ii)
            thisSim.runSim()
            simulations[thisSim.ID] = {
                "ID": thisSim.ID,
                "event name":thisSim.simEvent.name,
                "win percent": thisSim.winPercent,
                "starting gems": thisSim.startingGems,
                "events played": len(thisSim.gemHistory),
                "gem history": thisSim.gemHistory,
                "packs won": thisSim.packHistory[-1],
                "pack history": thisSim.packHistory
                }
        ID += 1

json.dump(simulations,open("simulations.json","w"))

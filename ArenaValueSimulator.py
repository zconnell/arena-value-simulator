from ArenaEvent import ArenaEvent
from ArenaSimulation import ArenaSimulation
import numpy
import json

# Create the Best of 1 (BO1) and Best of 3 (BO3) events
prizeBO1 = {"gems":[50, 100, 250, 1000, 1400, 1600, 1800, 2200],
             "packs":[1,1,2,2,3,4,5,6]}
BO1 = ArenaEvent("BO1",7,3,10,1,prizeBO1,1500)
prizeBO3 = {"gems":[0,0,1000,3000],
             "packs":[1,1,4,6]}
BO3 = ArenaEvent("BO3",3,3,3,3,prizeBO3,1500)

# All events to be simulated to be included in the "events" list
events = [BO1,BO3]

# Initialize values for the simulation
simulations = {} # simulations dictionary collects all simulations performed
startingGems = 20000 # Change value to change the number of gems for all starting simulations
simsPerWinPercent = 250 # Change value to change the number of sims performed for each win Percentage
minWinPercent = 0.4 # Change value to change the minimum win percentage simulated
maxWinPercent = 0.75 # Change value to change the maximum win percentage simulated
stepWinPercent = 0.005 # Change value to change the step between win percentages

for thisEvent in events:
    for winPercent in numpy.arange(minWinPercent,maxWinPercent,stepWinPercent):
        ID = thisEvent.name + "-" + str(winPercent)
        thisSim = ArenaSimulation(str(ID),winPercent,startingGems,thisEvent)
        for ii in range(simsPerWinPercent):
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

outfile = "simulations.json" # Change value to change the JSON output file name

json.dump(simulations,open(outfile,"w"))

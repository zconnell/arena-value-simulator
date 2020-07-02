from ArenaEvent import ArenaEvent
from ArenaSimulation import ArenaSimulation
import numpy
import json

prizeBO1 = {"gems":[50, 100, 250, 1000, 1400, 1600, 1800, 2200],
             "packs":[1,1,2,2,3,4,5,6]}
eventBO1 = ArenaEvent("B01",7,3,10,1,prizeBO1,1500)

prizeBO3 = {"gems":[0,0,1000,3000],
             "packs":[1,1,4,6]}
eventBO3 = ArenaEvent("B03",3,3,3,3,prizeBO3,1500)
eventTypes = [eventBO1,eventBO3]

ID = 0
simulations = {}
for thisEvent in eventTypes:
    for winPercent in numpy.arange(0.4,0.8,0.01):
        startingGems = 20000
        thisSim = ArenaSimulation(str(ID),winPercent,startingGems,thisEvent)
        for ii in range(10):
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

json.dump(simulations,open("simulations1.json","w"))

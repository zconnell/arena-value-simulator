import json
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy

inputFileName = 'simulations.json'

with open(inputFileName, 'r') as file:
    simulations = json.load(file)

eventPlotStyles = {'BO1':'.r', 'BO3':'.b'}

winP = {}
for ID in simulations:
    thisSim = simulations[ID]
    winPercent = thisSim['win percent']
    eventName = thisSim['event name']
    if not eventName in winP.keys():
        winP[eventName] = {}
    if not winPercent in winP[eventName]:
        winP[eventName][winPercent] = []
    winP[eventName][winPercent].append(thisSim['events played'])

fig,ax = plt.subplots()

for eventName in winP:
    plotStyle = eventPlotStyles[eventName]
    xAxes = []
    yValues = []
    for winPercent in winP[eventName]:
        eventsPlayed = winP[eventName][winPercent]
        xAxes.append(winPercent)
        eventsPlayedMean = numpy.mean(eventsPlayed)
        yValues.append(eventsPlayedMean)
    ax.plot(xAxes,yValues,plotStyle, label=eventName)

ax.set_title('Going infinite on Magic Arena:\nEvents Played vs. Game Win Percentage')
ax.set_xlabel('Game Win Percentage')
ax.set_ylabel('# Events Played')
ax.set_xlim([0.4,0.75])
ax.set_ylim([0,500])
ax.xaxis.set_major_locator(mtick.MultipleLocator(0.05))
ax.xaxis.set_minor_locator(mtick.MultipleLocator(0.01))
ax.tick_params(which='both',direction='in')
ax.xaxis.set_major_formatter(mtick.PercentFormatter(decimals=2))
ax.yaxis.set_major_locator(mtick.MultipleLocator(50))
ax.yaxis.set_minor_locator(mtick.MultipleLocator(12.5))
ax.legend(loc='upper left')
ax.grid(axis='both',which='major',color='k')
ax.grid(axis='both',which='minor',color='0.5')
fig.show()

# arena-value-simulator
A simple simulation of Magic Arena draft events so players can evaluate their best option.
At present time (2020.07.01), Magic Arena contains two primary limited event types:
1. Best-of-1 (BO1): Players play single games until they reach either 7 wins or 3 losses.
2. Best-of-3 (BO3): Players play matches that are best 2-out-of-3 games. Players play 3 matches regardless of record.
Both events cost 1500 Gems to enter, but prize payouts are very different.

# Conclusions
Below 55% game win percent, BO1 allows players to play slightly more events than Bo3 on average before running out of gems.
Above 55% game win percent, BO3 allows players to play more events on average. Players will also "go infinite" at lower game win percentages.

# Important considerations
This model is very simplified -it assumes that players have a fixed game win rate across all games.
This does not take into account the different ways that BO1 and BO3 pair players.
According to WotC's December 2018 state-of-the-beta, BO1 is paired using Event Record, Player Rank, and Player MMR whereas BO3 is paired using only Event Record.
The likely result is that BO1 win rates are suppressed on average compared to BO3 (as players win more, they gain higher rank and MMR and are paired against better opponents).
From a pure value perspective, this makes BO3 more appealing for higher skilled players.

# Files currently included:
1. ArenaValueSimulator.py - Python program to simulate playing events in Magic Arena.
2. ArenaEvent.py - Defines the ArenaEvent class (An Arena Event is a series of matches played. A match is a series of games.)
3. ArenaSimulation.py - Defines the ArenaSimulation class (An Arena Simulation is a series of Events played that results in gems and packs.)
4. simulations.json - A sample output file of the ArenaValueSimulator (note: Actual output file from the ArenaValueSimulator is larger than GitHub 25MB limit).
5. EventsGraphMaker - Makes the Average Events Played vs. Game Win % Graph from the sample file.
6. Events Played vs. Game Win Percentage - Image file of a graph made with the EventsGraphMaker program. Image made using 20,000 starting gems and 250 sims per win percent.

# If you want to run these simulations yourself:
1. Save ArenaEvent, ArenaSimulation, and ArenaValueSimulator to the same directory.
2. Run ArenaValueSimulator. This will create a JSON output file in the directory where ArenaSimulation is saved.
3. Run the EventsGraphMaker. This will create a graph of Events Played vs. Game Win % based on the simulation file created by ArenaValueSimulator.

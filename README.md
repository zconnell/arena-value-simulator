# arena-value-simulator
A simple simulation of Magic Arena draft events so players can evaluate their best option.
At present time (2020.07.01), Magic Arena contains two primary limited event types:
  Best-of-1 (BO1): Players play single games until they reach either 7 wins or 3 losses.
  Best-of-3 (BO3): Players play matches that are best 2-out-of-3 games. Players play 3 matches regardless of record.
Both events cost 1500 Gems to enter, but prize payouts for these events are very different.

Files currently included:
1. ArenaValueSimulator.py - Python program to simulate playing events in Magic Arena.
2. ArenaEvent.py - Defines the ArenaEvent class (An Arena Event is a series of matches played. A match is a series of games.)
3. ArenaSimulation.py - Defines the ArenaSimulation class (An Arena Simulation is a series of Events played that results in gems and packs.)
4. simulations.json - A sample output file of the ArenaValueSimulator.

If you want to run these simulations yourself:
1. Save ArenaEvent, ArenaSimulation, and ArenaValueSimulator to the same directory.
2. Run ArenaValueSimulator. This will create a JSON output file in the directory where ArenaSimulation is saved.

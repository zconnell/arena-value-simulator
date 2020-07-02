import random

# Create Event class - Events are a series of games played with a prize associated to them
class ArenaEvent:
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

from bots.lowest import Lowest
from bots.highest import Highest
from bots.random import Random
from bots.smartest import Smartest
from bots.estimate import Estimate
from engine.player import Player
from engine.gameLoop import GameLoop
from log.logger import open_log, close_log, log
from log.save import save
import random


LOG_FILE = "logs/game_"

def generatePlayer():
    p = random.randrange(0, 5)

    if p == 0:
        return Player("Carol", Smartest())
    elif p == 1:
        return Player("Nolan", Estimate())
    elif p == 2:
        return Player("Jim", Random())
    elif p == 3:
        return Player("Kim", Highest())
    else:
        return Player("Bill", Lowest())

def generatePlayers():
    n = random.randrange(2,10)
    players = []
    for _ in range(n):
        players.append(generatePlayer())
    return players

def setUpMappy():
    mappy = {}
    mappy["Bill"] = 0
    mappy["Kim"] = 0
    mappy["Jim"] = 0
    mappy["Carol"] = 0
    mappy["Nolan"] = 0
    return mappy

def addToMappy(mappy, mappy2, mappy3, values, players):
    losers = set(range(0, len(players))) - set(values)

    for x in values:
        mappy[players[x].name] += 1

    for x in losers:
        mappy2[players[x].name] += 1

    for player in players:
        mappy3[player.name] += player.score

    save(mappy, mappy2, mappy3)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    winMappy = setUpMappy()
    loseMappy = setUpMappy()
    totalMappy = setUpMappy()
    for x in range(500):
        open_log(LOG_FILE + str(x) + ".txt")
        players = generatePlayers()
        values = GameLoop().do_game(players)
        for player in players:
            log(f"{player.name}: {player.score}")
        close_log()
        addToMappy(winMappy, loseMappy, totalMappy, values, players)


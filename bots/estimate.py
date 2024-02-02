import copy
import random

EPOCHS = 2

class Estimate:

    def randomMove(self, cards, state):
        while True:
            temp = random.randrange(1, len(105))
            if temp not in cards and temp not in state.played:
                return temp

    def choose(self, hand, state):
        tempState = copy.deepcopy(state)
        epoch = 0
        
        while epoch:
        return 0

    def choose_pile(self, state):
        minn = state.pile_total(0)
        nummy = state.piles[0][-1]
        index = 0
        for x in range(1, 4):
            tot = state.pile_total(x)
            if tot == minn and nummy < state.piles[x][-1]:
                index = x
            if tot < minn:
                minn = tot
                index = x
        return index

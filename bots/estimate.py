import copy
import random

EPOCHS = 100

class Estimate:


    def randomMove(self, cards, state):
        while True:
            temp = random.randrange(1, 105)
            if temp not in cards and temp not in state.played:
                return temp

    def simulateCard(self, card, state, hand, numPlayers):
        epoch = 0
        total = 0
        while epoch < EPOCHS:
            tempState = copy.deepcopy(state)
            tempState.played = tempState.played + hand # enemy wont play hand
            moves = [card]
            for _ in range(1, numPlayers):
                moves.append(self.randomMove(moves, state))
            moves.sort()
            index = moves.index(card)
            total += self.simulateTurn(moves, state, index)
            epoch += 1
        return total

    def simulateTurn(self, moves, state, p):

        for i, move in enumerate(moves):
            bestPile = -1
            closest = -1
            for j, pile in enumerate(state.piles):
                if pile[-1] < move:
                    if bestPile == -1 or closest > pile[-1]:
                        bestPile = j
                        closest = pile[-1]

            if bestPile == -1: # no valid pile
                if p == i:
                    return self.takeLowestPile(move, state)
                else:
                    self.takeLowestPile(move, state)
            else:
                if p == i:
                    return self.addToRow(move, bestPile, state)
                else:
                    self.addToRow(move, bestPile, state)
        return 0

    def takeLowestPile(self, move, state):
        bestPile = -1
        closest = -1
        for i, pile in enumerate(state.piles):
            if bestPile == -1 or closest > state.pile_total(i):
                bestPile = i
                closest = state.pile_total(i)
        state.piles[i] = [move]
        return closest

    def addToRow(self, move, i, state):
        if len(state.piles) >= 5:
            temp = state.pile_total(i)
            state.piles[i] = [move]
            return temp
        state.piles[i].append(move)
        return 0



    def choose(self, hand, state, numPlayers):
        estimate = []
        minIndex = 0
        minEstimate = 0
        for i, card in enumerate(hand):
            temp = self.simulateCard(card, state, hand, numPlayers)
            if temp < minEstimate:
                minIndex = i
                minEstimate = temp


        return minIndex

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

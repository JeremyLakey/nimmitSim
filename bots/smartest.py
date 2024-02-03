import random


class Smartest:
    def choose(self, hand, state, numPlayers):
        closest = 10000
        index = -1
        for i in range(len(hand)):
            card = hand[i]
            takes = 0
            closey = 100000
            for x in range(4):
                num = state.piles[x][-1]
                if card > num and card - num < closey:
                    takes = x
                    closey = card - num
            if len(state.piles[takes]) != 5:
                num = state.piles[takes][-1]
                if card - num < closest:
                    index = i
                    closest = card - num
        if index == -1:
            index = random.randrange(0, len(hand))

        return index

    def choose_pile(self, state):
        minn = state.pile_total(0)
        nummy = state.piles[0][-1]
        index = 0
        for x in range(1, 4):
            tot = state.pile_total(x)
            if tot == minn and nummy > state.piles[x][-1]:
                index = x
            if tot < minn:
                minn = tot
                index = x
        return index
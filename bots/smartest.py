


class Smartest:
    def choose(self, hand, state):
        closest = 10000
        index = len(hand) - 1
        for i in range(len(hand)):
            card = hand[i]
            for x in range(4):
                num = state.piles[x][-1]
                if card > num and card - num < closest:
                    index = i

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
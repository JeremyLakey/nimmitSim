


class Highest:
    def choose(self, hand, state):
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
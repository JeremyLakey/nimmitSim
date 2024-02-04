
class Cautious:

    def dangerLevel(self, card, state, numPlayars, hand):

        takes = -1
        closeness = 100000
        for i in range(4):
            v = state.piles[i][-1]
            if v < card and card - v < closeness:
                takes = i
                closeness = card - v

        if takes == -1:
            pile = self.choose_pile(state)
            return state.pile_total(pile)
        else:
            top = state.piles[takes][-1] + 1
            pile_length = len(state.piles[takes])
            pain = []
            while top < card:
                if (not top in state.played) and (not top in hand):
                    pain.append(self.calculate_pain(top))
                top += 1

            pain.sort(reverse=True)

            temp = 0
            total = 0
            while temp < numPlayars:
                if temp < len(pain) and pile_length + temp <= 5:
                    total += pain[temp]
                temp += 1
            return (total + state.pile_total(takes)) * (pile_length ^ -1)





    def choose(self, hand, state, numPlayers):
        best = 100000
        index = 0
        for i, card in enumerate(hand):
            v = self.dangerLevel(card, state, numPlayers, hand)
            if v < best:
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

    def calculate_pain(self, card):
        if card == 55:
            return 7
        elif len(str(card)) > 1 and str(card)[0] == str(card)[1]:
            return 5
        elif card % 10 == 0:
            return 3
        elif card % 5 == 0:
            return 2
        else:
            return 1

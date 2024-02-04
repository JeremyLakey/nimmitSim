import random

class State:
    def __init__(self):
        self.piles = [[] for i in range(4)]
        self.played = []

    def start_cards(self, deck):
        self.piles = [[] for i in range(4)]
        self.played = []
        for i in range(4):
            card = deck.draw()
            self.played.append(card)
            self.piles[i].append(card)

    def add_card(self, move):
        pile = -1
        above = 0

        self.played.append(move.card)

        for i in range(4):
            if self.piles[i][-1] < move.card and self.piles[i][-1] > above:
                pile = i
                above = self.piles[i][-1]

        if pile == -1:
            return True

        if len(self.piles[pile]) >= 5:
            move.player.score -= self.pile_total(pile)
            self.piles[pile] = []
            self.piles[pile].append(move.card)
        else:
            self.piles[pile].append(move.card)

        return False

    def take_pile(self, player, i, card):
        total = self.pile_total(i)
        player.score -= total
        self.piles[i] = [card]

    def pile_total(self, i):
        total = 0
        for x in range(len(self.piles[i])):
            total += calculate_bulls(self.piles[i][x])
        return total

    def to_string(self):
        s = ""
        for x in range(4):
            s += self.print_row(x)
        return s

    def print_row(self, x):
        i = 0
        s = ""
        while i < 6:
            if i < len(self.piles[x]):
                s += f"{self.piles[x][i]} "
            else:
                s += "[] "
            i += 1
        return s + "\n"


def calculate_bulls(card):
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
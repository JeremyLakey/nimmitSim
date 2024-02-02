import random


class Deck:
    def __init__(self):
        self.cards = []
        self.setup()

    def draw(self):
        return self.cards.pop()

    def setup(self):
        self.cards = [i for i in range(1, 105)]
        random.shuffle(self.cards)

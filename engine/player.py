

SCORE_BASE = 66


class Player:

    def __init__(self, name, bot):
        self.name = name
        self.bot = bot
        self.score = SCORE_BASE
        self.hand = []

    def is_alive(self):
        return self.score > 0

    def give_hand(self, deck):
        hand = []
        for x in range(10):
            hand.append(deck.draw())
        hand.sort()
        self.hand = hand

    def play_card(self, state, numPlayers):
        i = self.bot.choose(self.hand, state, numPlayers)
        return self.hand.pop(i)

    def to_string(self):
        return f"{self.name}\nscore:{self.score}"

    def to_string_hand(self):
        s = ""
        for card in self.hand:
            s += f"{str(card)}\n"
        return self.to_string() + "\n"



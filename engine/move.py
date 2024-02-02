

class Move:
    def __init__(self, player, card):
        self.player = player
        self.card = card

    def __lt__(self, other):
        return self.card < other.card

    def to_string(self):
        return f"{self.player.name} plays {self.card}"
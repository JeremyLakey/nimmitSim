from engine.deck import Deck
from engine.move import Move
from engine.moveList import MoveList
from engine.state import State

class GameLoop:
    def __init__(self):
        self.state = State()

    def do_game(self, players):

        while self.is_done(players):
            self.do_round(players)

        return self.select_winners(players)

    def select_winners(self, players):
        maxx = players[0].score
        index = [0]

        for i in range(1, len(players)):
            player = players[i]
            if player.score == max:
                index.append(i)
            if player.score > maxx:
                index = [i]
                maxx = player.score

        return index

    def is_done(self, players):
        for player in players:
            if not player.is_alive():
                return False
        return True


    def do_round(self, players):
        deck = Deck()
        self.num_players = len(players)

        for player in players:
            player.give_hand(deck)

        self.state.start_cards(deck)

        for _ in range(10):
            moves = MoveList()

            for player in players:
                moves.addMove(Move(player, player.play_card(self.state)))

            moves.playMoves(self.state)

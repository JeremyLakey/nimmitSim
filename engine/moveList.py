from log.logger import log


class MoveList:

    def __init__(self):
        self.moves = []

    def addMove(self, move):
        self.moves.append(move)

    def playMoves(self, state):
        self.moves.sort()
        log(state.to_string())
        for move in self.moves:
            log(move.to_string())
            choose_pile = state.add_card(move)
            if choose_pile:
                state.take_pile(move.player, move.player.bot.choose_pile(state), move.card)

            log("Played : " + str(state.played))
            log(state.to_string())
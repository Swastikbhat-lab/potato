"""Chess board utilities using python-chess."""

import chess

class Board:
    """Wrapper around ``chess.Board`` with helper methods."""

    def __init__(self):
        self.board = chess.Board()

    def reset(self):
        self.board.reset()

    def push(self, move):
        self.board.push(move)

    def legal_moves(self):
        return list(self.board.legal_moves)

    def is_game_over(self):
        return self.board.is_game_over()

    def result(self):
        return self.board.result()

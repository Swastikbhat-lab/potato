"""Main game loop."""

import sys
import pyglet
import chess
from pyglet.window import key

from .board import Board
from .ai import LearningAI
from .view import ChessView


def run():
    board = Board()
    ai = LearningAI()
    view = ChessView()
    moves_san = []

    @view.event
    def on_draw():
        view.clear()
        view.setup_3d()
        view.draw_board()

    @view.event
    def on_key_press(symbol, modifiers):
        if symbol == key.ESCAPE:
            pyglet.app.exit()

    def ai_move():
        if board.is_game_over():
            return
        move = ai.choose_move(board.board)
        board.push(move)
        moves_san.append(board.board.san(move))
        if board.is_game_over():
            ai.record_result(moves_san, board.result())

    def on_user_move(move: chess.Move):
        board.push(move)
        moves_san.append(board.board.san(move))
        ai_move()

    # TODO: user move selection via mouse - simplified placeholder
    def update(dt):
        pass

    pyglet.clock.schedule_interval(update, 1/60)
    pyglet.app.run()

if __name__ == "__main__":
    run()

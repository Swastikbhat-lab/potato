
"""Simplified console based game loop."""

from __future__ import annotations

from typing import List

from .board import Board, Move
from .ai import LearningAI


def parse_move(text: str) -> Move:
    """Convert ``"x1 y1 z1 x2 y2 z2"`` into a move tuple."""
    parts = text.strip().split()
    if len(parts) != 6:
        raise ValueError("Move must have six numbers")
    nums = list(map(int, parts))
    return (nums[0], nums[1], nums[2]), (nums[3], nums[4], nums[5])


def run() -> None:
    board = Board()
    ai = LearningAI()
    moves: List[str] = []
    turn = "white"

    while not board.is_game_over():
        print(board)
        if turn == "white":
            try:
                raw = input("Your move (x1 y1 z1 x2 y2 z2 or 'quit'): ")
            except EOFError:
                break
            if raw.lower().strip() == "quit":
                print("Game aborted")
                return
            try:
                move = parse_move(raw)
            except Exception as exc:
                print(f"Invalid move: {exc}")
                continue
            if move not in board.legal_moves(turn):
                print("Illegal move")
                continue
            board.move_piece(*move)
            moves.append(board.move_to_str(move))
        else:
            move = ai.choose_move(board, turn)
            board.move_piece(*move)
            print(f"AI moves {board.move_to_str(move)}")
            moves.append(board.move_to_str(move))

        turn = "black" if turn == "white" else "white"

    print(board)
    result = board.result()
    ai.record_result(moves, result)
    print("Game over:", result)


if __name__ == "__main__":
    run()

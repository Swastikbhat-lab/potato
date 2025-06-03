"""Very simple adaptive chess AI."""

import json
import os
import random
from typing import Dict

import chess

MEMORY_FILE = "ai_memory.json"

class LearningAI:
    """Naive AI that adjusts move choices based on past results."""

    def __init__(self):
        self.stats: Dict[str, int] = {}
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as fh:
                self.stats = json.load(fh)

    def choose_move(self, board: chess.Board) -> chess.Move:
        moves = list(board.legal_moves)
        if not moves:
            raise ValueError("No legal moves")

        best_score = None
        best_move = None
        for move in moves:
            key = board.san(move)
            score = self.stats.get(key, 0)
            if best_score is None or score > best_score:
                best_score = score
                best_move = move
        if best_move is None:
            best_move = random.choice(moves)
        return best_move

    def record_result(self, moves: [str], result: str):
        """Update stats after a game."""
        factor = 1 if result == "1-0" else -1 if result == "0-1" else 0
        for san in moves:
            self.stats[san] = self.stats.get(san, 0) + factor
        with open(MEMORY_FILE, "w", encoding="utf-8") as fh:
            json.dump(self.stats, fh)

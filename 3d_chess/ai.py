"""Very simple adaptive chess AI for the minimal 3D board."""

from __future__ import annotations

import json
import os
import random
from typing import Dict, List

from .board import Board, Move

MEMORY_FILE = "ai_memory.json"

class LearningAI:
    """Naive AI that adjusts move choices based on past results."""

    def __init__(self) -> None:
        self.stats: Dict[str, int] = {}
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r", encoding="utf-8") as fh:
                self.stats = json.load(fh)

    def choose_move(self, board: Board, color: str) -> Move:
        moves = board.legal_moves(color)
        if not moves:
            raise ValueError("No legal moves")

        best_score = None
        best_move = None
        for move in moves:
            key = board.move_to_str(move)
            score = self.stats.get(key, 0)
            if best_score is None or score > best_score:
                best_score = score
                best_move = move
        if best_move is None:
            best_move = random.choice(moves)
        return best_move

    def record_result(self, moves: List[str], result: str) -> None:
        """Update stats after a game."""
        factor = 1 if result == "1-0" else -1 if result == "0-1" else 0
        for m in moves:
            self.stats[m] = self.stats.get(m, 0) + factor
        with open(MEMORY_FILE, "w", encoding="utf-8") as fh:
            json.dump(self.stats, fh)

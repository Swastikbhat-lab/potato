"""Extremely small self contained 3D chess board implementation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


BOARD_SIZE = 4  # keep the board tiny so it is manageable


@dataclass
class Piece:
    kind: str  # "K" or "P" for this demo
    color: str  # "white" or "black"


Coord = Tuple[int, int, int]
Move = Tuple[Coord, Coord]


class Board:
    """Minimal 3D chess board used for the demo game."""

    def __init__(self) -> None:
        self.board: Dict[Coord, Piece] = {}
        self.reset()

    # --------------------------------------------------------------
    # setup / utility helpers
    # --------------------------------------------------------------
    def reset(self) -> None:
        self.board.clear()
        # white pieces on z=0
        self.board[(1, 0, 0)] = Piece("K", "white")
        self.board[(0, 1, 0)] = Piece("P", "white")
        self.board[(2, 1, 0)] = Piece("P", "white")

        # black pieces mirrored on z=3
        self.board[(2, BOARD_SIZE - 1, BOARD_SIZE - 1)] = Piece("K", "black")
        self.board[(1, BOARD_SIZE - 2, BOARD_SIZE - 1)] = Piece("P", "black")
        self.board[(3, BOARD_SIZE - 2, BOARD_SIZE - 1)] = Piece("P", "black")

    # --------------------------------------------------------------
    def piece_at(self, c: Coord) -> Optional[Piece]:
        return self.board.get(c)

    def move_piece(self, from_c: Coord, to_c: Coord) -> None:
        piece = self.board.pop(from_c)
        captured = self.board.get(to_c)
        if captured:
            del self.board[to_c]
        self.board[to_c] = piece

    # --------------------------------------------------------------
    # move generation
    # --------------------------------------------------------------
    def legal_moves(self, color: str) -> List[Move]:
        moves: List[Move] = []
        for coord, piece in list(self.board.items()):
            if piece.color != color:
                continue
            if piece.kind == "K":
                moves.extend(self._king_moves(coord))
            elif piece.kind == "P":
                moves.extend(self._pawn_moves(coord, color))
        return moves

    def _inside(self, c: Coord) -> bool:
        x, y, z = c
        return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and 0 <= z < BOARD_SIZE

    def _king_moves(self, coord: Coord) -> List[Move]:
        moves: List[Move] = []
        x0, y0, z0 = coord
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    if dx == dy == dz == 0:
                        continue
                    dest = (x0 + dx, y0 + dy, z0 + dz)
                    if not self._inside(dest):
                        continue
                    piece = self.piece_at(dest)
                    if piece is None or piece.color != self.piece_at(coord).color:
                        moves.append((coord, dest))
        return moves

    def _pawn_moves(self, coord: Coord, color: str) -> List[Move]:
        moves: List[Move] = []
        x, y, z = coord
        dir_y = 1 if color == "white" else -1
        forward = (x, y + dir_y, z)
        if self._inside(forward) and self.piece_at(forward) is None:
            moves.append((coord, forward))

        for dx in (-1, 1):
            capture = (x + dx, y + dir_y, z)
            if not self._inside(capture):
                continue
            piece = self.piece_at(capture)
            if piece is not None and piece.color != color:
                moves.append((coord, capture))
        # allow climbing up or down one level
        for dz in (-1, 1):
            step = (x, y + dir_y, z + dz)
            if self._inside(step) and self.piece_at(step) is None:
                moves.append((coord, step))
        return moves

    # --------------------------------------------------------------
    def is_game_over(self) -> bool:
        return not self._has_king("white") or not self._has_king("black")

    def _has_king(self, color: str) -> bool:
        for p in self.board.values():
            if p.kind == "K" and p.color == color:
                return True
        return False

    def result(self) -> str:
        if self._has_king("white") and not self._has_king("black"):
            return "1-0"
        if self._has_king("black") and not self._has_king("white"):
            return "0-1"
        return "1/2-1/2"

    # --------------------------------------------------------------
    def move_to_str(self, move: Move) -> str:
        (x1, y1, z1), (x2, y2, z2) = move
        return f"{x1}{y1}{z1}-{x2}{y2}{z2}"

    def __str__(self) -> str:
        lines = []
        for z in range(BOARD_SIZE - 1, -1, -1):
            lines.append(f"Layer {z}:")
            for y in range(BOARD_SIZE - 1, -1, -1):
                row = []
                for x in range(BOARD_SIZE):
                    piece = self.piece_at((x, y, z))
                    row.append(piece.kind.lower() if piece and piece.color == "black" else (piece.kind if piece else "."))
                lines.append(" ".join(row))
            lines.append("")
        return "\n".join(lines)


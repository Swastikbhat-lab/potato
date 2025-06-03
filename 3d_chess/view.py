"""Minimal 3D board display using pyglet."""

import math
from typing import Tuple

import pyglet
from pyglet.gl import (
    glEnable, GL_DEPTH_TEST, glClearColor,
    gluPerspective, glMatrixMode, GL_PROJECTION,
    glLoadIdentity, glTranslatef, glRotatef, GL_MODELVIEW,
)


class ChessView(pyglet.window.Window):
    def __init__(self, board_size: int = 8, square_size: float = 1.0):
        super().__init__(800, 600, "3D Chess")
        self.board_size = board_size
        self.square_size = square_size
        self.rotation = 30
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.5, 0.7, 0.9, 1)

    def on_draw(self):
        self.clear()
        self.setup_3d()
        self.draw_board()

    def setup_3d(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(65.0, self.width / float(self.height), 0.1, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslatef(0, -5, -20)
        glRotatef(self.rotation, 1, 0, 0)

    def draw_board(self):
        for x in range(self.board_size):
            for y in range(self.board_size):
                self.draw_square(x, y)

    def draw_square(self, x: int, y: int):
        from pyglet.gl import glBegin, glEnd, glVertex3f, glColor3f, GL_QUADS
        glBegin(GL_QUADS)
        color = (x + y) % 2
        glColor3f(0.9, 0.9, 0.9) if color else glColor3f(0.2, 0.2, 0.2)
        size = self.square_size
        glVertex3f(x * size, 0, y * size)
        glVertex3f((x + 1) * size, 0, y * size)
        glVertex3f((x + 1) * size, 0, (y + 1) * size)
        glVertex3f(x * size, 0, (y + 1) * size)
        glEnd()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.rotation += dy * 0.3

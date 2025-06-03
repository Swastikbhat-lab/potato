# 3D Chess with Learning AI

This project contains a minimal Python implementation of a 3D chess game with an
AI opponent that learns from previous games. The visuals are rendered using
`pyglet` and the chess logic is powered by `python-chess`.

**Note:** This is a simplified example and does not represent a complete chess
engine or sophisticated machine learning. The AI records game results and
adjusts move selection based on past experience.

## Requirements

Install dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Running the Game

Execute the game from the repository root:

```bash
python -m 3d_chess.game
```

The game window displays a basic 3D board. Use your mouse to select and move
pieces. The AI will make a move after each of yours.

Saved game data is stored in `ai_memory.json`. Deleting this file resets the AI
learning state.

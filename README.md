# 3D Chess with Learning AI

This project contains a tiny Python implementation of a 3D‑inspired chess
variant with an AI opponent that learns from previous games.  It avoids any
external dependencies so it can run in restricted environments.

**Note:** This is a simplified example and does not represent a complete chess
engine or sophisticated machine learning. The AI records game results and
adjusts move selection based on past experience.

## Requirements

The game only requires the Python standard library.  No additional packages are
needed.

## Running the Game

Execute the game from the repository root:

```bash
python -m 3d_chess.game
```

The program prints the board layer by layer in the console.  Enter moves as six
space separated numbers representing the source and destination coordinates
``x1 y1 z1 x2 y2 z2``.  The AI will answer with its own move.

Saved game data is stored in `ai_memory.json`. Deleting this file resets the AI
learning state.

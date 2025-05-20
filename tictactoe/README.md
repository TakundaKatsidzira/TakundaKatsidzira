TicTacToe
Game optimized for performance, where the computer plays itself using random choices (no strategy). Logs include: who played first, was it a draw, who won, did the first player win, first move position, full move sequence, number of moves, and win method (e.g., row_1, diag_anti) saved to a CSV file. Develop multiple computer agents with different strategies. Backtracking can be used to simulate future game states and evaluate optimal moves (e.g., using minimax). Dynamic programming can cache board evaluations to avoid redundant computation during simulations.
# TicTacToe Project

## Overview

This project implements an optimized, command-line TicTacToe game framework where multiple computer agents can play against each other. It supports logging detailed game statistics to CSV for analysis. The code follows clean Object-Oriented principles, is optimized for time and space complexity, and is extensively tested.

---

## Design and Implementation Details

### Problem Modeling

- **Board**: Represented as a flat list of 9 positions indexed 0 to 8, representing a 3x3 grid.
- **Players**: Two players, ‘X’ and ‘O’, alternate moves.
- **Game State**: Tracks current player, board state, winner, draw status, and move history.
- **Win Detection**: Checks 8 fixed winning combinations (3 rows, 3 columns, 2 diagonals).

### Agents (Players)

- **RandomAgent**: Chooses moves randomly from available positions.
- **MinimaxAgent**: Uses the Minimax algorithm with memoization (dynamic programming) to evaluate the best possible move, ensuring optimal play.

### Algorithms and Optimizations

- **Minimax with Memoization**:
  - Recursively simulates possible game states to evaluate moves.
  - Memoizes board states to avoid redundant computations, improving time complexity.
- **Win Detection**: Constant-time check over predefined winning combos after each move.
- **Data Structures**:
  - Board as a list for O(1) access.
  - Move history stored as a list.
  - Memoization cache as a dictionary keyed by `(board_string, player)`.

### Logging

Games are logged to CSV, including:

- Timestamp
- Who played first
- Winner or draw status
- First move position
- Full move sequence
- Number of moves
- Win method (row, column, or diagonal)

---

## Code Structure

tictactoe/
├── src/
│ └── tictactoe.py # Core game logic and agent implementations
├── tests/
│ └── test_tictactoe.py # Unit tests for game logic and agents
├── scripts/
│ └── play_tictactoe.py # Command-line script to simulate games and log results
├── data/
│ └── game_logs.csv # CSV log of simulated games
├── README.md # This file
├── setup.py # Installation setup (optional)
└── requirements.txt # Dependencies (if any)

This implementation demonstrates:

Efficient game logic

Clear OOP design

Strategic AI agents

Optimized algorithms using dynamic programming

Comprehensive logging and testing

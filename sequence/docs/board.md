# Board Module

The `Board` class represents the Sequence game board.

- Board size is 10x10.
- Tokens are placed on the grid.
- Supports checking for sequences of length 5 using dynamic programming.
- Implements backtracking to simulate token placements.

Main methods:

- `place_token(row, col, player_id)`: Place player's token at position.
- `check_sequence_from(row, col)`: Checks if the last move forms a winning sequence.
- `find_all_sequences(player_id)`: Finds all sequences for the player on the board.

This class is central to the game logic.

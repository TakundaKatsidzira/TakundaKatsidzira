# src/tictactoe.py

import random  # Imports Python's built-in random module for generating random numbers.
# Study: Python standard library, random module (random.choice, random.shuffle, etc.)

from typing import List, Optional, Tuple, Dict  # Imports type hints for better code clarity and static analysis.
# Study: Python type hints, typing module, static typing in Python.

class TicTacToe:
    """
    Class representing the TicTacToe game board and logic.
    Study: Object-Oriented Programming (OOP) - classes, methods, attributes, encapsulation.

    Board positions indexed 0-8 (3x3 grid):
     0 | 1 | 2
    -----------
     3 | 4 | 5
    -----------
     6 | 7 | 8

    State representation:
    - board: List[str] with 'X', 'O', or ' ' (empty)
    - current_player: 'X' or 'O'
    """

    WINNING_COMBINATIONS = [
        (0, 1, 2),  # rows
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),  # columns
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # diagonals
        (2, 4, 6),
    ]
    # Class variable: all possible winning line combinations (rows, columns, diagonals).
    # Study: Lists, tuples, class variables, combinatorics.

    def __init__(self, starting_player: str = 'X'):
        # Constructor: initializes a new game.
        assert starting_player in ('X', 'O')  # Defensive programming: only allow valid players.
        self.board: List[str] = [' '] * 9  # 3x3 board as a flat list, all empty.
        self.current_player: str = starting_player  # Whose turn it is.
        self.winner: Optional[str] = None  # Winner ('X', 'O', or None).
        self.move_history: List[int] = []  # List of moves made (positions).
        self.is_draw: bool = False  # True if game ended in a draw.
        self.win_method: Optional[str] = None  # How the game was won (row/col/diag).
        # Study: __init__ method, instance variables, type annotations, assertions.

    def reset(self, starting_player: str = 'X'):
        self.__init__(starting_player)
        # Resets the board and state for a new game.
        # Study: Method calls, re-initialization.

    def make_move(self, position: int) -> bool:
        """Attempt to place current_player's mark at position."""
        if self.board[position] == ' ' and self.winner is None:
            # Only allow move if cell is empty and game not over.
            self.board[position] = self.current_player  # Place mark.
            self.move_history.append(position)  # Record move.
            self.check_winner()  # Check if this move wins the game.
            if not self.winner:
                if self.is_board_full():
                    self.is_draw = True  # If board full and no winner, it's a draw.
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
                    # Switch player using a conditional expression (ternary operator).
            return True  # Move was successful.
        return False  # Invalid move.
        # Study: Conditionals, boolean logic, list indexing, method calls, return values.

    def is_board_full(self) -> bool:
        return all(space != ' ' for space in self.board)
        # Returns True if no empty spaces left.
        # Study: all() function, generator expressions, list iteration.

    def check_winner(self):
        for idx, combo in enumerate(self.WINNING_COMBINATIONS):
            a, b, c = combo
            if (
                self.board[a] == self.board[b] == self.board[c] != ' '
            ):
                self.winner = self.board[a]  # Set winner to 'X' or 'O'.
                self.win_method = self._win_method_name(idx)  # Store how the win happened.
                return
        self.winner = None  # No winner found.
        # Study: for loops, tuple unpacking, equality checks, early return, method calls.

    def _win_method_name(self, idx: int) -> str:
        # Helper to convert a win combo index to a human-readable string.
        row_names = ['row_1', 'row_2', 'row_3']
        col_names = ['col_1', 'col_2', 'col_3']
        diag_names = ['diag_main', 'diag_anti']
        if idx <= 2:
            return row_names[idx]
        elif 3 <= idx <= 5:
            return col_names[idx - 3]
        else:
            return diag_names[idx - 6]
        # Study: Helper methods, list indexing, if-elif-else, return values.

    def available_moves(self) -> List[int]:
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # Returns a list of indices for empty spots.
        # Study: List comprehensions, enumerate(), filtering.

    def game_over(self) -> bool:
        return self.winner is not None or self.is_draw
        # Returns True if game is won or drawn.
        # Study: Boolean logic, or operator.

    def __str__(self) -> str:
        # Returns a string representation of the board for printing.
        rows = [
            f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} "
            for i in range(0, 9, 3)
        ]
        return "\n-----------\n".join(rows)
        # Study: Special methods (__str__), string formatting (f-strings), list slicing, join().

class Agent:
    """Base class for TicTacToe agents."""
    # Study: Inheritance, base classes, abstract methods.

    def __init__(self, symbol: str):
        assert symbol in ('X', 'O')
        self.symbol = symbol  # The agent's mark.

    def select_move(self, game: TicTacToe) -> int:
        raise NotImplementedError()
        # To be implemented by subclasses.
        # Study: Abstract methods, exceptions.

class RandomAgent(Agent):
    """Agent that picks a random available move."""
    # Study: Inheritance, subclassing, method overriding.

    def select_move(self, game: TicTacToe) -> int:
        moves = game.available_moves()  # Get all possible moves.
        return random.choice(moves)  # Pick one at random.
        # Study: Method overriding, using superclass methods, random.choice().

class MinimaxAgent(Agent):
    """
    Minimax agent with memoization (dynamic programming) and randomized tie-breaking.
    Study: Minimax algorithm (game theory), recursion, memoization, dynamic programming, AI.
    """

    def __init__(self, symbol: str):
        super().__init__(symbol)
        self.memo: Dict[Tuple[str, str], int] = {}
        # Memoization dictionary for board state and player.
        # Study: Dictionaries, tuples as keys, type hints.

    def select_move(self, game: TicTacToe) -> int:
        best_score = float('-inf')
        best_moves = []
        for move in game.available_moves():
            game.board[move] = self.symbol  # Try move.
            score = self._minimax(game, self._opponent(self.symbol), False)
            game.board[move] = ' '  # Undo move.
            if score > best_score:
                best_score = score
                best_moves = [move]
            elif score == best_score:
                best_moves.append(move)
        return random.choice(best_moves)  # Randomly break ties.
        # Study: Minimax search, recursion, backtracking, tie-breaking, for loops, if-else logic.

    def _minimax(self, game: TicTacToe, player: str, is_maximizing: bool) -> int:
        board_key = ''.join(game.board)  # Serialize board for memoization.
        memo_key = (board_key, player)
        if memo_key in self.memo:
            return self.memo[memo_key]  # Return cached result.

        winner = self._check_winner_static(game.board)
        if winner == self.symbol:
            return 1  # Win for this agent.
        elif winner == self._opponent(self.symbol):
            return -1  # Loss for this agent.
        elif ' ' not in game.board:
            return 0  # Draw.

        if is_maximizing:
            best_score = float('-inf')
            for i in game.available_moves():
                game.board[i] = player
                score = self._minimax(game, self._opponent(player), False)
                game.board[i] = ' '
                best_score = max(best_score, score)
        else:
            best_score = float('inf')
            for i in game.available_moves():
                game.board[i] = player
                score = self._minimax(game, self._opponent(player), True)
                game.board[i] = ' '
                best_score = min(best_score, score)

        self.memo[memo_key] = best_score  # Cache result.
        return best_score
        # Study: Recursion, backtracking, memoization, maximizing/minimizing logic, algorithm design.

    def _check_winner_static(self, board: List[str]) -> Optional[str]:
        # Static method to check winner for a given board (doesn't modify game state).
        for combo in TicTacToe.WINNING_COMBINATIONS:
            a, b, c = combo
            if board[a] == board[b] == board[c] != ' ':
                return board[a]
        return None
        # Study: Static analysis, win detection, for loops, tuple unpacking.

    def _opponent(self, player: str) -> str:
        # Returns the opposite player symbol.
        return 'O' if player == 'X' else 'X'
        # Study: Helper methods, conditional expressions (ternary operator).

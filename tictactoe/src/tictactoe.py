# src/tictactoe.py
import random
from typing import List, Optional, Tuple, Dict

class TicTacToe:
    """
    TicTacToe game board and logic.
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
        (0, 3, 6),  # cols
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),  # diagonals
        (2, 4, 6),
    ]

    def __init__(self, starting_player: str = 'X'):
        assert starting_player in ('X', 'O')
        self.board: List[str] = [' '] * 9
        self.current_player: str = starting_player
        self.winner: Optional[str] = None
        self.move_history: List[int] = []
        self.is_draw: bool = False
        self.win_method: Optional[str] = None

    def reset(self, starting_player: str = 'X'):
        self.__init__(starting_player)

    def make_move(self, position: int) -> bool:
        """Attempt to place current_player's mark at position."""
        if self.board[position] == ' ' and self.winner is None:
            self.board[position] = self.current_player
            self.move_history.append(position)
            self.check_winner()
            if not self.winner:
                if self.is_board_full():
                    self.is_draw = True
                else:
                    self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def is_board_full(self) -> bool:
        return all(space != ' ' for space in self.board)

    def check_winner(self):
        for idx, combo in enumerate(self.WINNING_COMBINATIONS):
            a, b, c = combo
            if (
                self.board[a] == self.board[b] == self.board[c] != ' '
            ):
                self.winner = self.board[a]
                self.win_method = self._win_method_name(idx)
                return
        self.winner = None

    def _win_method_name(self, idx: int) -> str:
        row_names = ['row_1', 'row_2', 'row_3']
        col_names = ['col_1', 'col_2', 'col_3']
        diag_names = ['diag_main', 'diag_anti']
        if idx <= 2:
            return row_names[idx]
        elif 3 <= idx <= 5:
            return col_names[idx - 3]
        else:
            return diag_names[idx - 6]

    def available_moves(self) -> List[int]:
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def game_over(self) -> bool:
        return self.winner is not None or self.is_draw

    def __str__(self) -> str:
        rows = [
            f" {self.board[i]} | {self.board[i+1]} | {self.board[i+2]} "
            for i in range(0, 9, 3)
        ]
        return "\n-----------\n".join(rows)

class Agent:
    """Base class for TicTacToe agents."""

    def __init__(self, symbol: str):
        assert symbol in ('X', 'O')
        self.symbol = symbol

    def select_move(self, game: TicTacToe) -> int:
        raise NotImplementedError()

class RandomAgent(Agent):
    """Agent that picks a random available move."""

    def select_move(self, game: TicTacToe) -> int:
        moves = game.available_moves()
        return random.choice(moves)

class MinimaxAgent(Agent):
    """
    Minimax agent with memoization (dynamic programming) and randomized tie-breaking.
    """

    def __init__(self, symbol: str):
        super().__init__(symbol)
        self.memo: Dict[Tuple[str, str], int] = {}

    def select_move(self, game: TicTacToe) -> int:
        best_score = float('-inf')
        best_moves = []
        for move in game.available_moves():
            game.board[move] = self.symbol
            score = self._minimax(game, self._opponent(self.symbol), False)
            game.board[move] = ' '
            if score > best_score:
                best_score = score
                best_moves = [move]
            elif score == best_score:
                best_moves.append(move)
        return random.choice(best_moves)

    def _minimax(self, game: TicTacToe, player: str, is_maximizing: bool) -> int:
        board_key = ''.join(game.board)
        memo_key = (board_key, player)
        if memo_key in self.memo:
            return self.memo[memo_key]

        winner = self._check_winner_static(game.board)
        if winner == self.symbol:
            return 1
        elif winner == self._opponent(self.symbol):
            return -1
        elif ' ' not in game.board:
            return 0

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

        self.memo[memo_key] = best_score
        return best_score

    def _check_winner_static(self, board: List[str]) -> Optional[str]:
        for combo in TicTacToe.WINNING_COMBINATIONS:
            a, b, c = combo
            if board[a] == board[b] == board[c] != ' ':
                return board[a]
        return None

    def _opponent(self, player: str) -> str:
        return 'O' if player == 'X' else 'X'

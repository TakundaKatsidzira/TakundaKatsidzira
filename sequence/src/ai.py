# src/ai.py
import random
# Imports Python's built-in random module for random selection (used for tie-breaking).
# Study: Python standard library, random.choice.

from player import Player
from board import Board
# Imports Player and Board classes from your modules.
# Study: Python import system, OOP class usage.

class AIPlayer(Player):
    # Defines an AIPlayer class, inheriting from Player.
    # Study: OOP inheritance, subclassing, polymorphism.

    def __init__(self, name, token, deck, max_depth=3):
        super().__init__(name, token, deck)
        # Calls the parent Player's constructor to initialize name, token, and hand.
        self.max_depth = max_depth
        # Sets the maximum search depth for the minimax algorithm.
        self.opponent_token = 'O' if token == 'X' else 'X'
        # Determines the opponent's token based on this player's token.
        self.memo = {}
        # Initializes a dictionary for memoization (caching board evaluations).
        # AI concept: Memoization (Dynamic Programming) to avoid redundant calculations.

    def choose_move(self, board, card_to_positions):
        # Main method to choose the best move using minimax.
        moves = self._generate_valid_moves(board, card_to_positions)
        # Generates all valid moves for the current hand and board.
        if not moves:
            return None, None
        # If there are no valid moves, return (None, None).

        best_score = float('-inf')
        best_moves = []
        # Initialize variables to track the best score and corresponding moves.

        for card, pos in moves:
            new_board = board.copy()
            # Create a copy of the board to simulate the move.
            self._apply_move(new_board, card, pos, self.token)
            # Apply the move to the copied board.
            score = self._minimax(new_board, self.max_depth - 1, False, float('-inf'), float('inf'), card_to_positions)
            # Evaluate the move using minimax with alpha-beta pruning.
            # AI concept: Minimax algorithm with alpha-beta pruning (adversarial search).
            if score > best_score:
                best_score = score
                best_moves = [(card, pos)]
            elif score == best_score:
                best_moves.append((card, pos))
            # Track all moves that tie for the best score.

        return random.choice(best_moves)
        # Randomly select among the best moves (to break ties).
        # AI concept: Random tie-breaking to add unpredictability.

    def _generate_valid_moves(self, board, card_to_positions):
        # Generates all valid moves for the AI's current hand.
        moves = []
        for card in self.hand.cards:
            if card == 'JO':
                # One-eyed Jack: can remove any opponent token.
                for r in range(board.rows):
                    for c in range(board.cols):
                        if board.get_token(r, c) == self.opponent_token:
                            moves.append((card, (r, c)))
                # AI concept: Handling special cards (removal action).
            elif card == 'JT':
                # Two-eyed Jack: wild card, can place anywhere empty except corners.
                for r in range(board.rows):
                    for c in range(board.cols):
                        if board.is_corner((r, c)):
                            continue
                        if board.is_empty((r, c)):
                            moves.append((card, (r, c)))
                # AI concept: Handling wildcards (flexible placement).
            else:
                positions = card_to_positions.get(card, [])
                for pos in positions:
                    if board.is_empty(pos):
                        moves.append((card, pos))
                # AI concept: Move generation based on current hand and board state.
        return moves

    def _apply_move(self, board, card, pos, token):
        # Applies a move to the board (either placing or removing a token).
        if card == 'JO':
            board.remove_token(pos, self.opponent_token)
            # AI concept: Simulating opponent token removal.
        else:
            board.place_token(pos, token)
            # AI concept: Simulating token placement.

    def _minimax(self, board, depth, maximizing_player, alpha, beta, card_to_positions):
        # Recursive minimax algorithm with alpha-beta pruning.
        # AI concept: Minimax (adversarial search), alpha-beta pruning (optimization).
        if board.check_sequence(self.token):
            return 1000 + depth
            # If AI wins, return a large positive score (prefer faster wins).
        if board.check_sequence(self.opponent_token):
            return -1000 - depth
            # If opponent wins, return a large negative score (prefer slower losses).

        if depth == 0:
            return self._heuristic(board)
            # If at max depth, return heuristic evaluation.
            # AI concept: Heuristic evaluation for non-terminal states.

        board_key = self._board_to_key(board)
        if board_key in self.memo:
            return self.memo[board_key]
            # Use memoization to avoid redundant calculations.

        if maximizing_player:
            max_eval = float('-inf')
            moves = self._generate_valid_moves(board, card_to_positions)
            if not moves:
                return self._heuristic(board)
            for card, pos in moves:
                new_board = board.copy()
                self._apply_move(new_board, card, pos, self.token)
                eval = self._minimax(new_board, depth - 1, False, alpha, beta, card_to_positions)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
                # AI concept: Alpha-beta pruning (cutting off branches).
            self.memo[board_key] = max_eval
            return max_eval
        else:
            min_eval = float('inf')
            moves = self._generate_valid_moves(board, card_to_positions)
            if not moves:
                return self._heuristic(board)
            for card, pos in moves:
                new_board = board.copy()
                self._apply_move(new_board, card, pos, self.opponent_token)
                eval = self._minimax(new_board, depth - 1, True, alpha, beta, card_to_positions)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
                # AI concept: Alpha-beta pruning (cutting off branches).
            self.memo[board_key] = min_eval
            return min_eval

    def _heuristic(self, board):
        # Heuristic evaluation of the board state for non-terminal nodes.
        score = 0
        score += self._count_open_sequences(board, self.token) * 10
        score -= self._count_open_sequences(board, self.opponent_token) * 15
        return score
        # AI concept: Heuristic evaluation function (estimates board favorability).

    def _count_open_sequences(self, board, token):
        # Counts open sequences (potential lines) for a token.
        count = 0
        directions = [(0,1), (1,0), (1,1), (1,-1)]
        for r in range(board.rows):
            for c in range(board.cols):
                for dr, dc in directions:
                    seq_len = self._sequence_length(board, r, c, dr, dc, token)
                    if 2 <= seq_len < 5:
                        count += seq_len
        return count
        # AI concept: Pattern recognition, feature extraction for heuristic.

    def _sequence_length(self, board, r, c, dr, dc, token):
        # Returns the length of a sequence starting at (r, c) in direction (dr, dc).
        length = 0
        for i in range(5):
            rr = r + dr*i
            cc = c + dc*i
            if rr < 0 or rr >= board.rows or cc < 0 or cc >= board.cols:
                return length
            if board.is_corner((rr, cc)) or board.get_token(rr, cc) == token:
                length += 1
            else:
                return length
        return length
        # AI concept: Board scanning, sequence detection.

    def _board_to_key(self, board):
        # Converts the board and hand to a hashable key for memoization.
        return (
            tuple(tuple(row) for row in board.grid),
            tuple(sorted(self.hand.cards))
        )
        # AI concept: State hashing for memoization (dynamic programming).

# Example of creating a board instance with the new size
rows, cols = 10, 10
position_to_card = {}  # This should be defined based on your game logic
board = Board(rows=rows, cols=cols, position_to_card=position_to_card)
# Demonstrates how to create a Board instance for use with the AI.
# Study: Object instantiation, passing arguments, board setup.

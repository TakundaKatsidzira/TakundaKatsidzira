# agents.py

import random
from abc import ABC, abstractmethod
from copy import deepcopy

from .board import WIN_MASKS

CENTER = 4
CORNERS = [0, 2, 6, 8]
EDGES = [1, 3, 5, 7]


class Agent(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def select_move(self, board):
        pass


class RandomAgent(Agent):
    def __init__(self, name="RandomAgent"):
        super().__init__(name)

    def select_move(self, board):
        return random.choice(board.available_moves())

class RulesAgent(Agent):
    def __init__(self, name="RulesAgent"):
        super().__init__(name)

    def select_move(self, board):
        player = board.current_player
        opponent = 'O' if player == 'X' else 'X'

        # 1. Win if possible
        for move in board.available_moves():
            temp = board.copy()
            temp.make_move(move)
            if temp.check_winner() == player:
                return move

        # 2. Block opponent if they can win
        for move in board.available_moves():
            temp = board.copy()
            temp.make_move(move)
            if temp.check_winner() == opponent:
                return move

        # 3. Center
        if board.is_valid_move(CENTER):
            return CENTER

        # 4. Corner
        for move in CORNERS:
            if board.is_valid_move(move):
                return move

        # 5. Edge
        for move in EDGES:
            if board.is_valid_move(move):
                return move

        return random.choice(board.available_moves())

"""class ForkAgent(Agent):
    def __init__(self, name="ForkAgent"):
        super().__init__(name)

    def select_move(self, board):
        player = board.current_player
        opponent = 'O' if player == 'X' else 'X'

        def count_wins(mask, other_mask):
            count = 0
            for win in WIN_MASKS:
                if (win & mask) == win:
                    continue
                if (win & other_mask) == 0 and (win & mask) != 0:
                    count += 1
            return count

        best_move = None
        max_forks = 0
        for move in board.available_moves():
            temp = board.copy()
            temp.make_move(move)
            forks = count_wins(temp.get_bitmask(player), temp.get_bitmask(opponent))
            if forks >= 2:
                return move
            elif forks > max_forks:
                max_forks = forks
                best_move = move

        if best_move is not None:
            return best_move

        return RulesAgent().select_move(board)
"""
class MinimaxAgent(Agent):
    def __init__(self, name="MinimaxAgent"):
        super().__init__(name)
        self.memo = {}

    def select_move(self, board):
        player = board.current_player
        _, move = self.minimax(board, player, True, float('-inf'), float('inf'))
        return move

    def minimax(self, board, player, maximizing, alpha, beta):
        key = (board.get_state_key(), maximizing)
        if key in self.memo:
            return self.memo[key]

        winner = board.check_winner()
        if winner:
            if winner == player:
                return (1, None)
            else:
                return (-1, None)
        elif board.is_draw():
            return (0, None)

        best_score = float('-inf') if maximizing else float('inf')
        best_move = None

        for move in board.available_moves():
            board.make_move(move)
            score, _ = self.minimax(board, player, not maximizing, alpha, beta)
            board.undo_move(move)

            if maximizing:
                if score > best_score:
                    best_score = score
                    best_move = move
                alpha = max(alpha, best_score)
            else:
                if score < best_score:
                    best_score = score
                    best_move = move
                beta = min(beta, best_score)

            if beta <= alpha:
                break

        self.memo[key] = (best_score, best_move)
        return self.memo[key]


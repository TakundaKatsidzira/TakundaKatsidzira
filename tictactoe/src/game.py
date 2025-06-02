# game.py

import time
import random
from .board import Board, WIN_MASKS

class Game:
    def __init__(self, agent1, agent2, game_id):
        self.agent1 = agent1
        self.agent2 = agent2
        self.game_id = game_id
        self.board = Board()

        # Randomly assign roles
        if random.choice([True, False]):
            self.agent_X = agent1
            self.agent_O = agent2
        else:
            self.agent_X = agent2
            self.agent_O = agent1

        self.time_X = 0.0
        self.time_O = 0.0

    def run(self):
        while not self.board.is_terminal():
            current_agent = self.agent_X if self.board.current_player == 'X' else self.agent_O
            start = time.perf_counter()
            move = current_agent.select_move(self.board.copy())
            elapsed = time.perf_counter() - start

            self.board.make_move(move)

            if self.board.current_player == 'O':
                self.time_X += elapsed
            else:
                self.time_O += elapsed

        winner = self.board.check_winner()
        is_draw = winner is None
        win_method = self._get_win_method() if winner else 'None'

        return {
            "game_id": self.game_id,
            "is_draw": is_draw,
            "winner": winner if winner else 'Draw',
            "first_player": 'X' if self.agent1 == self.agent_X else 'O',
            "first_move": self.board.move_sequence[0],
            "last_move": self.board.move_sequence[-1],
            "X_move_sequence": [m for i, m in enumerate(self.board.move_sequence) if i % 2 == (0 if self.agent1 == self.agent_X else 1)],
            "O_move_sequence": [m for i, m in enumerate(self.board.move_sequence) if i % 2 == (1 if self.agent1 == self.agent_X else 0)],
            "game_move_sequence": self.board.move_sequence,
            "num_moves_X": len([p for i, p in enumerate(self.board.move_sequence) if i % 2 == (0 if self.agent1 == self.agent_X else 1)]),
            "num_moves_O": len([p for i, p in enumerate(self.board.move_sequence) if i % 2 == (1 if self.agent1 == self.agent_X else 0)]),
            "win_method": win_method,
            "agent_X_type": self.agent_X.name,
            "agent_O_type": self.agent_O.name,
            "agent_X_time": round(self.time_X, 6),
            "agent_O_time": round(self.time_O, 6),
            "game_time": round(self.time_X + self.time_O, 6)
        }

    def _get_win_method(self):
        x_mask = self.board.x_mask
        o_mask = self.board.o_mask
        for i, mask in enumerate(WIN_MASKS):

            if (x_mask & mask) == mask or (o_mask & mask) == mask:
                if i < 3:
                    return f"row{i + 1}"
                elif i < 6:
                    return f"col{i - 2}"
                else:
                    return f"diag{i - 5}"
        return 'None'

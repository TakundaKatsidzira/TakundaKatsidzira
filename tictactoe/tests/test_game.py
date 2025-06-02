import unittest
from src.agents import RandomAgent, RulesAgent, MinimaxAgent
from src.board import Board
from src.game import Game
import json


class DummyAgent:
    def __init__(self, name="DummyAgent"):
        self.name = name
    def select_move(self, board):
        return 0  # Always tries to move in position 0


class TestGameExtended(unittest.TestCase):

    def test_invalid_agent_raises(self):
        game = Game(DummyAgent(), DummyAgent(), game_id=42)
        game.board.make_move(0)  # Occupy the only move DummyAgent tries
        with self.assertRaises(ValueError):
            game.run()

    def test_reproducibility_via_move_sequence(self):
        agent1 = RulesAgent()
        agent2 = RandomAgent()
        game1 = Game(agent1, agent2, game_id=1)
        result1 = game1.run()

        replay_board = Board()
        for move in result1['game_move_sequence']:
            replay_board.make_move(move)

        winner = replay_board.check_winner()
        self.assertEqual(winner if winner else 'Draw', result1['winner'])

    def test_move_assignment_correctness(self):
        game = Game(RulesAgent("R1"), RandomAgent("R2"), game_id=2)
        result = game.run()
        moves = result['game_move_sequence']
        X_moves = result['X_move_sequence']
        O_moves = result['O_move_sequence']
        self.assertEqual(sorted(X_moves + O_moves), sorted(moves))
        self.assertEqual(len(X_moves), result['num_moves_X'])
        self.assertEqual(len(O_moves), result['num_moves_O'])

    
    def test_edge_case_full_board_start(self):
        # Pre-fill the board to simulate invalid game start
        game = Game(RandomAgent(), RandomAgent(), game_id=4)
        game.board.move_sequence = list(range(9))
        game.board.x_mask = 0b101010101
        game.board.o_mask = 0b010101010
        game.board.current_player = 'X'
        result = game.run()
        self.assertTrue(result['is_draw'])
        self.assertEqual(result['winner'], 'Draw')
        self.assertEqual(len(result['game_move_sequence']), 9)

    def test_timing_is_reasonable(self):
        game = Game(RandomAgent(), RandomAgent(), game_id=5)
        result = game.run()
        self.assertLess(result['game_time'], 1.0)  # Should be fast
        self.assertGreaterEqual(result['agent_X_time'], 0.0)
        self.assertGreaterEqual(result['agent_O_time'], 0.0)

    def test_first_and_last_move_indices(self):
        game = Game(RandomAgent(), RandomAgent(), game_id=6)
        result = game.run()
        first = result['first_move']
        last = result['last_move']
        self.assertIn(first, range(9))
        self.assertIn(last, range(9))
        self.assertEqual(first, result['game_move_sequence'][0])
        self.assertEqual(last, result['game_move_sequence'][-1])


if __name__ == '__main__':
    unittest.main()

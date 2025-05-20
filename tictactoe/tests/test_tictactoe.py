# tests/test_tictactoe.py
import unittest
from src.tictactoe import TicTacToe, RandomAgent, MinimaxAgent

class TestTicTacToe(unittest.TestCase):

    def test_initial_board_empty(self):
        game = TicTacToe()
        self.assertEqual(game.board, [' '] * 9)
        self.assertEqual(game.current_player, 'X')
        self.assertFalse(game.game_over())

    def test_make_move_and_switch_player(self):
        game = TicTacToe()
        move_made = game.make_move(0)
        self.assertTrue(move_made)
        self.assertEqual(game.board[0], 'X')
        self.assertEqual(game.current_player, 'O')

    def test_invalid_move(self):
        game = TicTacToe()
        game.make_move(0)
        move_made = game.make_move(0)  # Already occupied
        self.assertFalse(move_made)

    def test_winning_row(self):
        game = TicTacToe()
        moves = [0, 3, 1, 4, 2]  # X wins row_1
        for m in moves:
            game.make_move(m)
        self.assertTrue(game.game_over())
        self.assertEqual(game.winner, 'X')
        self.assertEqual(game.win_method, 'row_1')

    def test_draw(self):
        game = TicTacToe()
        moves = [0,1,2,4,3,5,7,6,8]  # Fill board with no winner
        for m in moves:
            game.make_move(m)
        self.assertTrue(game.game_over())
        self.assertTrue(game.is_draw)
        self.assertIsNone(game.winner)

    def test_random_agent_move(self):
        game = TicTacToe()
        agent = RandomAgent('X')
        move = agent.select_move(game)
        self.assertIn(move, range(9))
        self.assertIn(move, game.available_moves())

    def test_minimax_agent_blocks_win(self):
        game = TicTacToe()
        # Board state:
        # X | O | X
        # O | X |  
        #   |   | O
        #
        # O to move, must block X at pos 7 or lose
        game.board = ['X', 'O', 'X',
                      'O', 'X', ' ',
                      ' ', ' ', 'O']
        game.current_player = 'O'
        agent = MinimaxAgent('O')
        move = agent.select_move(game)
        # Best move is position 7 to block
        self.assertEqual(move, 7)

    def test_minimax_agent_wins_if_possible(self):
        game = TicTacToe()
        # Board state:
        # X | X |  
        # O | O |  
        #   |   |  
        #
        # X to move, can win at pos 2
        game.board = ['X', 'X', ' ',
                      'O', 'O', ' ',
                      ' ', ' ', ' ']
        game.current_player = 'X'
        agent = MinimaxAgent('X')
        move = agent.select_move(game)
        self.assertEqual(move, 2)

if __name__ == '__main__':
    unittest.main()

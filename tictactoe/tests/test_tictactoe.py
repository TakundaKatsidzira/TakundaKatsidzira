# tests/test_tictactoe.py
import unittest
# Imports Python's built-in unit testing framework.
# Study: Python standard library, unittest documentation, test-driven development.

from src.tictactoe import TicTacToe, RandomAgent, MinimaxAgent
# Imports your game logic and agent classes from your project.
# Study: Python import system, modules, packages, OOP (classes and inheritance).

class TestTicTacToe(unittest.TestCase):
    # Defines a test case class for TicTacToe, inheriting from unittest.TestCase.
    # Study: Python classes, inheritance, and unittest.TestCase usage.

    def test_initial_board_empty(self):
        game = TicTacToe()  # Creates a new game instance.
        self.assertEqual(game.board, [' '] * 9)  # Checks that the board is empty.
        self.assertEqual(game.current_player, 'X')  # Checks that X starts.
        self.assertFalse(game.game_over())  # Checks that the game is not over.
        # Study: Object instantiation, assert methods in unittest, list multiplication.

    def test_make_move_and_switch_player(self):
        game = TicTacToe()
        move_made = game.make_move(0)  # X moves at position 0.
        self.assertTrue(move_made)  # Checks that the move was successful.
        self.assertEqual(game.board[0], 'X')  # Checks that the board updated.
        self.assertEqual(game.current_player, 'O')  # Checks that the player switched.
        # Study: Method calls, return values, state changes, list indexing.

    def test_invalid_move(self):
        game = TicTacToe()
        game.make_move(0)  # X moves at position 0.
        move_made = game.make_move(0)  # Try to move again at the same spot.
        self.assertFalse(move_made)  # Checks that the move was rejected.
        # Study: Boolean logic, error handling, method return values.

    def test_winning_row(self):
        game = TicTacToe()
        moves = [0, 3, 1, 4, 2]  # X wins row_1 with these moves.
        for m in moves:
            game.make_move(m)  # Play each move in sequence.
        self.assertTrue(game.game_over())  # Checks that the game is over.
        self.assertEqual(game.winner, 'X')  # Checks that X is the winner.
        self.assertEqual(game.win_method, 'row_1')  # Checks the win method.
        # Study: Loops, game logic, win detection, list iteration.

    def test_draw(self):
        game = TicTacToe()
        moves = [0,1,2,4,3,5,7,6,8]  # Fill board with no winner.
        for m in moves:
            game.make_move(m)
        self.assertTrue(game.game_over())  # Checks that the game is over.
        self.assertTrue(game.is_draw)  # Checks that it's a draw.
        self.assertIsNone(game.winner)  # Checks that there is no winner.
        # Study: List operations, draw logic, assertTrue/assertIsNone.

    def test_random_agent_move(self):
        game = TicTacToe()
        agent = RandomAgent('X')  # Create a random agent for X.
        move = agent.select_move(game)  # Agent picks a move.
        self.assertIn(move, range(9))  # Checks that move is on the board.
        self.assertIn(move, game.available_moves())  # Checks that move is available.
        # Study: Randomness, agent pattern, assertIn, method overriding.

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
        # Tests if the minimax agent takes a winning move.
        # Study: Minimax, AI, board state manipulation, assertEqual.

    def test_o_can_win(self):
        # Test that O can win the game
        game = TicTacToe()
        moves = [0, 1, 2, 4, 3, 7]  # O wins by filling column 2
        for m in moves:
            game.make_move(m)
        self.assertTrue(game.game_over())
        self.assertEqual(game.winner, 'O')
        # Study: Alternate win scenarios, game logic for both players.

    def test_cannot_move_after_game_over(self):
        # Test that no moves can be made after the game is over
        game = TicTacToe()
        moves = [0, 3, 1, 4, 2]  # X wins
        for m in moves:
            game.make_move(m)
        move_made = game.make_move(5)
        self.assertFalse(move_made)
        self.assertEqual(game.winner, 'X')
        # Study: Game state, enforcing rules after game over.

    def test_invalid_move_out_of_range(self):
        # Test that moves out of range are not allowed
        game = TicTacToe()
        with self.assertRaises(IndexError):
            game.make_move(9)  # Board is 0-8
        # Study: Exception handling, with statement, assertRaises.

    def test_win_on_diagonal(self):
        # Test win on main diagonal
        game = TicTacToe()
        moves = [0, 1, 4, 2, 8]  # X wins on main diagonal
        for m in moves:
            game.make_move(m)
        self.assertTrue(game.game_over())
        self.assertEqual(game.winner, 'X')
        self.assertEqual(game.win_method, 'diag_main')
        # Study: Diagonal win detection, board indexing.

    def test_win_on_anti_diagonal(self):
        # Test win on anti-diagonal
        game = TicTacToe()
        moves = [2, 0, 4, 1, 6]  # X wins on anti-diagonal
        for m in moves:
            game.make_move(m)
        self.assertTrue(game.game_over())
        self.assertEqual(game.winner, 'X')
        self.assertEqual(game.win_method, 'diag_anti')
        # Study: Anti-diagonal win detection, board indexing.

    def test_minimax_agent_blocks_win(self):
        # Test that minimax agent blocks opponent's win
        game = TicTacToe()
        game.board = ['X', 'O', 'X',
                      'O', 'X', ' ',
                      ' ', ' ', 'O']
        game.current_player = 'O'
        agent = MinimaxAgent('O')
        move = agent.select_move(game)
        self.assertEqual(move, 7)  # Must block X at position 7
        # Study: Minimax algorithm, AI defense, board state manipulation.

    def test_minimax_agent_draw(self):
        # Test that minimax agent can force a draw if no win is possible
        game = TicTacToe()
        # Board state: only one move left, both players can't win
        game.board = ['X', 'O', 'X',
                      'X', 'O', 'O',
                      'O', 'X', ' ']
        game.current_player = 'X'
        agent = MinimaxAgent('X')
        move = agent.select_move(game)
        self.assertEqual(move, 8)
        game.make_move(move)
        self.assertTrue(game.is_draw)
        # Study: Minimax algorithm, AI decision making, test-driven development, board state manipulation.

if __name__ == '__main__':
    unittest.main()
    # Standard Python idiom: runs all tests in this file if executed directly.
    # Study: Script entry points, __name__ variable, unittest discovery.

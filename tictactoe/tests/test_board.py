import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def test_initial_state(self):
        board = Board()
        self.assertEqual(board.x_mask, 0)
        self.assertEqual(board.o_mask, 0)
        self.assertEqual(board.current_player, 'X')
        self.assertEqual(board.move_sequence, [])
        self.assertEqual(board.available_moves(), list(range(9)))

    def test_make_move_and_switch_player(self):
        board = Board()
        board.make_move(0)
        self.assertEqual(board.x_mask, 1 << 0)
        self.assertEqual(board.current_player, 'O')
        self.assertIn(0, board.move_sequence)

        board.make_move(1)
        self.assertEqual(board.o_mask, 1 << 1)
        self.assertEqual(board.current_player, 'X')
        self.assertIn(1, board.move_sequence)

    def test_invalid_move_raises(self):
        board = Board()
        board.make_move(0)
        with self.assertRaises(ValueError):
            board.make_move(0)

    def test_undo_move(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        board.undo_move(1)
        board.undo_move(0)
        self.assertEqual(board.x_mask, 0)
        self.assertEqual(board.o_mask, 0)
        self.assertEqual(board.current_player, 'X')
        self.assertEqual(board.move_sequence, [])

    def test_check_winner_x_row1(self):
        board = Board()
        board.make_move(0)
        board.make_move(3)
        board.make_move(1)
        board.make_move(4)
        board.make_move(2)
        self.assertEqual(board.check_winner(), 'X')

    def test_check_winner_o_diag(self):
        board = Board()
        board.make_move(1)  # X
        board.make_move(0)  # O
        board.make_move(2)  # X
        board.make_move(4)  # O
        board.make_move(3)  # X
        board.make_move(8)  # O (wins with diag)
        self.assertEqual(board.check_winner(), 'O')

    def test_draw(self):
        board = Board()
        for move in [0, 1, 2, 4, 3, 5, 7, 6, 8]:  # Draw pattern
            board.make_move(move)
        self.assertTrue(board.is_draw())
        self.assertIsNone(board.check_winner())
        self.assertTrue(board.is_terminal())

    def test_copy_board(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        new_board = board.copy()
        self.assertEqual(new_board.x_mask, board.x_mask)
        self.assertEqual(new_board.o_mask, board.o_mask)
        self.assertEqual(new_board.move_sequence, board.move_sequence)
        self.assertEqual(new_board.current_player, board.current_player)
        # Ensure it's a deep copy
        new_board.make_move(2)
        self.assertNotEqual(new_board.move_sequence, board.move_sequence)

    def test_get_state_key(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        key = board.get_state_key()
        self.assertIsInstance(key, tuple)
        self.assertEqual(key, (1 << 0, 1 << 1, True))  # X played 0, O played 1, X’s turn

if __name__ == "__main__":
    unittest.main()

import pytest
# Imports the pytest library for writing and running tests.
# Study: Pytest basics, test discovery, assertion rewriting, exception testing.

from src.board import Board
# Imports the Board class from your board module.
# Study: Python import system, module structure, OOP class usage.

def test_board_setup():
    board = Board()
    # Instantiates a new Board object.
    assert len(board.grid) == 10
    # Asserts that the board has 10 rows.
    assert len(board.grid[0]) == 10
    # Asserts that each row has 10 columns.
    # Study: Object instantiation, attribute access, list length, assertions.

def test_place_and_check_token():
    board = Board()
    pos = (0, 1)
    board.place_token(pos, "X")
    # Places an "X" token at position (0, 1).
    assert board.grid[0][1] == "X"
    # Checks that the token was placed correctly.
    # Study: Method calls, tuple unpacking, list indexing.

def test_invalid_placement():
    board = Board()
    pos = (0, 1)
    board.place_token(pos, "X")
    with pytest.raises(ValueError):
        board.place_token(pos, "O")
    # Tries to place a token on an already occupied spot, expects a ValueError.
    # Study: Exception handling in tests, context managers, defensive programming.

def test_place_and_remove_token():
    board = Board()
    pos = (1, 1)
    board.place_token(pos, 'X')
    assert board.get_token(*pos) == 'X'
    # Checks that the token was placed.
    board.remove_token(pos, 'X')
    assert board.get_token(*pos) is None
    # Removes the token and checks that the cell is empty.
    # Study: Method calls, argument unpacking, state mutation.

def test_invalid_placement_on_corner():
    board = Board()
    with pytest.raises(ValueError):
        board.place_token((0, 0), 'O')
    # Tries to place a token on a corner, expects a ValueError.
    # Study: Board rules, exception testing.

def test_check_sequence_horizontal():
    board = Board()
    for i in range(5):
        board.place_token((0, i + 1), 'X')
    # Places 5 "X" tokens in a horizontal row.
    assert board.check_sequence('X')
    # Checks if the board detects a horizontal sequence.
    # Study: Loops, win condition logic, method calls.

def test_check_sequence_vertical():
    board = Board()
    for i in range(5):
        board.place_token((i + 1, 0), 'X')
    # Places 5 "X" tokens in a vertical column.
    assert board.check_sequence('X')
    # Checks if the board detects a vertical sequence.

def test_check_sequence_diagonal():
    board = Board()
    for i in range(5):
        board.place_token((i + 1, i + 1), 'X')
    # Places 5 "X" tokens in a diagonal (top-left to bottom-right).
    assert board.check_sequence('X')
    # Checks if the board detects a diagonal sequence.

def test_check_sequence_anti_diagonal():
    board = Board()
    for i in range(5):
        board.place_token((i + 1, 9 - i), 'X')
    # Places 5 "X" tokens in an anti-diagonal (top-right to bottom-left).
    assert board.check_sequence('X')
    # Checks if the board detects an anti-diagonal sequence.

def test_remove_token_wrong_player():
    board = Board()
    pos = (1, 1)
    board.place_token(pos, 'X')
    with pytest.raises(ValueError):
        board.remove_token(pos, 'O')
    # Tries to remove a token with the wrong player, expects a ValueError.
    # Study: Defensive programming, error handling.

def test_place_token_out_of_bounds():
    board = Board()
    with pytest.raises(IndexError):
        board.place_token((10, 10), 'X')
    # Tries to place a token outside the board, expects an IndexError.
    # Study: Index bounds checking, exception handling.

def test_board_copy_independence():
    board = Board()
    pos = (1, 1)
    board.place_token(pos, 'X')
    board2 = board.copy()
    board2.place_token((1, 2), 'X')
    assert board.get_token(1, 2) is None
    assert board2.get_token(1, 2) == 'X'
    # Checks that copying the board creates an independent copy (modifying one does not affect the other).
    # Study: Object copying, deep vs shallow copy, test isolation.

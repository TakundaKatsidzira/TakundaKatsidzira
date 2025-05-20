import pytest
from src.board import Board

def test_place_token_and_check_sequence():
    board = Board()

    # Place tokens in a horizontal line for player 1
    player_id = 1
    for c in range(5):
        board.place_token(0, c, player_id)

    # Check sequence detection on last placed token
    assert board.check_sequence_from(0, 4)

def test_no_sequence_for_sparse_tokens():
    board = Board()
    player_id = 2
    board.place_token(0, 0, player_id)
    board.place_token(1, 1, player_id)
    board.place_token(2, 2, player_id)

    # Should be false because no 5 in a row
    assert not board.check_sequence_from(2, 2)

def test_find_all_sequences():
    board = Board()
    player_id = 1
    for c in range(5):
        board.place_token(0, c, player_id)

    sequences = board.find_all_sequences(player_id)
    assert len(sequences) >= 1
    assert sequences[0] == [(0, i) for i in range(5)]

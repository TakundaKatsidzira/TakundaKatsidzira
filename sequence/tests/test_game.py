import pytest
from src.game import Game
from src.player import Player

def test_game_turns_and_winner():
    players = [Player(1, "Alice"), Player(2, "Bob")]
    game = Game(players)

    # Simulate Alice placing 5 tokens in row 0
    for c in range(5):
        game.board.place_token(0, c, 1)

    assert game.board.check_sequence_from(0, 4)
    game.winner = players[0]

    assert game.is_over()
    assert game.winner.name == "Alice"

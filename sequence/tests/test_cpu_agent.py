import pytest
from src.board import Board
from src.game import Game
from src.player import Player
from src.cpu_agent import CPUAgent

def test_cpu_agent_blocks_opponent():
    players = [Player(1, "P1"), Player(2, "CPU", is_cpu=True)]
    game = Game(players)
    cpu = CPUAgent(2)

    # Set up board so opponent has 4 in a row, CPU must block 5th
    for c in range(4):
        game.board.place_token(0, c, 1)

    move = cpu.select_move(game)
    assert move == (0,4)  # CPU blocks at (0,4)

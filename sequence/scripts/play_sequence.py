import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import argparse
from player import Player
from game import Game
from board import Board


def main():
    parser = argparse.ArgumentParser(description="Play the Sequence game.")
    parser.add_argument('--players', type=int, choices=[2,3], default=2,
                        help="Number of players (2 or 3)")
    parser.add_argument('--cpu', type=int, default=0,
                        help="Number of CPU players")
    args = parser.parse_args()

    total_players = args.players
    cpu_count = args.cpu

    if cpu_count > total_players:
        print("CPU count cannot exceed total players.")
        sys.exit(1)

    players = []
    for i in range(total_players):
        is_cpu = i < cpu_count
        name = f"CPU-{i+1}" if is_cpu else f"Player-{i+1-cpu_count}"
        players.append(Player(i+1, name, is_cpu=is_cpu))

    game = Game(players)

    print("Starting Sequence game!")
    while not game.is_over():
        game.play_turn()

    print(f"Game over! Winner: {game.winner.name}")

if __name__ == "__main__":
    main()

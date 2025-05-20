# scripts/play_tictactoe.py
import csv
import os
from datetime import datetime
from src.tictactoe import TicTacToe, RandomAgent, MinimaxAgent

LOG_FILE = os.path.join(os.path.dirname(__file__), '../data/game_logs.csv')

def init_log_file():
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))
    if not os.path.isfile(LOG_FILE):
        with open(LOG_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp", "first_player", "winner", "is_draw",
                "first_move_position", "move_sequence", "num_moves", "win_method"
            ])

def log_game(game: TicTacToe, first_player: str):
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),
            first_player,
            game.winner if game.winner else "None",
            game.is_draw,
            game.move_history[0] if game.move_history else None,
            '-'.join(map(str, game.move_history)),
            len(game.move_history),
            game.win_method if game.win_method else "None"
        ])

def play_game(agent_x, agent_o, verbose=True) -> TicTacToe:
    game = TicTacToe(starting_player='X')
    if verbose:
        print("Starting new TicTacToe game:")
        print(game)
        print()
    while not game.game_over():
        current_agent = agent_x if game.current_player == 'X' else agent_o
        move = current_agent.select_move(game)
        game.make_move(move)
        if verbose:
            print(f"{game.current_player} moved to {move}")
            print(game)
            print()
    if verbose:
        if game.winner:
            print(f"Winner: {game.winner} by {game.win_method}")
        else:
            print("Game ended in a draw.")
    return game

def main():
    init_log_file()

    # Example: RandomAgent vs MinimaxAgent
    agent_x = RandomAgent('X')
    agent_o = MinimaxAgent('O')

    NUM_GAMES = 10000
    for i in range(NUM_GAMES):
        print(f"Game {i+1}/{NUM_GAMES}")
        game = play_game(agent_x, agent_o, verbose=False)
        log_game(game, first_player='X')
    print(f"{NUM_GAMES} games simulated and logged to {LOG_FILE}")

if __name__ == "__main__":
    main()

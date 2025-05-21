import csv  # Imports the csv module for reading/writing CSV files.
# Study: Python standard library, file I/O, CSV file format.

import os    # Imports the os module for interacting with the operating system (paths, directories).
# Study: File paths, directory management, os.path functions.

import sys  # Imports the sys module for system-specific parameters and functions.

import random  # Imports the random module for random number generation.
# Study: Randomness in Python, random.choice, random.shuffle.

from datetime import datetime  # Imports datetime for getting the current timestamp.
# Study: Date and time handling in Python, datetime module.

from src.tictactoe import TicTacToe, RandomAgent, MinimaxAgent
# Imports your game logic and agent classes from your project.
# Study: Python import system, modules, packages, OOP (classes).

LOG_FILE = os.path.join(os.path.dirname(__file__), '../data/game_logs.csv')
# Sets the path for the log file, relative to this script's location.
# Study: __file__ variable, os.path.join, os.path.dirname, relative vs absolute paths.

def init_log_file():
    # Ensures the log directory exists, creates it if not.
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))
        # Study: os.path.exists, os.makedirs, directory creation.
    # Opens the log file for writing (overwrites if exists).
    with open(LOG_FILE, mode='w', newline='') as f:
        writer = csv.writer(f)
        # Creates a CSV writer object.
        writer.writerow([
            "timestamp", "first_player", "winner", "is_draw",
            "first_move_position", "move_sequence", "num_moves", "win_method",
            "agent_X", "agent_O"
        ])
        # Writes the header row for the CSV log.
    # Study: with statement (context manager), file I/O, CSV writing.

def choose_agent(player):
    # Randomly assigns either a RandomAgent or MinimaxAgent to a player ('X' or 'O').
    agent_type = random.choice(['RandomAgent', 'MinimaxAgent'])
    # Picks one of the two agent types at random.
    if agent_type == 'RandomAgent':
        return RandomAgent(player), 'RandomAgent'
        # Instantiates a RandomAgent and returns it with its type as a string.
    else:
        return MinimaxAgent(player), 'MinimaxAgent'
        # Instantiates a MinimaxAgent and returns it with its type as a string.
    # Study: Functions, return values, random.choice, OOP instantiation.

def log_game(game: TicTacToe, first_player: str, agent_X_type: str, agent_O_type: str):
    # Appends a row to the log file with game results and metadata.
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().isoformat(),  # Current timestamp.
            first_player,                # Who started the game.
            game.winner if game.winner else "None",  # Winner or None.
            game.is_draw,                # Boolean: was it a draw?
            game.move_history[0] if game.move_history else None,  # First move.
            '-'.join(map(str, game.move_history)),   # Move sequence as a string.
            len(game.move_history),      # Number of moves.
            game.win_method if game.win_method else "None",  # How the game was won.
            agent_X_type,                # Type of agent for X.
            agent_O_type                 # Type of agent for O.
        ])
    # Study: File I/O, CSV writing, list comprehensions, ternary expressions, string manipulation.

def play_game(agent_x, agent_o, starting_player, verbose=True) -> TicTacToe:
    # Plays a single game between two agents, returns the finished game object.
    game = TicTacToe(starting_player=starting_player)
    # Instantiates a new game, setting the starting player.
    if verbose:
        print("Starting new TicTacToe game:")
        print(game)
        print()
    while not game.game_over():
        # Main game loop: continues until the game is over.
        # Study: while loops, loop conditions, method calls.
        current_agent = agent_x if game.current_player == 'X' else agent_o
        # Selects the agent whose turn it is (ternary/conditional expression).
        move = current_agent.select_move(game)  # Agent chooses a move.
        game.make_move(move)                    # Apply the move to the game.
        # Study: OOP method calls, agent pattern, encapsulation.
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
    # Study: Function return values, game simulation, OOP.

def main():
    init_log_file()  # Set up the log file and header.
    NUM_GAMES = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    # Number of games to simulate.
    
    print("Simulating games...")
    for i in range(NUM_GAMES):
        # Loop to play many games.
        first_player = random.choice(['X', 'O'])  # Randomly choose who starts.
        # Study: for loops, range(), random.choice.

        # Choose agents randomly for each player.
        agent_x, agent_x_type = choose_agent('X')
        agent_o, agent_o_type = choose_agent('O')
        # Study: Tuple unpacking, function calls, OOP.

        game = play_game(agent_x, agent_o, starting_player=first_player, verbose=False)
        # Simulate a game (no output).
        log_game(game, first_player=first_player, agent_X_type=agent_x_type, agent_O_type=agent_o_type)
        # Log the results.
    
    # Study: Print statements, logging, game simulation.
    print(f"{NUM_GAMES} games simulated and logged to {LOG_FILE}")
    # Final summary output.

if __name__ == "__main__":
    main()
# Standard Python idiom: only run main() if this script is executed directly, not imported.
# Study: Script entry points, __name__ variable, module execution.

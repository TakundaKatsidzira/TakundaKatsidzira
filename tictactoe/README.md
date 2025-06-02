TicTacToe 

Build a tic tac toe game where two computer agents play each other using different strategies logging key data and results.
Board handles board logic and win checking, Manages board state using bitmasks

Agent subclasses handle strategy, Agent: Abstract class with select_move()
RandomAgent Picks from available moves at random
RulesAgent plays to win if possible, block opponent if winning move available, else take center, else corner else then edge priority
MinimaxAgent Uses the Minimax algorithm and  dynamic programming (memoization), to simulate all possible future moves and outcomes. It recursively simulates moves until the game ends, then backs up the scores to make the best choice. Consider alpha beta pruning
Game handles gameplay flow, Runs a single game session choosing randomly who goes first and what type of agents match up
Logger is responsible for data capture Logs each game result as a row in a CSV file
Simulator runs 1000s of games, controlled by command line arguments between ai agents
Analyzer script handles post-game insights, Analyzer: Post-processes logs to extract statistical insights 

Bit Manipulation used to represent each player’s moves as a 9-bit integer. Win states are precomputed bitmasks (e.g., 0b111000000 for row 1). Enables constant-time win detection using bitwise AND, Dramatically reduces board comparison time in memoization.
Hash Maps (Memoization), Used in Minimax with Dynamic Programming to cache previously evaluated board states with their scores, Trade-off: memory usage increases, but speeds up repeated state evaluation significantly in large simulations.
Stacks: Used in recursive Minimax to simulate move sequences and undo actions during backtracking
Backtracking: Core of the Minimax implementation. Each possible move is recursively explored, scoring terminal states. Poor branches are pruned where applicable. Evaluates all possible outcomes to select optimal moves. Minimax algorithm simulates all possible future moves and outcomes, choosing the optimal move for the current player by maximizing their minimum gain (or minimizing their maximum loss). A hash map (dictionary) is used to map unique board states to their computed scores for fast lookup. The memoization logic is encapsulated within the agent, ensuring that only the agent manages its cache. Key: Hash the (X_bitmask, O_bitmask, is_X_turn) tuple to get a unique board state.

✅ Full Game Log Schema (CSV-Friendly) Here’s the final field list, with some naming standardization and extras for flexibility:
game_id, int, gamenumber
is_draw, bool, Whether the game ended in a draw
winner, str 'X'/ 'O', or 'Draw'
first_player, str 'X' or 'O', who played first
first_move, int, Index of first move (0–8)
last_move, int, Index of final move
X_move_sequence, list of Moves by X only
O_move_sequence list of Moves by O
game_move_sequence list of  Full sequence of moves 
num_moves_X, int, Number of moves made by X
num_moves_O, int, Number of moves made by O
win_method, str, 'row1', 'row2', ..., 'diag1', 'diag2', or 'None'
agent_X_type, str, Strategy used by X
agent_O_type, str, Strategy used by O 
agent_X_time, float, Total time (sec) X used
agent_O_time, float, Total time (sec) O used
game_time, float, Time from first to last move

📈 Comprehensive Analysis Script Should Extract 🎮 Game Stats total_games
total_draws, total_X_wins, total_O_wins
draw_rate, win_rate_X, win_rate_O
min_moves, max_moves, avg_moves
min_game_time, max_game_time, avg_game_time

📊 Occurrence Counts & Rates Breakdown of absolute counts and relative rates for:
first_player → 'X', 'O'
winner → 'X', 'O', 'Draw'
first_move → index 0–8
last_move → index 0–8
Game-wide position coverage: how often each index appears in game_move_sequence
win_method → row1-3, col1-3, diag1/2
matchup_frequency: agent_X_type vs agent_O_type


tictactoe/
├── src/
│   ├── __init__.py
│   ├── agents.py            # Agent base class# RandomAgent, Rules-based strategy, ForkAgent, MinimaxAgent + memoization
│   ├── board.py             # Board class (bitmask logic) to optimize
│   ├── game.py              # Game class: runs one match
│   ├── simulator.py         # Simulator: runs batch games main entry and  logs each game  to csv
│   └── analyzer.py          # Analyze log data and print insights to terminal
|
├── data/
│   └── games_log.csv        # Game results (auto-generated)
│
├── scripts/ ## bash scrpts to :
│   ├── game.sh          # CLI entry point for running  simulations number as command line arg
│   ├── analysis.sh      # CLI for analyzing results
│   ├── clean.sh         # clean and delete logs and pycache
│   └── tests.sh         # run tests 
│
├── tests/
│   ├── test_board.py     # test board logic
│   ├── test_agents.py    # test agent clases and functions
│   └── test_game.py      # test game logic outcomes etc
├── .gitignore
└── README.md


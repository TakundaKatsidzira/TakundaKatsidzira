TicTacToe AI Simulation Engine
Project Summary

tictactoe/
├── src/
│   ├── __init__.py
│   ├── agents.py            # Agent base class# RandomAgent, Rules-based strategy, MinimaxAgent + memoization, ForkAgent with forking  logic.
│   ├── board.py             # Board class (bitmask logic) to optimize
│   ├── game.py              # Game class: runs one match
│   ├── logger.py            # Logger class: logs to CSV
│   ├── simulator.py         # Simulator: runs batch games main entry to log to csv
│   ├── analyzer.py          # Analyzer: reads logs, computes stats
│   └── utils.py             # helpers eatc and store calculations that help other modules
│
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
│   ├── test_agents.py    # test agent clases and functions
│   └── test_game.py # test game logic outcomes etc
├── .gitignore
└── README.md

This engine simulates thousands of TicTacToe games(specific decided by command line argument) between computer-controlled agents with different strategies. Who goes first is randomized and so is which agents match up againts each other. Each game is played silently (no board output) and logged with rich metadata for post-game analysis. The design focuses on time and space optimization, clean OOP architecture, and data-driven insight generation.

✅ Full Game Log Schema (CSV-Friendly) Here’s the final field list, with some naming standardization and extras for flexibility:

data to log in csv format
Field, Name,  Description
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

🧩 Uniqueness / Diversity Stats distinct_X_sequences

distinct_O_sequences, distinct_X_sequence
distinct_game_sequences

📊 Occurrence Counts & Rates Breakdown of absolute counts and relative rates for:

first_player → 'X', 'O'
winner → 'X', 'O', 'Draw'
first_move → index 0–8
last_move → index 0–8
Game-wide position coverage: how often each index appears in game_move_sequence
win_method → row1-3, col1-3, diag1/2
matchup_frequency: agent_X_type vs agent_O_type

⚔️ Outcome Breakdown (W/L/D) by Dimensions by 
player Outcome by being X or O, agent_type, Outcome by strategy used (e.g., minimax, random), order of moves, Outcome as first vs secondm, first_move Outcome by first move index, last_move Outcome by last move index, win_method Distribution of how games are won matchup By agent_X_type vs agent_O_type, X_move_sequence Outcome rate for exact X sequences O_move_sequence Same for O
The system uses fundamental OOP principles to ensure maintainability, scalability, and testability:

Single Responsibility Principle
Game handles gameplay flow
Board handles board logic and win checking
Agent subclasses handle strategy
Logger is responsible for data capture
Analyzer script handles post-game insights
Modules and Class Design
Game: Runs a single game session\
Board: Manages board state using arrays and bitmasks
Agent: Abstract class with select_move()
RandomAgent Picks from available moves at random
RulesAgent plays to win if possible,block opponent if not, else take centre, else corner else then edge priority
MinimaxAgent Uses the Minimax algorithm to simulate all possible future moves and outcomes. It recursively simulates moves until the game ends, then backs up the scores to make the best choice.
ForkAgent Looks for opportunities to immediately create a fork—a position with two threats to win, if not available picks move likely to set up a fork picking from common patterns, if not possible random
Logger: Logs each game result as a row in a CSV file
Simulator: Orchestrates batch simulations
Analyzer: Post-processes logs to extract statistical insights
Techniques and Data Structures

Arrays
Used to represent the 3x3 board. Fast constant-time access, minimal overhead.
Bit Manipulation
Each player’s moves are stored in a 9-bit integer (int). Win states are precomputed bitmasks (e.g., 0b111000000 for row 1).
Enables constant-time win detection using bitwise AND.
Dramatically reduces board comparison time in memoization.
Hash Maps (Memoization)
Used in Minimax with Dynamic Programming to cache previously evaluated board states with their scores.
Trade-off: memory usage increases, but speeds up repeated state evaluation significantly in large simulations.
Stacks
Used in recursive Minimax to simulate move sequences and undo actions during backtracking
Heaps (Optional in Analysis)
Identify top-k most effective opening moves, frequent winning paths.
Algorithmic Techniques
Backtracking
Core of the Minimax implementation. Each possible move is recursively explored, scoring terminal states. Poor branches are pruned where applicable.
(Algorithms: Backtracking, Recursion) Minimax uses recursion to explore all possible moves (backtracking), scoring terminal states and pruning poor branches for efficiency.
(OOP: Encapsulation) The recursive logic is encapsulated within the MinimaxAgent class, keeping the search logic hidden from other parts of the code.
(Data Structures: Stack) The call stack is used implicitly to keep track of move sequences and to undo moves as recursion unwinds, simulating the process of making and unmaking moves.
Minimax
Evaluates all possible outcomes to select optimal moves.
Minimax algorithm simulates all possible future moves and outcomes, choosing the optimal move for the current player by maximizing their minimum gain (or minimizing their maximum loss).
The MinimaxAgent class inherits from a base Agent class and overrides the select_move() method to implement the Minimax strategy, allowing for interchangeable agent types.
The game state space is conceptually a tree, where each node is a board state and each edge is a possible move.
Two modes: Pure Minimax and Minimax with memoization.
Memoization is used to cache results of previously evaluated board states, avoiding redundant computation and improving efficiency.
The memoization cache is managed internally by the agent, not exposed to other classes.
Dynamic Programming (Memoization)
Reduces exponential time complexity in Minimax by caching board evaluations.
By storing the results of board evaluations, repeated subproblems are solved only once, reducing the overall time complexity from exponential to polynomial in many cases.
A hash map (dictionary) is used to map unique board states to their computed scores for fast lookup.
The memoization logic is encapsulated within the agent, ensuring that only the agent manages its cache.
Key: Hash the (X_bitmask, O_bitmask, is_X_turn) tuple to get a unique board state.
Bitmasks are used to represent board states compactly and uniquely, enabling fast hashing and lookup in the memoization dictionary.
The tuple (X_bitmask, O_bitmask, is_X_turn) serves as a unique key for each possible game state, ensuring correctness and efficiency.
Game Log Analysis (Top-K Elements)
Determine most successful agents, most common winning strategies, and best opening moves.
(Algorithms: Top-K, Heap) Heaps (priority queues) or efficient sorting algorithms are used to extract the most frequent or successful strategies/moves from large game logs.
(Data Structures: Heap, Hash Map) Hash maps count occurrences, and heaps efficiently maintain the top-k elements for reporting.
Analysis is handled by a dedicated Analyzer class or script, keeping concerns separated from gameplay and logging.
Logging Agent Playing, Thinking, and Decision Time
For each move, log the time taken by each agent to decide and play their move ("thinking time" or "decision time").
Each agent or the Game class manages its own timing logic, keeping timing state and logic internal to the object.
Use Python's time module (e.g., time.time() or time.perf_counter()) to record timestamps before and after move selection. Study: Python standard library, time measurement functions, performance profiling.
The logger class/module is responsible for collecting, storing, and aggregating timing data for each agent and the overall game. Study: Separation of concerns, logging patterns, data aggregation.
Enables post-game analysis of agent efficiency, average move time, and performance comparison between strategies. Study: Data analysis, statistics, and visualization techniques.

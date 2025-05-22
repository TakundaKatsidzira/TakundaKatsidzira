## TicTacToe AI Simulation Engine
Project Summary

This engine simulates thousands of TicTacToe games(specific decided by command line argument) between computer-controlled agents with different strategies. Who goes first is randomized and so is which agents match up againts each other.  Each game is played silently (no board output) and logged with rich metadata for post-game analysis. The design focuses on time and space optimization, clean OOP architecture, and data-driven insight generation.

✅ Full Game Log Schema (CSV-Friendly)
Here’s the final field list, with some naming standardization and extras for flexibility:

Field Name	Type	Description
game_id	int	Unique game identifier
is_draw	bool	Whether the game ended in a draw
winner	str	'X', 'O', or 'Draw'
first_player	str	'X' or 'O'
first_move	int	Index of first move (0–8)
last_move	int	Index of final move
X_move_sequence	str	Moves by X only (e.g., '0,4,8')
O_move_sequence	str	Moves by O only
game_move_sequence	str	Full sequence (e.g., 'X0,O4,X8,O3,...')
num_moves_X	int	Number of moves made by X
num_moves_O	int	Number of moves made by O
win_method	str	'row1', 'row2', ..., 'diag1', 'diag2', or 'None'
agent_X_type	str	Strategy used by X
agent_O_type	str	Strategy used by O
agent_X_time	float	Total time (sec) X used
agent_O_time	float	Total time (sec) O used
game_time	float	Time from first to last move

📈 Comprehensive Analysis Script Should Extract
🎮 Game Stats
total_games

total_draws, total_X_wins, total_O_wins

draw_rate, win_rate_X, win_rate_O

min_moves, max_moves, avg_moves

min_game_time, max_game_time, avg_game_time

🧩 Uniqueness / Diversity Stats
distinct_X_sequences

distinct_O_sequences

distinct_game_sequences

📊 Occurrence Counts & Rates
Breakdown of absolute counts and relative rates for:

first_player → 'X', 'O'

winner → 'X', 'O', 'Draw'

first_move → index 0–8

last_move → index 0–8

Game-wide position coverage: how often each index appears in game_move_sequence

win_method → row1-3, col1-3, diag1/2

matchup_frequency: agent_X_type vs agent_O_type

⚔️ Outcome Breakdown (W/L/D) by Dimensions
Dimension	Description
player	Outcome by being X or O
agent_type	Outcome by strategy used (e.g., minimax, random)
order	Outcome as first vs second
first_move	Outcome by first move index
last_move	Outcome by last move index
win_method	Distribution of how games are won
matchup	By agent_X_type vs agent_O_type
X_move_sequence	Outcome rate for exact X sequences
O_move_sequence	Same for O

Fully modular and extensible object-oriented codebase

Object-Oriented Design

The system uses fundamental OOP principles to ensure maintainability, scalability, and testability:

Encapsulation
Each class (e.g., Game, Agent, Board) manages its own state and logic internally.

Inheritance and Polymorphism
Agents derive from a common Agent base class. The RandomAgent and MinimaxAgent override the select_move() method to provide different decision-making strategies.

Single Responsibility Principle

Game handles gameplay flow

Board handles board logic and win checking

Agent subclasses handle strategy

Logger is responsible for data capture

Analyzer script handles post-game insights

Modules and Class Design

Game: Runs a single game session

Board: Manages board state using arrays and bitmasks

Agent: Abstract class with select_move()

RandomAgent Picks from available moves at random

RulesAgent plays to win if possible,block opponent if not, else take centre, else corner else then edge priority

MinimaxAgent Uses the Minimax algorithm to simulate all possible future moves and outcomes. It recursively simulates moves until the game ends, then backs up the scores to make the best choice.

ForkAgent   Looks for opportunities to immediately create a fork—a position with two threats to win, if not available picks move likely to set up a fork picking from common patterns, if not possible random

Logger: Logs each game result as a row in a CSV file

Simulator: Orchestrates batch simulations

Analyzer: Post-processes logs to extract statistical insights

Techniques and Data Structures

1. Arrays

Used to represent the 3x3 board. Fast constant-time access, minimal overhead.

2. Bit Manipulation

Each player’s moves are stored in a 9-bit integer (int). Win states are precomputed bitmasks (e.g., 0b111000000 for row 1).

Enables constant-time win detection using bitwise AND.

Dramatically reduces board comparison time in memoization.

3. Hash Maps (Memoization)

Used in Minimax with Dynamic Programming to cache previously evaluated board states with their scores.

Trade-off: memory usage increases, but speeds up repeated state evaluation significantly in large simulations.

4. Stacks

Used in recursive Minimax to simulate move sequences and undo actions during backtracking.

5. Prefix Sum (In Analysis Script)

Used to aggregate win/draw stats by move positions and opening patterns efficiently.

6. Heaps (Optional in Analysis)

Identify top-k most effective opening moves, frequent winning paths.

Algorithmic Techniques

1. Backtracking

Core of the Minimax implementation. Each possible move is recursively explored, scoring terminal states. Poor branches are pruned where applicable.
# (Algorithms: Backtracking, Recursion) Minimax uses recursion to explore all possible moves (backtracking), scoring terminal states and pruning poor branches for efficiency.
# (OOP: Encapsulation) The recursive logic is encapsulated within the MinimaxAgent class, keeping the search logic hidden from other parts of the code.
# (Data Structures: Stack) The call stack is used implicitly to keep track of move sequences and to undo moves as recursion unwinds, simulating the process of making and unmaking moves.

2. Minimax

Evaluates all possible outcomes to select optimal moves.
# (Algorithms: Minimax, Game Theory) Minimax algorithm simulates all possible future moves and outcomes, choosing the optimal move for the current player by maximizing their minimum gain (or minimizing their maximum loss).
# (OOP: Inheritance/Polymorphism) The MinimaxAgent class inherits from a base Agent class and overrides the select_move() method to implement the Minimax strategy, allowing for interchangeable agent types.
# (Data Structures: Tree) The game state space is conceptually a tree, where each node is a board state and each edge is a possible move.

Two modes: Pure Minimax and Minimax with memoization.
# (Algorithms: Dynamic Programming) Memoization is used to cache results of previously evaluated board states, avoiding redundant computation and improving efficiency.
# (OOP: Encapsulation) The memoization cache is managed internally by the agent, not exposed to other classes.

3. Dynamic Programming (Memoization)

Reduces exponential time complexity in Minimax by caching board evaluations.
# (Algorithms: Dynamic Programming, Memoization) By storing the results of board evaluations, repeated subproblems are solved only once, reducing the overall time complexity from exponential to polynomial in many cases.
# (Data Structures: Hash Map) A hash map (dictionary) is used to map unique board states to their computed scores for fast lookup.
# (OOP: Encapsulation) The memoization logic is encapsulated within the agent, ensuring that only the agent manages its cache.

Key: Hash the (X_bitmask, O_bitmask, is_X_turn) tuple to get a unique board state.
# (Data Structures: Hash Map, Bit Manipulation) Bitmasks are used to represent board states compactly and uniquely, enabling fast hashing and lookup in the memoization dictionary.
# (Algorithms: Hashing) The tuple (X_bitmask, O_bitmask, is_X_turn) serves as a unique key for each possible game state, ensuring correctness and efficiency.

4. Game Log Analysis (Top-K Elements)

Determine most successful agents, most common winning strategies, and best opening moves.
# (Algorithms: Top-K, Heap) Heaps (priority queues) or efficient sorting algorithms are used to extract the most frequent or successful strategies/moves from large game logs.
# (Data Structures: Heap, Hash Map) Hash maps count occurrences, and heaps efficiently maintain the top-k elements for reporting.
# (OOP: Single Responsibility Principle) Analysis is handled by a dedicated Analyzer class or script, keeping concerns separated from gameplay and logging.

---

Logging Agent Playing, Thinking, and Decision Time

For each move, log the time taken by each agent to decide and play their move ("thinking time" or "decision time").
# (OOP: Encapsulation) Each agent or the Game class manages its own timing logic, keeping timing state and logic internal to the object.
# (DSA: Timestamps, Time Measurement) Use Python's time module (e.g., time.time() or time.perf_counter()) to record timestamps before and after move selection. Study: Python standard library, time measurement functions, performance profiling.
# (OOP: Logging, Data Aggregation) The logger class/module is responsible for collecting, storing, and aggregating timing data for each agent and the overall game. Study: Separation of concerns, logging patterns, data aggregation.
# (Analysis) Enables post-game analysis of agent efficiency, average move time, and performance comparison between strategies. Study: Data analysis, statistics, and visualization techniques.

**Example log fields:**
- agent_X_time: Total time (sec) X used for all moves
  # (OOP: Attribute Aggregation) Each agent or the logger maintains a running total of time spent. Study: Attribute management, aggregation patterns.
- agent_O_time: Total time (sec) O used for all moves
  # (OOP: Attribute Aggregation) Same as above for the other agent.
- move_times_X: List of time taken for each move by X (optional, for deeper analysis)
  # (DSA: List/Array) Store per-move times in a list for further statistical analysis. Study: List operations, data collection.
- move_times_O: List of time taken for each move by O
  # (DSA: List/Array) Same as above for the other agent.
- game_time: Total elapsed time for the game
  # (DSA: Time Measurement) Calculate the difference between the start and end timestamps of the game. Study: Time arithmetic, performance measurement.

**Analysis Script Should Extract:**
- Average, min, max, and standard deviation of move times per agent/strategy
  # (DSA: Statistics) Use statistical functions to summarize timing data. Study: Python's statistics module, descriptive statistics.
- Comparison of thinking time between agent types (e.g., Minimax vs Random)
  # (OOP: Polymorphism) Different agent subclasses can be compared based on their timing data. Study: Class inheritance, method overriding, comparative analysis.
- Correlation between decision time and win rate or move quality
  # (DSA: Correlation Analysis) Analyze relationships between timing and outcomes. Study: Correlation coefficients, data science basics.
- Outlier detection (e.g., unusually long or short moves)
  # (DSA: Outlier Detection) Identify and analyze outliers in timing data. Study: Box plots, z-scores, robust statistics.
- Aggregate statistics for total and per-move decision time
  # (DSA: Aggregation) Summarize timing data for reporting and visualization. Study: Data aggregation, reporting.

**How to implement:**
- Before calling an agent's move selection, record the start time.
  # (DSA: Timestamping) Use time.time() or time.perf_counter() to get the current time. Study: Function calls, time measurement.
- After the move is selected, record the end time and compute the difference.
  # (DSA: Time Arithmetic) Subtract start from end to get elapsed time. Study: Arithmetic operations, variable assignment.
- Accumulate this per agent and log it in the game log.
  # (OOP: Attribute Update, Logging) Update the agent's or logger's attributes and write to the log. Study: Attribute mutation, logging best practices.
- In analysis, compute summary statistics and visualize distributions of decision times.
  # (DSA: Data Analysis, Visualization) Use libraries like pandas, matplotlib, or seaborn to analyze and visualize timing data. Study: Data science tools, visualization techniques.

This enables detailed analysis of agent performance, efficiency, and strategic complexity.
# (OOP: Modularity, Extensibility) The design allows for easy extension to new agent types or additional logging fields. Study: Modular code design, extensibility patterns.
# (DSA: Data-Driven Insights) Rich logs support advanced analytics and data-driven improvements to agent strategies. Study: Data-driven development, feedback loops.

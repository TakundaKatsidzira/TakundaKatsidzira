===========================
SEQUENCE GAME
===========================

A command-line implementation of the classic board game "Sequence" featuring both human and AI players. This version supports efficient gameplay logic, strategic AI, and optimized win detection using algorithms like sliding window and dynamic programming.
# (OOP: Abstraction, Encapsulation) The game logic is abstracted into classes and modules, hiding complexity from the user and exposing a simple interface.
# (DSA: Sliding Window, Dynamic Programming) Efficient win detection and AI logic use these algorithmic techniques.

---------------------------
HOW TO PLAY
---------------------------

1. RUNNING THE GAME:
   - Run the main script:
     $ python sequence.py
   # (DSA: Script Entry Point) The main script acts as the entry point, orchestrating the game flow.

   - Follow the prompts to:
     * Choose play mode, human vs human or human vs computer
     * Play cards from your hand while recycling them wih deck
     * Place or remove tokens on the board
   # (OOP: Polymorphism) The game supports different player types (human/AI) using polymorphism.
   # (DSA: Queue/Stack) Card drawing and recycling use queue/stack data structures.

2. GAME RULES:
   - The board is a 10x10 grid with playing cards mapped to positions.
   - Each player/team tries to form sequences of 5 tokens in a row. to win, horizontally, vertically or diagonally
   - "Two-Eyed Jacks" (JO) are wild and can place a token anywhere thats available.
   - "One-Eyed Jacks" (JT) allow removing an opponent’s token to disrupt sequences
   # (OOP: Encapsulation) Board and card logic are encapsulated in their respective classes.
   # (DSA: 2D Array, Hash Map) The board is a 2D array; card-to-position mapping uses a hash map.

---------------------------
FEATURES & ENHANCEMENTS
---------------------------

---
Parallelized Move Evaluation: When AI evaluates multiple options use multithreading or multiprocessing for speedup.
# (DSA: Parallelism, Concurrency) Uses multiple cores for faster AI decision-making.
# (DSA: Parallelism, Concurrency) This can be applied in:
# - Minimax move evaluation: Each possible move at the root of the search tree can be evaluated in parallel, distributing the computation across threads or processes.
# - Heuristic evaluation: When scoring multiple board states (e.g., for Monte Carlo simulations or batch heuristic scoring), parallelism can be used to evaluate many states at once.
# - Simulation-based AI (e.g., Monte Carlo Tree Search): Each simulation or rollout can be run in parallel to speed up statistical evaluation.
# - Game log analysis: When analyzing large numbers of logged games or moves for statistics or training data, parallel processing can accelerate aggregation and pattern detection.
# - Sequence detection: If checking for sequences in multiple directions or for multiple players, these checks can be parallelized for large boards or batch analysis.
# (OOP: Encapsulation, Modularity) Parallel logic should be encapsulated in utility functions or within the AI class, keeping threading/multiprocessing details hidden from the main game logic.

## ✅ ACCURATE GAME MECHANICS

**OOP Strategies**:
Use classes such as `Deck`, `Hand`, `Board` and `Card` to encapsulate their responsibilities cleanly. The `Player` class can use composition to hold a `Hand` and interact with the `Board`. Inheritance allows for easy extension, such as `AIPlayer` inheriting from `Player`. Encapsulation ensures that methods like `hand.draw()` or `deck.shuffle()` maintain game integrity without exposing internal structures.
# (OOP: Encapsulation, Composition, Inheritance) Each class is responsible for its own state and behavior; composition and inheritance enable code reuse and extension.

**DSA Strategies**:
Use a 2D array to represent the board state. Hash maps are useful for mapping cards to positions (`card_to_positions`) and tracking ownership of tokens. Sets can track played cards efficiently. Queues or stacks can manage card drawing and discarding behavior in the deck and hand logic.
# (DSA: 2D Array, Hash Map, Set, Queue/Stack) Efficient data structures are chosen for board state, card mapping, and card management.

---

## ✅ AI PLAYER

**OOP Strategies**:
`AIPlayer` extends `Player`, encapsulating all decision logic. This makes AI code modular and testable. AI state like known cards, probabilities, and evaluations are internal to the class. The heuristic function and move selection logic are separated into methods or utility classes, keeping responsibilities clear.
# (OOP: Inheritance, Encapsulation, Single Responsibility) AI logic is modular, testable, and separated from other game logic.

**DSA Strategies**:
Use the Minimax algorithm with alpha-beta pruning to explore move trees efficiently. Memoization is applied using dictionaries keyed by board state and hand, to prevent recalculating scores for the same game situations. Heuristic evaluations are used to rank board states based on open sequences, central board control, and token clustering. The AI introduces controlled randomness when choosing among equally good moves to avoid being predictable. It also tracks cards played by others to estimate remaining probabilities and improve blocking decisions.AI keeps track of cards still available, not played already in using Hash set. Uses knowing available card How:
# (DSA: Minimax, Alpha-Beta Pruning, Memoization, Heuristic Evaluation, Hash Set) Advanced algorithms and data structures optimize AI performance and decision-making.

Include card-based probabilities in the board evaluation function, Track Played Cards, During simulation, filter moves by whether cards to execute them likely exist, Infer Remaining Cards, Ensures deeper Minimax branches are more realistic, Avoids over-valuing unlikely sequences. use in  Jack Usage Strategy, Probability-Aware Move Selection, Opponent Hand Estimation
How:
# (DSA: Probability, Simulation, Filtering, Game Theory) AI uses probability and simulation to make realistic decisions.

---

## ✅ SEQUENCE DETECTION OPTIMIZED

**OOP Strategies**:
Encapsulate all sequence detection logic within the `Board` class . Ensure it works in both player turns and AI simulations. Make it modular and reusable for maintainability.
# (OOP: Encapsulation, Modularity, Reusability) Sequence detection is a self-contained, reusable component.

**DSA Strategies**:
Use a sliding window of length 5 across rows, columns, and diagonals to efficiently detect potential winning sequences. Two pointers are used within each line scan to track streaks of the same token. Diagonal and anti-diagonal scans are supported by iterating over offset-based index ranges. Wildcards (e.g., Jacks and corner tokens) are included in detection logic using flexible match conditions. This detection logic is designed to be fast and work across both real gameplay and simulated AI evaluations.
# (DSA: Sliding Window, Two Pointers, Flexible Matching) Efficient algorithms for sequence detection, supporting wildcards and all directions.

---

## ✅ PERFORMANCE STRATEGIES

**OOP Strategies**:
The game supports move simulations through clean interfaces like `board.place_token()` and `board.undo_token()`. This helps the AI simulate turns without affecting the actual game state. The system is designed to be stateless during evaluation by copying or cloning board instances when needed.
# (OOP: Interface Design, Statelessness, Copying) Interfaces and stateless design allow safe simulation and evaluation.

**DSA Strategies**:
Use dynamic programming to cache repeated evaluations of board configurations, such as streak checks or open sequences. The AI can use backtracking to simulate future game states and evaluate consequences. Stacks are used for undo/redo mechanics, tracking player actions and token placements. Prefix sum grids can be integrated later for efficient density analysis of token clusters, aiding both heuristics and strategic AI planning.
# (DSA: Dynamic Programming, Backtracking, Stack, Prefix Sum) Advanced algorithmic techniques for performance and analysis.

---

## ✅ CODE ORGANIZATION

Each module is focused on a single responsibility. The `sequence.py` script acts as the game entry point, controlling turn order, input, and progression. The `board.py` file handles token placements, move validations, and sequence detection. The `deck.py` module manages card distribution and hand mechanics. The `player.py` module defines `Player` classes and their core actions. The `ai.py` module contains Minimax logic, scoring heuristics, and all strategic AI functionality. `mapping.py` manages the relationship between cards and their board positions. `utils.py` supports user-facing board display. Finally, `logger.py` captures turn-by-turn logs and stores them as structured JSON for debugging or analytics.
# (OOP: Single Responsibility Principle, Modularity) Each module/class has a clear, focused responsibility, improving maintainability and scalability.

---

## ✅ LOGGING

**OOP Strategies**:
All logging is handled via a dedicated `Logger` class or module. It offers clean functions like `log_turn(data)` or `log_game_start(players)` to abstract away file operations and formatting. This keeps game logic clean and readable.
# (OOP: Encapsulation, Abstraction) Logging logic is separated from game logic, using clean interfaces.

**DSA Strategies**:
Game events are logged in a structured format (e.g., JSON) with timestamps. Logs track played cards, board state, moves made, and game outcomes. This is useful for game replays, debugging, and analyzing AI behavior post-game. Logs can be stored in a list or buffer before being written to disk, minimizing I/O performance impacts.
# (DSA: Structured Data, Buffering, Timestamps) Efficient and structured logging for analysis and debugging.

---

## ✅ SUMMARY

By combining OOP design patterns like inheritance, encapsulation, and modular composition with algorithmic techniques like Minimax, memoization, sliding window detection, and dynamic programming, your Sequence game becomes both accurate and performant. This structure supports clean scalability, strategic AI, and rich game logging—laying the foundation for future enhancements such as multiplayer networking, GUI integration, or machine learning agents.
# (OOP: Inheritance, Encapsulation, Modularity; DSA: Minimax, Memoization, Sliding Window, Dynamic Programming) The project is built for extensibility, performance, and maintainability.

✅ ENHANCED SEQUENCE DETECTION SYSTEM
Incremental Update Logic: Instead of re-scanning the board each turn, update sequence data only for the affected region of the board—reduces detection time to near-constant per move.
# (DSA: Incremental Update, Locality) Optimizes detection by updating only affected regions.

Weighted Sequences: Instead of binary detection (sequence or not), calculate partial sequence weights for AI scoring (e.g., 3-in-a-row = +3 points).
# (DSA: Weighted Scoring, Heuristics) Enables nuanced AI evaluation.

Line-of-Sight Heuristics: Evaluate not just current sequences, but potential extension paths, using ray-like scanning in all directions.
# (DSA: Ray Scanning, Heuristic Evaluation) Looks ahead for potential moves.

✅ EXTRA PERFORMANCE STRATEGIES
Immutable Board Snapshots: Use copy-on-write for simulating moves in the AI; helps prevent mutation bugs during recursive searches.
# (OOP: Immutability, Copy-on-Write) Ensures safe state management during simulations.

Bitmasking: Represent board token presence with bitmaps for faster comparisons and low-memory storage during simulations.
# (DSA: Bitmasking) Efficient board representation for fast computation.

Lazy Evaluation: Delay costly evaluations (like full sequence detection) until the board state requires it—e.g., after a 4-in-a-row is placed.
# (DSA: Lazy Evaluation) Improves performance by avoiding unnecessary computation.




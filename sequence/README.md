SEQUENCE

A command-line implementation of the classic board game "Sequence" featuring both human and AI players. This version supports efficient gameplay logic, strategic AI, and optimized win detection using algorithms like sliding window and dynamic programming.

1. RUNNING THE GAME:
   - Follow the prompts to:
     * Play vs computer in terminal 
     * Play cards from your hand while recycling them with deck, must have 5 cards always. Game ends if  deck runs out and hand   
       runs out after
     * Place or remove tokens on the board 

2. GAME RULES:
   - The board is a 10x10 grid with playing cards mapped to positions. 2 places for each card, corners as wild cards and no positions for jacks which are special
   - Each player/team tries to form sequences of 5 tokens in a row. to win, horizontally, vertically or diagonally while stopping opponent from doing so.
   - Each player has a deck to draw cards from while playing to maintain a hand of 5 hands.
   - "Two-Eyed Jacks" (JO) are wild and can place a token anywhere thats available.
   - "One-Eyed Jacks" (JT) allow removing an opponent’s token to disrupt sequences

The agent will use the Minimax algorithm with alpha-beta pruning to explore move trees efficiently. Memoization is applied using dictionaries keyed by board state and hand, to prevent recalculating scores for the same game situations. Heuristic evaluations are used to rank board states based on open sequences, central board control, and token clustering. The AI introduces controlled randomness when choosing among equally good moves to avoid being predictable.

Encapsulate all sequence detection logic within the `Board` class . Ensure it works in both player turns and AI simulations. Make it modular and reusable for maintainability. Use a sliding window of length 5 across rows, columns, and diagonals to efficiently detect potential winning sequences. Two pointers are used within each line scan to track streaks of the same token to find sequences while they are being built scoring 1,2,3,4 token sequences of computer and opponent to improve decision making. Diagonal and anti-diagonal scans are supported by iterating over offset-based index ranges. Wildcards (e.g., Jacks and corner tokens) are included in detection logic using flexible match conditions. This detection logic is designed to be fast and work across both real gameplay and simulated AI evaluations.

Incremental Update Logic: Instead of re-scanning the board each turn, update sequence data only for the affected region of the board—reduces detection time to near-constant per move.
Weighted Sequences: Instead of binary detection (sequence or not), calculate partial sequence weights for AI scoring (e.g., 3-in-a-row = +3 points).
cloning board instances when needed.

Use dynamic programming to cache repeated evaluations of board configurations, such as streak checks or open sequences. The AI can use backtracking to simulate future game states and evaluate consequences. Stacks are used for undo/redo mechanics, tracking player actions and token placements. Prefix sum grids can be integrated later for efficient density analysis of token clusters, aiding both heuristics and strategic AI planning.

Lazy Evaluation: Delay costly evaluations (like full sequence detection) until the board state requires it—e.g., after a 4-in-a-row is placed.

Game events are logged in a structured format (e.g., JSON) with timestamps. Logs track played cards, board state, moves made, and game outcomes. This is useful for game replays, debugging, and analyzing AI behavior post-game. Logs can be stored in a list or buffer before being written to disk, minimizing I/O performance impacts.

sequence/
├── src/                           # Core source files
│   ├── __init__.py
│   ├── sequence.py                # Entry point / main loop
│   ├── board.py                   # Game board mapping, rules, token placement, sequence checks and printing
│   ├── cards.py                   #  Handles deck and hand initialization and management, drawing and  recyling 
│   ├── player.py                  # Defines Player class for human to play the game
│   ├── agent.py                   # Defines a strategic AI agent for the player to play against
│   └── utils.py                   # Controls event and state logging as well as configurations and settings
│
├── data/                          # Runtime data and logs
│   └── progression.logs            # Game logs in JSON
│   
│
├── tests/                         # Unit + integration tests
│   ├── __init__.py
│   ├── test_board.py              # test board logic and functions
│   ├── test_agent.py              # test ai agent logic and functions
│   ├── test_cards.py              # test deck and hand logic and functions
│   └── test_player.py             # test player logic and functions
|
├── scripts/                       # Automation
│   ├── game.sh                    # Run game
│   ├── tests.sh                   # Run all tests
│   └── clean.sh                   # Clear logs, reset game and delete pycache
|
├── .gitignore
└── README.md


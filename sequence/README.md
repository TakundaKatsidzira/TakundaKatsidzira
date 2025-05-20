Sequence
Build an accurate version of the Sequence game. Implement board logic, card handling, and rules. Support two or three players or teams. Optimize for performance and allow AI agents with a mix of strategy and randomness. Backtracking can simulate token placements and analyze optimal sequences. Dynamic programming helps detect sequences efficiently on the grid by caching token alignments.
# Sequence Game

An accurate Python implementation of the classic **Sequence** board game supporting 2-3 players or teams, with options to play against CPU opponents. The game supports human vs human, human vs CPU, or team play, with AI agents combining strategic backtracking and randomness.

## Features

- Complete Sequence board logic with card handling and token placements.
- Supports 2 or 3 players/teams.
- Play human vs human, human vs CPU, or team games.
- CPU agents with a mix of strategy and randomness:
  - Backtracking simulates token placements to analyze optimal sequences.
  - Dynamic programming efficiently detects winning sequences by caching token alignments.
- Command-line interface (CLI) to set up game parameters.
- Optimized for performance and extensibility.

## Project Structure

sequence_game/
├── README.md
├── LICENSE
├── setup.py
├── pyproject.toml
├── requirements.txt
├── MANIFEST.in
├── .gitignore
├── docs/
├── tests/
├── src/
│ ├── board.py
│ ├── game.py
│ ├── player.py
│ ├── cpu_agent.py
│ └── utils.py
├── scripts/
│ └── play_sequence.py
├── data/
├── notebooks/
└── .github/

perl
Copy
Edit

## Installation

```bash
pip install -r requirements.txt
python setup.py install
Or install in editable mode for development:

bash
Copy
Edit
pip install -e .
Usage
Run the game CLI with options for player count and CPU:

bash
Copy
Edit
python scripts/play_sequence.py --players 3 --cpu 1
Testing
Run unit tests using pytest:

bash
Copy
Edit
pytest tests/
Contributing
Contributions are welcome! Please open issues or pull requests.
#!/bin/bash

# Base directory
BASE_DIR="/home/takundakatsidzira/projects/TakundaKatsidzira/sequence"

echo "Creating project directory at $BASE_DIR"
mkdir -p "$BASE_DIR"

# Directories
mkdir -p "$BASE_DIR/data"
mkdir -p "$BASE_DIR/docs"
mkdir -p "$BASE_DIR/scripts"
mkdir -p "$BASE_DIR/src"
mkdir -p "$BASE_DIR/tests"
mkdir -p "$BASE_DIR/.github/workflows"

# Files with initial content
touch "$BASE_DIR/LICENSE"
touch "$BASE_DIR/MANIFEST.in"
touch "$BASE_DIR/requirements.txt"
touch "$BASE_DIR/pyproject.toml"
touch "$BASE_DIR/setup.py"
touch "$BASE_DIR/setup_github.sh"
touch "$BASE_DIR/setup.sh"
touch "$BASE_DIR/data/progression.log"
touch "$BASE_DIR/docs/gameplay_rules.md"
touch "$BASE_DIR/docs/index.md"
touch "$BASE_DIR/docs/mkdocs.yml"
touch "$BASE_DIR/scripts/run_game.py"
touch "$BASE_DIR/scripts/run_tests.sh"
touch "$BASE_DIR/scripts/simulate_games.py"
touch "$BASE_DIR/.gitignore"
touch "$BASE_DIR/README.md"
touch "$BASE_DIR/CONTRIBUTING.md"
touch "$BASE_DIR/.github/workflows/ci.yml"

# Python modules in src/
touch "$BASE_DIR/src/__init__.py"
touch "$BASE_DIR/src/ai.py"
touch "$BASE_DIR/src/board.py"
touch "$BASE_DIR/src/deck.py"
touch "$BASE_DIR/src/logger.py"
touch "$BASE_DIR/src/mapping.py"
touch "$BASE_DIR/src/player.py"
touch "$BASE_DIR/src/sequence.py"
touch "$BASE_DIR/src/utils.py"

# Test files
touch "$BASE_DIR/tests/__init__.py"
touch "$BASE_DIR/tests/test_ai.py"
touch "$BASE_DIR/tests/test_board.py"
touch "$BASE_DIR/tests/test_deck.py"
touch "$BASE_DIR/tests/test_player.py"

echo "Project scaffold created successfully at:"
tree "$BASE_DIR"

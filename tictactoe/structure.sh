#!/bin/bash

# Define base directory
BASE_DIR=~/projects/TakundaKatsidzira/tictactoe

# Create the directory structure
mkdir -p "$BASE_DIR"/{src,tests,data,scripts}

# Create main files
touch "$BASE_DIR"/README.md
touch "$BASE_DIR"/setup.py
touch "$BASE_DIR"/requirements.txt

# Create source files
touch "$BASE_DIR"/src/__init__.py
touch "$BASE_DIR"/src/tictactoe.py

# Create test files
touch "$BASE_DIR"/tests/__init__.py
touch "$BASE_DIR"/tests/test_tictactoe.py

# Create data file
touch "$BASE_DIR"/data/game_logs.csv

# Create script file
touch "$BASE_DIR"/scripts/play_tictactoe.py

echo "Project structure created at $BASE_DIR"

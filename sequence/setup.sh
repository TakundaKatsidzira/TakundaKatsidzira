#!/bin/bash

BASE_DIR=~/projects/TakundaKatsidzira/sequence

echo "Creating project directories and files at $BASE_DIR"

# Create base directory
mkdir -p "$BASE_DIR"

# Create root files
touch "$BASE_DIR/README.md" \
      "$BASE_DIR/LICENSE" \
      "$BASE_DIR/setup.py" \
      "$BASE_DIR/pyproject.toml" \
      "$BASE_DIR/requirements.txt" \
      "$BASE_DIR/MANIFEST.in" \
      "$BASE_DIR/.gitignore"

# Create directories
mkdir -p "$BASE_DIR/docs"
mkdir -p "$BASE_DIR/tests"
mkdir -p "$BASE_DIR/src"
mkdir -p "$BASE_DIR/scripts"
mkdir -p "$BASE_DIR/data"
mkdir -p "$BASE_DIR/notebooks"
mkdir -p "$BASE_DIR/.github"

# Create source files inside src/
touch "$BASE_DIR/src/board.py" \
      "$BASE_DIR/src/game.py" \
      "$BASE_DIR/src/player.py" \
      "$BASE_DIR/src/cpu_agent.py" \
      "$BASE_DIR/src/utils.py"

# Create scripts
touch "$BASE_DIR/scripts/play_sequence.py"

echo "Project structure created successfully."

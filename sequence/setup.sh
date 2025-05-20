#!/bin/bash

BASE_DIR=~/projects/TakundaKatsidzira/sequence

echo "Creating project directories and files under $BASE_DIR ..."

# Create directories
mkdir -p $BASE_DIR/docs
mkdir -p $BASE_DIR/data
mkdir -p $BASE_DIR.scripts
mkdir -p $BASE_DIR/scripts
mkdir -p $BASE_DIR/src/sequence_game
mkdir -p $BASE_DIR/tests
mkdir -p $BASE_DIR/.github/workflows

# Create root files
touch $BASE_DIR/README.md
touch $BASE_DIR/LICENSE
touch $BASE_DIR/setup.py
touch $BASE_DIR/pyproject.toml
touch $BASE_DIR/requirements.txt
touch $BASE_DIR/MANIFEST.in
touch $BASE_DIR/.gitignore

# Docs
touch $BASE_DIR/docs/index.md
touch $BASE_DIR/docs/gameplay_rules.md

# Data
touch $BASE_DIR/data/card_mappings.json
touch $BASE_DIR/data/progression.log

# Scripts
touch $BASE_DIR/scripts/run_game.py
touch $BASE_DIR/scripts/run_tests.sh
touch $BASE_DIR/scripts/simulate_games.py

# Src module files
touch $BASE_DIR/src/sequence_game/__init__.py
touch $BASE_DIR/src/sequence_game/board.py
touch $BASE_DIR/src/sequence_game/card.py
touch $BASE_DIR/src/sequence_game/player.py
touch $BASE_DIR/src/sequence_game/game.py
touch $BASE_DIR/src/sequence_game/ai.py
touch $BASE_DIR/src/sequence_game/cli.py
touch $BASE_DIR/src/sequence_game/config.py
touch $BASE_DIR/src/sequence_game/utils.py
touch $BASE_DIR/src/sequence_game/logging_config.py

# Tests
touch $BASE_DIR/tests/__init__.py
touch $BASE_DIR/tests/test_board.py
touch $BASE_DIR/tests/test_card.py
touch $BASE_DIR/tests/test_player.py
touch $BASE_DIR/tests/test_game.py
touch $BASE_DIR/tests/test_ai.py

# GitHub workflows and issue template
touch $BASE_DIR/.github/ISSUE_TEMPLATE.md
touch $BASE_DIR/.github/workflows/ci.yml

echo "Setup complete!"

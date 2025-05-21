#!/bin/bash

# Activate virtual environment if exists
if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
fi

# Ensure src is in PYTHONPATH for package imports
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PYTHONPATH="$PROJECT_ROOT/src:$PYTHONPATH"

# Run the Sequence game as a module
python -m src.sequence

# Deactivate venv after running (optional)
if [ -n "$VIRTUAL_ENV" ]; then
  deactivate
fi
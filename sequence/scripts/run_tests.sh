#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Running tests..."

# Navigate to the project root
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$PROJECT_ROOT"

# Activate virtual environment if it exists
if [ -f "venv/bin/activate" ]; then
  source venv/bin/activate
fi

# Ensure src is in PYTHONPATH for package imports
export PYTHONPATH="$PROJECT_ROOT/src:$PYTHONPATH"

# Run tests with pytest
pytest tests --maxfail=5 --disable-warnings -v

echo "All tests completed."
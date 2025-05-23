#!/bin/bash

# Exit on any error
set -e

# Navigate to project root (this script lives in scripts/)
cd "$(dirname "$0")/.."

echo "🧪 Running all unit tests in tests/..."

# Run unittest discovery from the project root
PYTHONPATH=src python3 -m unittest discover -s tests -p "test_*.py" -v

echo "✅ All tests completed."

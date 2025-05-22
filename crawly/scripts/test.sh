#!/bin/bash

echo "🧪 Running all unit tests in tests/..."

# Run Python's unittest discovery in the tests/ folder
python3 -m unittest discover -s tests -p 'test_*.py'

echo "✅ All tests completed."

#!/bin/bash
# Exit on any error
set -e

# Navigate to project root (this script lives in scripts/)
cd "$(dirname "$0")/.."

# Run unittest discovery from the project root
#!/bin/bash
#!/bin/bash
echo "🧪 Running all unit tests in tests/..."
PYTHONPATH=src python3 -m unittest discover -s tests -p "test_*.py"

echo "✅ All tests completed."



#!/bin/bash
rm -f data/state.json data/history.log
find . -type d -name "__pycache__" -exec rm -rf {} +
echo "✅ All __pycache__ directories  removed and VFS reset"

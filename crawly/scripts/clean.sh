#!/bin/bash

echo "🧹 Cleaning __pycache__ files in project..."

# Find and delete all __pycache__ directories
find . -type d -name "__pycache__" -exec rm -r {} +

echo "✅ All __pycache__ directories removed."

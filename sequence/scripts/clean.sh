#!/bin/bash

# Remove all __pycache__ directories in the parent directory and all subdirectories
find .. -type d -name "__pycache__" -exec rm -rf {} +

echo "All __pycache__ directories removed."
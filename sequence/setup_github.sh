#!/bin/bash
set -e

echo "Initializing git repository..."
git init "/home/takundakatsidzira/projects/TakundaKatsidzira/sequence"

cd "/home/takundakatsidzira/projects/TakundaKatsidzira/sequence"

echo "Adding all files..."
git add .

echo "Creating initial commit..."
git commit -m "Initial commit - project scaffold"

echo "Setting up GitHub remote..."
git remote add origin git@github.com:TakundaKatsidzira/TakundaKatsidzira.git

echo "Pushing to GitHub..."
git branch -M main
git push -u origin main

echo "GitHub setup complete."

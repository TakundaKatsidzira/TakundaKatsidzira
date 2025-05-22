#!/bin/bash

echo "🔧 Setting up aliases..."
cat << 'EOF' >> ~/.bashrc

# Custom Aliases
alias cls='clear'
alias py='python3'
alias act='source venv/bin/activate'
alias touchpy='f(){ touch "$1.py"; } ; f'
alias rpy='f(){ python3 "$1.py"; } ; f'
alias sudo-last='sudo $(fc -ln -1)'
alias mcd='f(){ mkdir -p "$1" && cd "$1"; }; f'
alias mcdcp='f(){ mkdir -p "$1" && cd "$1" && touch "$1.py"; }; f'
alias gp='git add . && git commit -m "update" && git push'
alias updateall='sudo apt update && sudo apt upgrade -y'

EOF

echo "✅ Aliases added to .bashrc"

echo "📦 Installing essential packages..."
sudo apt install -y python3-venv python3-pip python3-full build-essential curl git

# Optional: create venv
python3 -m venv venv
source venv/bin/activate

# Install common Python packages
pip install --upgrade pip
pip install \
    rich loguru ipython python-dotenv typer \
    more-itertools networkx numpy joblib \
    ipdb pytest pytest-cov \
    black isort flake8 mypy \
    requests beautifulsoup4 lxml pandas tabulate

echo "📁 Setup complete. Reload terminal or run: source ~/.bashrc"

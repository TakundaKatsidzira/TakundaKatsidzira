# logger.py

import csv
import os

LOG_PATH = "../data/games_log.csv"

CSV_FIELDS = [
    "game_id",
    "is_draw",
    "winner",
    "first_player",
    "first_move",
    "last_move",
    "X_move_sequence",
    "O_move_sequence",
    "game_move_sequence",
    "num_moves_X",
    "num_moves_O",
    "win_method",
    "agent_X_type",
    "agent_O_type",
    "agent_X_time",
    "agent_O_time",
    "game_time"
]

def init_log():
    """Initialize the log file if it does not exist."""
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
            writer.writeheader()

def reset_log():
    """Completely reset the log file, erasing all previous entries."""
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    with open(LOG_PATH, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()

def log_game(game_summary):
    """Append a game summary to the CSV log."""
    with open(LOG_PATH, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        # Serialize list fields as strings
        row = {
            key: (",".join(map(str, val)) if isinstance(val, list) else val)
            for key, val in game_summary.items()
        }
        writer.writerow(row)

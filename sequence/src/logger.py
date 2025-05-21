import os
# Imports the os module for interacting with the operating system (like file paths and directories).
# Study: Python standard library, os.path, directory management.

import json
# Imports the json module for encoding and decoding JSON data.
# Study: JSON format, serialization, deserialization, file I/O.

from datetime import datetime
# Imports the datetime class for working with timestamps.
# Study: Date and time handling in Python, datetime module.

LOG_DIR = "data"
# Sets the directory where log files will be stored.
# Study: String variables, file system organization.

LOG_FILE = os.path.join(LOG_DIR, "progression.log")
# Constructs the full path to the log file using os.path.join for cross-platform compatibility.
# Study: File path construction, os.path functions.

def ensure_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    # Checks if the log directory exists, and creates it if it doesn't.
    # Study: os.path.exists, os.makedirs, defensive programming.

def log_turn(turn_data):
    """
    Append JSON log entry of a turn to progression.log
    turn_data: dict with keys like player, move, hand, board state etc.
    """
    ensure_log_dir()
    with open(LOG_FILE, "a") as f:
        json.dump(turn_data, f)
        f.write("\n")
    # Opens the log file in append mode, writes the turn data as a JSON object, and adds a newline.
    # Study: File I/O, context managers (with), JSON serialization, append mode.

def log_game_start(players):
    """
    Log game start event: player names and tokens.
    """
    ensure_log_dir()
    start_data = {
        "event": "game_start",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        # Uses UTC time in ISO format for consistency and interoperability.
        "players": [{"name": p.name, "token": p.token} for p in players]
        # Builds a list of player info dictionaries using a list comprehension.
        # Study: List comprehensions, object attribute access, dictionary construction.
    }
    with open(LOG_FILE, "w") as f:  # overwrite on new game start
        json.dump(start_data, f)
        f.write("\n")
    # Opens the log file in write mode (overwriting any previous content), writes the start data as JSON, and adds a newline.
    # Study: File I/O, write mode, JSON serialization.

def log_game_end(winner_name):
    """
    Log game end event with winner name or None for draw.
    """
    ensure_log_dir()
    end_data = {
        "event": "game_end",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "winner": winner_name
    }
    with open(LOG_FILE, "a") as f:
        json.dump(end_data, f)
        f.write("\n")
    # Opens the log file in append mode, writes the end data as JSON, and adds a newline.
    # Study: File I/O, append mode, JSON serialization, logging conventions.

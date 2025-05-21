boardLayout = {
    # A dictionary mapping string coordinates (like "(0,0)") to card codes (like "2S") or None for corners.
    # Study: Python dictionaries, key-value pairs, string formatting, board representation.
    "(0,0)": None, "(0,1)": "2S", "(0,2)": "3S", "(0,3)": "4S", "(0,4)": "5S", "(0,5)": "6S", "(0,6)": "7S", "(0,7)": "8S", "(0,8)": "9S", "(0,9)": None,
    "(1,0)": "6C", "(1,1)": "5C", "(1,2)": "4C", "(1,3)": "3C", "(1,4)": "2C", "(1,5)": "AH", "(1,6)": "KH", "(1,7)": "QH", "(1,8)": "10H", "(1,9)": "10S",
    "(2,0)": "7C", "(2,1)": "AS", "(2,2)": "2D", "(2,3)": "3D", "(2,4)": "4D", "(2,5)": "5D", "(2,6)": "6D", "(2,7)": "7D", "(2,8)": "9H", "(2,9)": "QS",
    "(3,0)": "8C", "(3,1)": "KS", "(3,2)": "6C", "(3,3)": "5C", "(3,4)": "4C", "(3,5)": "3C", "(3,6)": "2C", "(3,7)": "8D", "(3,8)": "8H", "(3,9)": "KS",
    "(4,0)": "9C", "(4,1)": "QS", "(4,2)": "7C", "(4,3)": "6H", "(4,4)": "5H", "(4,5)": "4H", "(4,6)": "AH", "(4,7)": "9D", "(4,8)": "7H", "(4,9)": "AS",
    "(5,0)": "10C", "(5,1)": "10S", "(5,2)": "8C", "(5,3)": "7H", "(5,4)": "2H", "(5,5)": "3H", "(5,6)": "KH", "(5,7)": "10D", "(5,8)": "6H", "(5,9)": "2D",
    "(6,0)": "QC", "(6,1)": "9S", "(6,2)": "9C", "(6,3)": "8H", "(6,4)": "9H", "(6,5)": "10H", "(6,6)": "QH", "(6,7)": "QD", "(6,8)": "5H", "(6,9)": "3D",
    "(7,0)": "KC", "(7,1)": "8S", "(7,2)": "10C", "(7,3)": "QC", "(7,4)": "KC", "(7,5)": "AC", "(7,6)": "AD", "(7,7)": "KD", "(7,8)": "4H", "(7,9)": "4D",
    "(8,0)": "AC", "(8,1)": "7S", "(8,2)": "6S", "(8,3)": "5S", "(8,4)": "4S", "(8,5)": "3S", "(8,6)": "2S", "(8,7)": "2H", "(8,8)": "3H", "(8,9)": "5D",
    "(9,0)": None, "(9,1)": "AD", "(9,2)": "KD", "(9,3)": "QD", "(9,4)": "10D", "(9,5)": "9D", "(9,6)": "8D", "(9,7)": "7D", "(9,8)": "6D", "(9,9)": None
}
# This structure allows you to look up what card (if any) is at a given board position.
# Study: How to represent a 2D board as a dictionary, why use strings for keys.

def build_card_to_positions():
    """
    Build reverse mapping: card -> list of positions on the board
    """
    card_map = {}  # Initialize an empty dictionary to hold the mapping.
    for pos_str, card in boardLayout.items():
        # Loop through each position and card in the boardLayout dictionary.
        pos = tuple(int(x) for x in pos_str.strip("()").split(","))
        # Convert the string key "(r,c)" into a tuple (r, c).
        # Study: String methods (strip, split), tuple construction, generator expressions.
        card_map.setdefault(card, []).append(pos)
        # For each card, append the position to its list in the dictionary.
        # setdefault ensures that if the card isn't already a key, it creates a new list.
        # Study: dict.setdefault(), list methods, grouping data by key.
    return card_map
    # Returns the completed mapping: {card: [(r1,c1), (r2,c2), ...], ...}
    # Study: Function return values, dictionary of lists.

card_to_positions = build_card_to_positions()
# Calls the function to create the reverse mapping and stores it in a variable.
# Now you can look up all positions for a given card.
# Study: Function calls, variable assignment.

# Optional: Check for missing positions (for a 10x10 board)
missing = []
for r in range(10):
    for c in range(10):
        if f"({r},{c})" not in boardLayout:
            missing.append((r, c))
# Loops through all possible positions on a 10x10 board and checks if each is in boardLayout.
# If not, adds it to the missing list.
# Study: Nested for loops, string formatting, membership testing (in), list appending.

if missing:
    print("Warning: Missing positions in boardLayout:", missing)
    # If any positions are missing, print a warning.
    # Study: Conditionals, print statements, debugging board setup.

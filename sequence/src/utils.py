def print_board(board):
    """
    Print the board grid showing tokens and cards.
    Assumes board has:
      - rows, cols
      - get_token(r,c) method
      - is_corner(pos) method
      - position_to_card dict attribute mapping (r,c) -> card string
    """
    header = "    " + " ".join(f"{c:2}" for c in range(board.cols))
    # Builds a header row with column numbers, formatted to width 2.
    # Study: String formatting (f-strings), list comprehensions, join().
    print(header)
    print("   " + "---" * board.cols)
    # Prints a separator line under the header.
    # Study: String multiplication, print().

    for r in range(board.rows):
        row_str = f"{r:2} |"
        # Formats the row number and a separator for each row.
        # Study: f-strings, string formatting.
        for c in range(board.cols):
            pos = (r, c)
            if board.is_corner(pos):
                cell = " * "  # 3 chars for corners
                # Marks corners with an asterisk.
                # Study: Conditional statements, method calls.
            else:
                token = board.get_token(r, c)
                if token is not None:
                    cell = f" {token} " if len(token) == 1 else f"{token:>3}"
                    # Shows the token if present, formatted for width.
                    # Study: String length, conditional expressions (ternary operator).
                else:
                    card = board.position_to_card.get(pos, "  ")
                    cell = f"{card:>3}"
                    # Shows the card code if no token, right-aligned to width 3.
                    # Study: Dictionary get(), string formatting.
            row_str += cell + " "
            # Adds the cell to the row string.
        print(row_str)
        # Prints the completed row.
    print()
    # Adds a blank line after the board.

def prompt_card_choice(hand_cards):
    """
    Prompt for valid card choice.
    Returns the chosen card string.
    """
    while True:
        choice = input(f"Choose a card to play (1-{len(hand_cards)}): ").strip()
        # Prompts the user for input, strips whitespace.
        # Study: input(), string methods, user interaction.
        if choice.isdigit():
            idx = int(choice) - 1
            # Converts input to integer index (1-based to 0-based).
            # Study: Type conversion, indexing.
            if 0 <= idx < len(hand_cards):
                return hand_cards[idx]
                # Returns the selected card if valid.
        print("Invalid choice. Please enter a valid number.")
        # Error message for invalid input.
        # Study: Input validation, loops, error handling.

def prompt_position_choice(possible_positions):
    """
    Prompt player to select a position from a list of possible positions.
    Returns chosen (row, col) tuple.
    """
    print("Possible positions to place token:")
    for i, pos in enumerate(possible_positions):
        print(f"{i+1}: {pos}")
        # Lists all possible positions with numbers for selection.
        # Study: enumerate(), for loops, tuple display.
    while True:
        choice = input(f"Choose a position (1-{len(possible_positions)}): ").strip()
        # Prompts the user for input, strips whitespace.
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(possible_positions):
                return possible_positions[idx]
                # Returns the selected position if valid.
        print("Invalid choice. Please enter a valid position number.")
        # Error message for invalid input.
        # Study: Input validation, loops, error handling.

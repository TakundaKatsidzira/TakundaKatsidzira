import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Adds the parent directory to the Python module search path so imports work.
# Study: sys.path, os.path, module import system, relative imports.

from board import Board
from deck import Deck
from ai import AIPlayer
from mapping import card_to_positions, boardLayout
# Imports classes and variables needed for testing the AI.
# Study: Python imports, modular code, using objects from other files.

def test_ai_choose_valid_move():
    deck = Deck()
    # Creates a new deck of cards for the test.
    ai = AIPlayer("AI", "X", deck)
    # Instantiates an AI player with name "AI", token "X", and the deck.
    board = Board(rows=10, cols=10, position_to_card=boardLayout)
    # Creates a 10x10 game board using the board layout mapping.
    card, pos = ai.choose_move(board, card_to_positions)
    # Asks the AI to choose a move given the current board and card-to-positions mapping.
    assert card is not None and pos is not None
    # Asserts that the AI returns a valid card and position (not None).
    # Study: Object instantiation, method calls, assertions, test-driven development.

def test_ai_move_is_valid():
    deck = Deck()
    ai = AIPlayer("AI", "X", deck)
    board = Board(rows=10, cols=10, position_to_card=boardLayout)
    card, pos = ai.choose_move(board, card_to_positions)
    # The chosen position should be valid for the chosen card
    if card in ("JT", "JO"):
        # For wild cards, just check the move is on the board
        assert isinstance(pos, tuple)
        # Checks that the position is a tuple (row, col).
    else:
        assert pos in card_to_positions.get(card, [])
        # Checks that the position is one of the valid positions for the card.
    # Study: Conditional logic, dictionary access, assertions, AI move validation.

def test_ai_with_empty_hand():
    deck = Deck()
    ai = AIPlayer("AI", "X", deck)
    ai.hand.cards = []  # Force empty hand
    # Empties the AI's hand to simulate no available moves.
    board = Board(rows=10, cols=10, position_to_card=boardLayout)
    result = ai.choose_move(board, card_to_positions)
    assert result is None or (result[0] is None and result[1] is None)
    # Checks that the AI returns None or (None, None) when it has no cards.
    # Study: Edge case testing, handling empty input, AI robustness.

def test_ai_with_no_valid_moves():
    deck = Deck()
    ai = AIPlayer("AI", "X", deck)
    board = Board(rows=10, cols=10, position_to_card=boardLayout)
    # Fill the board so there are no valid moves
    for r in range(board.rows):
        for c in range(board.cols):
            if (r, c) not in board.corners:
                board.grid[r][c] = "O"
    # Fills every non-corner cell with "O" so the AI cannot play.
    result = ai.choose_move(board, card_to_positions)
    assert result is None or (result[0] is None and result[1] is None)
    # Checks that the AI returns None or (None, None) when there are no valid moves.
    # Study: Nested loops, board manipulation, edge case testing.

def test_ai_can_play_as_o():
    deck = Deck()
    ai = AIPlayer("AI", "O", deck)
    # Tests the AI as the "O" player instead of "X".
    board = Board(rows=10, cols=10, position_to_card=boardLayout)
    card, pos = ai.choose_move(board, card_to_positions)
    assert card is not None and pos is not None
    # Checks that the AI can play as either token.
    # Study: Parameterization, AI flexibility, assertions.

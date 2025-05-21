import pytest
# Imports the pytest library for writing and running tests.
# Study: Pytest basics, test discovery, assertion rewriting, exception testing.

from src.player import Player
from src.deck import Deck
# Imports the Player and Deck classes from your source modules.
# Study: Python import system, module structure, OOP class usage.

def test_player_initialization():
    deck = Deck()
    # Instantiates a new Deck object.
    player = Player("Alice", "X", deck)
    # Instantiates a new Player object with name "Alice", token "X", and the deck.
    assert player.name == "Alice"
    # Checks that the player's name is set correctly.
    assert player.token == "X"
    # Checks that the player's token is set correctly.
    assert isinstance(player.hand.cards, list)
    # Checks that the player's hand is a list of cards.
    assert len(player.hand.cards) == 5  # Default hand size
    # Checks that the hand contains 5 cards by default.
    # Study: Object instantiation, attribute access, assertions, default arguments.

def test_player_has_and_play_card():
    deck = Deck()
    player = Player("Bob", "O", deck)
    card = player.get_hand()[0]
    # Gets the first card from the player's hand.
    assert player.has_card(card)
    # Checks that the player has the card in their hand.
    player.play_card(card)
    # Plays (discards) the card and draws a new one.
    assert not player.has_card(card) or card not in player.get_hand()
    # Checks that the card is no longer in the hand after playing.
    # Study: Method calls, state mutation, assertions, logical operators.

def test_show_hand_returns_string():
    deck = Deck()
    player = Player("Carol", "Y", deck)
    hand_str = player.show_hand()
    # Gets the string representation of the player's hand.
    assert isinstance(hand_str, str)
    # Checks that the hand is displayed as a string.
    for card in player.get_hand():
        assert card in hand_str
    # Checks that each card in the hand appears in the string.
    # Study: Special methods (__str__), string containment, for loops.

def test_play_card_invalid_raises():
    deck = Deck()
    player = Player("Dan", "Z", deck)
    invalid_card = "ZZ"
    with pytest.raises(ValueError):
        player.play_card(invalid_card)
    # Tries to play a card not in the hand, expects a ValueError.
    # Study: Exception handling in tests, context managers, error raising.

def test_choose_move_not_implemented():
    deck = Deck()
    player = Player("Eve", "W", deck)
    with pytest.raises(NotImplementedError):
        player.choose_move(None, None)
    # Calls choose_move on the base Player, expects NotImplementedError.
    # Study: Abstract methods, inheritance, exception testing.

def test_has_card_negative():
    deck = Deck()
    player = Player("Frank", "V", deck)
    assert not player.has_card("ZZ")
    # Checks that has_card returns False for a card not in the hand.
    # Study: Negative testing, method return values, assertions.

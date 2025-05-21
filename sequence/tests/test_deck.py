import pytest
# Imports the pytest library for writing and running tests.
# Study: Pytest basics, test discovery, assertion rewriting, exception testing.

from src.deck import Deck, Hand
# Imports the Deck and Hand classes from your deck module.
# Study: Python import system, module structure, OOP class usage.

def test_deck_initialization():
    deck = Deck()
    # Instantiates a new Deck object.
    assert len(deck.cards) > 0
    # Checks that the deck contains cards after initialization.
    # Study: Object instantiation, attribute access, assertions.

def test_deck_shuffle_changes_order():
    deck1 = Deck()
    deck2 = Deck()
    assert deck1.cards != deck2.cards
    # Checks that two decks are shuffled differently (not in the same order).
    # Study: Randomization, object comparison, test for randomness.

def test_draw_card_reduces_count():
    deck = Deck()
    initial = len(deck.cards)
    card = deck.draw()
    assert card is not None
    # Checks that drawing a card returns a card (not None).
    assert len(deck.cards) == initial - 1
    # Checks that the deck size decreases by one after drawing.
    # Study: Method calls, state mutation, assertions.

def test_deck_draw():
    deck = Deck()
    initial_size = deck.size()
    card = deck.draw()
    assert card is not None
    assert deck.size() == initial_size - 1
    # Similar to above, but uses the deck.size() method.
    # Study: Method definitions, encapsulation.

def test_hand_draw_discard():
    deck = Deck()
    hand = Hand(deck)
    old_size = len(hand.cards)
    card = hand.cards[0]
    hand.discard(card)
    assert card not in hand.cards
    # Checks that discarding a card removes it from the hand.
    hand.draw()
    assert len(hand.cards) == old_size
    # Checks that drawing a card restores the hand to its original size.
    # Study: List operations, method calls, state mutation.

def test_draw_from_empty_deck():
    deck = Deck()
    # Draw all cards
    while deck.size() > 0:
        deck.draw()
    assert deck.size() == 0
    assert deck.draw() is None
    # Checks that drawing from an empty deck returns None.
    # Study: Loops, edge case handling, return values.

def test_discard_card_not_in_hand():
    deck = Deck()
    hand = Hand(deck)
    card_not_in_hand = "ZZ"
    # Should not raise error, just do nothing
    hand.discard(card_not_in_hand)
    assert card_not_in_hand not in hand.cards
    # Checks that discarding a card not in hand does not cause errors.
    # Study: Defensive programming, error handling, list membership.

def test_hand_custom_size():
    deck = Deck()
    hand = Hand(deck, size=3)
    assert len(hand.cards) == 3
    # Checks that a hand can be initialized with a custom size.
    # Study: Constructor arguments, default values, object instantiation.

def test_deck_size_matches_cards():
    deck = Deck()
    assert deck.size() == len(deck.cards)
    deck.draw()
    assert deck.size() == len(deck.cards)
    # Checks that the deck.size() method always matches the actual number of cards.
    # Study: Consistency checks, encapsulation, method correctness.

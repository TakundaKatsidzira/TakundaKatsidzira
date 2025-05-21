import random
# Imports Python's built-in random module for shuffling and drawing cards.
# Study: Python standard library, random.shuffle, randomization in games.

class Deck:
    """Represents a deck of Sequence cards."""
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Q', 'K', 'A']
        suits = ['C', 'D', 'H', 'S']
        # Defines the possible ranks and suits for cards.
        # Study: Lists, string formatting, combinatorics.

        # Add all cards except Jacks
        self.cards = [f"{rank}{suit}" for rank in ranks for suit in suits]
        # Creates a list of all cards (except Jacks) using a list comprehension.
        # Study: List comprehensions, nested loops, string interpolation.

        # Add 2 JT and 2 JO (total 4 Jacks, as required)
        self.cards += ['JT'] * 2  # Two "One-eyed Jacks"
        self.cards += ['JO'] * 2  # Two "Two-eyed Jacks"
        # Adds special Jack cards to the deck.
        # Study: List addition, list multiplication.

        random.shuffle(self.cards)
        # Shuffles the deck in place.
        # Study: random.shuffle, in-place operations.

    def draw(self):
        """Draw a card from the deck."""
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
        # Removes and returns the last card in the list (deck).
        # Study: List methods (pop), return values, handling empty lists.

    def size(self):
        """Return the number of cards left in the deck."""
        return len(self.cards)
        # Returns the number of cards remaining.
        # Study: len() function, method definitions.

class Hand:
    """Represents a player's hand."""
    def __init__(self, deck, size=5):
        self.cards = []
        self.deck = deck
        for _ in range(size):
            self.draw()
        # Initializes the hand by drawing 'size' cards from the deck.
        # Study: Object composition (Hand has a Deck), for loops, method calls.

    def draw(self):
        """Draw a card from the deck into the hand."""
        card = self.deck.draw()
        if card:
            self.cards.append(card)
        # Draws a card from the deck and adds it to the hand if not None.
        # Study: Method calls, conditional statements, list appending.

    def discard(self, card):
        """Remove a card from the hand."""
        if card in self.cards:
            self.cards.remove(card)
        # else:  # Optionally, raise an error if card not in hand
        #     raise ValueError(f"Card {card} not in hand.")
        # Removes the specified card from the hand if present.
        # Study: List membership, list removal, error handling (optional).

    def has_card(self, card):
        """Check if the hand contains a card."""
        return card in self.cards
        # Returns True if the card is in the hand.
        # Study: Membership testing (in), boolean return.

    def __str__(self):
        return ", ".join(self.cards)
        # Returns a string representation of the hand (comma-separated cards).
        # Study: Special methods (__str__), string joining, list to string conversion.

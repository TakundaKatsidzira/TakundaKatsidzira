import random

def generate_deck():
    """Generate a standard Sequence deck of cards (excluding jokers)."""
    suits = ['H', 'D', 'C', 'S']
    ranks = [str(x) for x in range(2,11)] + ['J', 'Q', 'K', 'A']
    deck = [rank + suit for suit in suits for rank in ranks] * 2  # 2 decks usually
    random.shuffle(deck)
    return deck

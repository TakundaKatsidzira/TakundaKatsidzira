from deck import Hand
# Imports the Hand class from your deck module.
# Study: Python import system, modules, packages, class usage.

class Player:
    # Defines a Player class, representing a Sequence game player.
    # Study: Object-Oriented Programming (OOP), class definitions, encapsulation.

    def __init__(self, name, token, deck):
        self.name = name
        # Stores the player's name as an instance attribute.
        self.token = token
        # Stores the player's token (e.g., color or symbol) as an instance attribute.
        self.hand = Hand(deck)  # Each player gets their own Hand from their own Deck
        # Creates a Hand object for the player, drawing cards from the provided deck.
        # Study: Object composition (Player "has a" Hand), constructor (__init__), passing objects as arguments.

    def get_hand(self):
        return self.hand.cards
        # Returns the list of cards in the player's hand.
        # Study: Attribute access, method definitions, returning values.

    def show_hand(self):
        return str(self.hand)
        # Returns a string representation of the player's hand (uses Hand's __str__).
        # Study: Special methods (__str__), string conversion, delegation.

    def play_card(self, card):
        if not self.has_card(card):
            raise ValueError(f"Card {card} not in hand.")
        self.hand.discard(card)
        self.hand.draw()  # Draw from this player's own deck
        # Draws a new card from the deck to replace the played card.
        # Study: Method calls, object interaction, game mechanics.

    def choose_move(self, board, card_to_positions):
        """
        To be implemented in subclasses (Human, AI).
        Returns (card, position)
        """
        raise NotImplementedError
        # This method is meant to be overridden by subclasses (e.g., HumanPlayer, AIPlayer).
        # If called directly, it raises an error.
        # Study: Inheritance, abstract methods, exceptions, polymorphism.

    def has_card(self, card):
        return card in self.hand.cards
        # Checks if the player's hand contains the specified card.
        # Study: Membership testing, method definition.

from board import Board
from deck import Deck
from player import Player
from ai import AIPlayer
from mapping import boardLayout
from logger import log_turn, log_game_start, log_game_end
from utils import print_board, prompt_card_choice, prompt_position_choice
import sys

def map_cards_to_positions(boardLayout):
    """
    Create two mappings:
    - card_to_positions: {card: [(r,c), ...]}
    - position_to_card: {(r,c): card}
    """
    card_to_positions = {}
    position_to_card = {}
    for pos_str, card in boardLayout.items():
        r, c = eval(pos_str)
        position_to_card[(r,c)] = card
        card_to_positions.setdefault(card, []).append((r,c))
    return card_to_positions, position_to_card

def main():
    print("Welcome to Sequence CLI!")
    mode = input("Play mode? (h)uman vs (c)omputer: ").strip().lower()
    if mode not in ('h','c'):
        print("Invalid mode. Exiting.")
        sys.exit(1)

    card_to_positions, position_to_card = map_cards_to_positions(boardLayout)

    # Initialize board with mapping
    board = Board(rows=10, cols=10, position_to_card=position_to_card)

    # Initialize separate decks for each player
    deck1 = Deck()
    deck2 = Deck()
    player1 = Player("Human", "X", deck1)
    player2 = AIPlayer("Computer", "O", deck2)
    players = [player1, player2]

    log_game_start(players)

    current_player_idx = 0
    winner = None

    while True:
        player = players[current_player_idx]
        print_board(board)
        # Calls a utility function to print the current board state.
        # Study: Function calls, board visualization, user interface.

        if isinstance(player, AIPlayer):
            print(f"{player.name}'s turn.")  # Do NOT show AI hand
            # Checks if the current player is an AIPlayer (using isinstance).
            # Study: Type checking, class inheritance, polymorphism.
        else:
            # Show human hand with available slots for each card
            hand_cards = player.get_hand()
            hand_display = []
            print(f"{player.name}'s turn. Your hand:")
            for idx, card in enumerate(hand_cards, 1):
                # Loops through each card in the player's hand, showing possible moves.
                # Study: for loops, enumerate, list indexing.
                if card == 'JO':
                    opponent_tokens = [(r, c) for r in range(board.rows) for c in range(board.cols)
                                       if board.get_token(r, c) == players[1-current_player_idx].token]
                    if opponent_tokens:
                        slots_str = ', '.join(str(pos) for pos in opponent_tokens)
                        print(f"{idx}: {card} {slots_str}")
                    else:
                        print(f"{idx}: {card} NONE")
                    # Study: List comprehensions, string joining, conditional logic.
                elif card == 'JT':
                    print(f"{idx}: {card} ALL OPEN!")
                    # JT is a wild card, can be played anywhere open.
                else:
                    positions = card_to_positions.get(card, [])
                    if positions:
                        slots_str = ', '.join(str(pos) for pos in positions)
                        print(f"{idx}: {card} {slots_str}")
                    else:
                        print(f"{idx}: {card}")
                # Study: Dictionary access, handling missing keys, string formatting.

        # Get move
        if isinstance(player, AIPlayer):
            card, pos = player.choose_move(board, card_to_positions)
            # Calls the AI's move selection method.
            # Study: AI algorithms, method overriding, polymorphism.
            if card is None or pos is None:
                print(f"{player.name} has no valid moves. Skipping turn.")
                current_player_idx = 1 - current_player_idx
                continue
            print(f"{player.name} plays {card} at {pos}.")
        else:
            # Human turn
            while True:
                card = prompt_card_choice(player.get_hand())
                # Prompts the user to choose a card from their hand.
                # Study: User input, function calls, input validation.
                # Valid positions for this card
                if card == 'JO':
                    # Can remove any opponent token
                    possible_positions = [(r,c) for r in range(board.rows) for c in range(board.cols)
                                          if board.get_token(r,c) == players[1-current_player_idx].token]
                    if not possible_positions:
                        print("No opponent tokens to remove. Choose a different card.")
                        continue
                elif card == 'JT':
                    possible_positions = [(r,c) for r in range(board.rows) for c in range(board.cols)
                                          if not board.is_corner((r,c)) and board.is_empty((r,c))]
                else:
                    positions = card_to_positions.get(card, [])
                    possible_positions = [pos for pos in positions if board.is_empty(pos)]

                if not possible_positions:
                    print("No valid positions to place/remove token for that card. Choose another card.")
                    continue

                pos = prompt_position_choice(possible_positions)
                # Prompts the user to choose a position from the valid options.
                # Study: User input, list filtering, function calls.
                break

        # Apply move
        try:
            if card == 'JO':
                board.remove_token(pos, players[1-current_player_idx].token)
                # Removes an opponent's token from the board.
                # Study: Method calls, board manipulation, exception handling.
            else:
                board.place_token(pos, player.token)
            # Places the player's token on the board.
                player.play_card(card)
            # Removes the played card from the hand and draws a new one.
            # Study: Object interaction, method calls, game state update.
        except ValueError as e:
            print(f"Invalid move: {e}")
            if not isinstance(player, AIPlayer):
                continue  # let human retry
            else:
                # AI error fallback - skip turn
                print(f"{player.name} move failed, skipping turn.")
            current_player_idx = 1 - current_player_idx
            continue
            # Study: Exception handling, error messages, control flow.

    # Log turn
        log_turn({
            "player": player.name,
            "card": card,
            "position": pos,
            "hand": player.get_hand(),
            "board_state": [[board.get_token(r,c) for c in range(board.cols)] for r in range(board.rows)]
        })
        # Logs the move for later analysis or debugging.
        # Study: Logging, dictionary construction, nested list comprehensions.

        # Check for winner
        if board.check_sequence(player.token):
            winner = player.name
            break
        # Checks if the current player has formed a winning sequence.
        # Study: Game logic, win detection, breaking out of loops.

        current_player_idx = 1 - current_player_idx
        # Switches to the other player (0 <-> 1).
        # Study: Index arithmetic, turn alternation.

    print_board(board)
    print(f"Game Over! Winner is {winner}")
    log_game_end(winner)
    # Prints the final board, announces the winner, and logs the game end.
    # Study: Output, logging, function calls.

if __name__ == "__main__":
    main()
# Standard Python idiom: only run main() if this script is executed directly, not imported.
# Study: Script entry points, __name__ variable, program structure.

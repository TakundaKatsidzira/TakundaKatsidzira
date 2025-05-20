from board import Board
from player import Player
from cpu_agent import CPUAgent

class Game:
    def __init__(self, players):
        self.board = Board()
        self.players = {p.player_id: p for p in players}
        self.turn_order = list(self.players.keys())
        self.current_turn_index = 0
        self.winner = None
        self.cpu_agents = {
            p.player_id: CPUAgent(p.player_id) for p in players if p.is_cpu
        }

    def current_player(self):
        return self.players[self.turn_order[self.current_turn_index]]

    def next_turn(self):
        self.current_turn_index = (self.current_turn_index + 1) % len(self.turn_order)

    def play_turn(self):
        player = self.current_player()
        print(f"\nIt's {player.name}'s turn!")

        if player.is_cpu:
            cpu = self.cpu_agents[player.player_id]
            move = cpu.select_move(self)
            if move is None:
                print("No moves available for CPU.")
                self.next_turn()
                return
            r, c = move
            print(f"CPU {player.name} places token at ({r},{c})")
            self.board.place_token(r, c, player.player_id)
        else:
            # Human player input
            while True:
                try:
                    raw = input("Enter row,col to place token (0-based, e.g. 3,4): ")
                    r, c = map(int, raw.split(','))
                    if not self.board.is_valid_position(r, c):
                        print("Invalid position. Try again.")
                        continue
                    if self.board.grid[r][c] is not None:
                        print("Position already occupied. Try again.")
                        continue
                    self.board.place_token(r, c, player.player_id)
                    break
                except Exception as e:
                    print("Invalid input. Try again.")

        # Check for win
        if self.board.check_sequence_from(r, c):
            self.winner = player
            print(f"Player {player.name} wins!")

        self.next_turn()

    def is_over(self):
        return self.winner is not None

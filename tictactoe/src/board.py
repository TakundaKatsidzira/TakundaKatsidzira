# board.py

WIN_MASKS = [
    0b111000000,  # Row 1
    0b000111000,  # Row 2
    0b000000111,  # Row 3
    0b100100100,  # Col 1
    0b010010010,  # Col 2
    0b001001001,  # Col 3
    0b100010001,  # Diag 1
    0b001010100   # Diag 2
]

class Board:
    def __init__(self):
        self.x_mask = 0  # X player positions
        self.o_mask = 0  # O player positions
        self.move_sequence = []  # list of all moves made
        self.current_player = 'X'  # X starts

    def get_bitmask(self, player):
        return self.x_mask if player == 'X' else self.o_mask

    def set_bitmask(self, player, new_mask):
        if player == 'X':
            self.x_mask = new_mask
        else:
            self.o_mask = new_mask

    def make_move(self, index):
        if not self.is_valid_move(index):
            raise ValueError(f"Invalid move at index {index}")
        bit = 1 << index
        mask = self.get_bitmask(self.current_player)
        self.set_bitmask(self.current_player, mask | bit)
        self.move_sequence.append(index)
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def undo_move(self, index):
        bit = ~(1 << index)
        last_player = 'O' if self.current_player == 'X' else 'X'
        mask = self.get_bitmask(last_player)
        self.set_bitmask(last_player, mask & bit)
        self.move_sequence.pop()
        self.current_player = last_player

    def is_valid_move(self, index):
        occupied = self.x_mask | self.o_mask
        return (occupied & (1 << index)) == 0

    def available_moves(self):
        return [i for i in range(9) if self.is_valid_move(i)]

    def check_winner(self):
        for mask in WIN_MASKS:
            if (self.x_mask & mask) == mask:
                return 'X'
            if (self.o_mask & mask) == mask:
                return 'O'
        return None

    def is_draw(self):
        return len(self.move_sequence) == 9 and self.check_winner() is None

    def is_terminal(self):
        return self.check_winner() is not None or self.is_draw()

    def copy(self):
        new_board = Board()
        new_board.x_mask = self.x_mask
        new_board.o_mask = self.o_mask
        new_board.move_sequence = self.move_sequence.copy()
        new_board.current_player = self.current_player
        return new_board

    def get_state_key(self):
        return (self.x_mask, self.o_mask, self.current_player == 'X')

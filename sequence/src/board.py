from collections import defaultdict

class Board:
    ROWS = 10
    COLS = 10
    SEQUENCE_LENGTH = 5

    def __init__(self):
        # Board represented as a 2D list of None or player tokens
        self.grid = [[None for _ in range(Board.COLS)] for _ in range(Board.ROWS)]
        # Map from card to positions on the board (many cards appear multiple times)
        self.card_positions = self._generate_card_positions()
        # Precompute directions for sequence checking
        self.directions = [(1,0), (0,1), (1,1), (1,-1)]

    def _generate_card_positions(self):
        # Normally Sequence board cards layout:
        # Here simplified: cards are strings, with multiple positions per card
        # TODO: Replace with actual board mapping from cards to positions
        return defaultdict(list)

    def place_token(self, row, col, player_id):
        if self.grid[row][col] is not None:
            raise ValueError("Cell already occupied")
        self.grid[row][col] = player_id

    def remove_token(self, row, col):
        self.grid[row][col] = None

    def is_valid_position(self, row, col):
        return 0 <= row < Board.ROWS and 0 <= col < Board.COLS

    def check_sequence_from(self, row, col):
        """Check if placing a token at (row,col) forms a sequence of SEQUENCE_LENGTH"""
        player_id = self.grid[row][col]
        if player_id is None:
            return False

        for dr, dc in self.directions:
            count = 1
            # Check forward direction
            r, c = row + dr, col + dc
            while self.is_valid_position(r, c) and self.grid[r][c] == player_id:
                count += 1
                r += dr
                c += dc
            # Check backward direction
            r, c = row - dr, col - dc
            while self.is_valid_position(r, c) and self.grid[r][c] == player_id:
                count += 1
                r -= dr
                c -= dc

            if count >= Board.SEQUENCE_LENGTH:
                return True
        return False

    def find_all_sequences(self, player_id):
        """Return list of sequences (list of cells) of length SEQUENCE_LENGTH for player_id"""
        sequences = []
        visited = set()
        for r in range(Board.ROWS):
            for c in range(Board.COLS):
                if self.grid[r][c] == player_id:
                    for dr, dc in self.directions:
                        seq_cells = []
                        rr, cc = r, c
                        while (self.is_valid_position(rr, cc) and
                               self.grid[rr][cc] == player_id and
                               len(seq_cells) < Board.SEQUENCE_LENGTH):
                            seq_cells.append((rr, cc))
                            rr += dr
                            cc += dc
                        if len(seq_cells) == Board.SEQUENCE_LENGTH:
                            seq_tuple = tuple(seq_cells)
                            if seq_tuple not in visited:
                                sequences.append(seq_cells)
                                visited.add(seq_tuple)
        return sequences

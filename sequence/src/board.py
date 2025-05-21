class Board:
    def __init__(self, rows=10, cols=10, position_to_card=None):
        """Initialize the board."""
        self.rows = rows  # Number of rows in the board.
        self.cols = cols  # Number of columns in the board.
        self.corners = [(0,0), (0,9), (9,0), (9,9)]  # List of corner positions (special in Sequence).
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        # 2D list (list of lists) representing the board grid; each cell is None or a token.
        self.position_to_card = position_to_card if position_to_card else {}
        # Optional mapping from positions to card codes.
        # Study: __init__ method, instance variables, default arguments, list comprehensions, OOP basics.

    def is_corner(self, pos):
        """Check if a position is a corner."""
        return pos in self.corners
        # Returns True if the position is one of the four corners.
        # Study: Membership testing (in), tuples, method definitions.

    def is_empty(self, pos):
        """Check if a position is empty (not a corner and not occupied)."""
        r, c = pos
        if self.is_corner(pos):
            return False
        return self.grid[r][c] is None
        # Checks if a cell is not a corner and is unoccupied.
        # Study: Tuple unpacking, list indexing, boolean logic.

    def place_token(self, pos, token):
        """Place a token at a position."""
        r, c = pos
        if self.is_corner(pos):
            raise ValueError("Cannot place token on corner spots")
        if self.grid[r][c] is not None:
            raise ValueError("Position already occupied")
        self.grid[r][c] = token
        # Places a token at the specified position if valid.
        # Study: Exception handling (raise), error messages, list assignment.

    def remove_token(self, pos, opponent_token):
        """Remove an opponent's token from a position."""
        r, c = pos
        if self.is_corner(pos):
            raise ValueError("Cannot remove tokens from corners")
        if self.grid[r][c] != opponent_token:
            raise ValueError("No opponent token at this position")
        self.grid[r][c] = None
        # Removes a token if it matches the opponent's and is not a corner.
        # Study: Defensive programming, equality checks, error handling.

    def get_token(self, r, c):
        """Get the token at a specific position."""
        return self.grid[r][c]
        # Returns the token at the given row and column.
        # Study: Method parameters, list indexing.

    def check_sequence(self, token, length=5):
        """Check if a sequence of the given length exists for the token."""
        directions = [(0,1), (1,0), (1,1), (1,-1)]
        # Directions: right, down, diagonal down-right, diagonal down-left.
        for r in range(self.rows):
            for c in range(self.cols):
                for dr, dc in directions:
                    if self._check_line(r, c, dr, dc, token, length):
                        return True
        return False
        # Checks every possible starting point and direction for a sequence of the given length.
        # Study: Nested loops, range(), tuple unpacking, method calls, early return.

    def _check_line(self, r, c, dr, dc, token, length):
        """Check a line in a given direction for a sequence."""
        count = 0
        for i in range(length):
            rr = r + dr*i
            cc = c + dc*i
            if not (0 <= rr < self.rows and 0 <= cc < self.cols):
                return False
            if (rr, cc) in self.corners:
                count += 1
            elif self.grid[rr][cc] == token:
                count += 1
            else:
                return False
        return count == length
        # Checks if a line of the given length from (r, c) in direction (dr, dc) is all the player's tokens or corners.
        # Study: Index arithmetic, bounds checking, nested logic, for loops, return values.

    def copy(self):
        """Return a copy of the board."""
        new_board = Board(self.rows, self.cols, self.position_to_card)
        for r in range(self.rows):
            for c in range(self.cols):
                new_board.grid[r][c] = self.grid[r][c]
        return new_board
        # Creates a deep copy of the board (new object with the same grid and mapping).
        # Study: Object copying, for loops, deep vs shallow copy, method return.

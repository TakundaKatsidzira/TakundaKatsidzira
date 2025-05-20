import random

class CPUAgent:
    def __init__(self, player_id, difficulty='medium'):
        self.player_id = player_id
        self.difficulty = difficulty

    def select_move(self, game):
        """Return (row, col) to place token.
        Mix strategy and randomness based on difficulty.
        """

        board = game.board
        opponent_ids = [pid for pid in game.players if pid != self.player_id]

        # Very basic strategy:
        # 1) Try to complete own sequence if possible
        # 2) Block opponent's sequences
        # 3) Else pick random valid move

        # 1) Try to place token to create or complete a sequence
        for r in range(board.ROWS):
            for c in range(board.COLS):
                if board.grid[r][c] is None:
                    board.place_token(r, c, self.player_id)
                    if board.check_sequence_from(r, c):
                        board.remove_token(r, c)
                        return (r, c)
                    board.remove_token(r, c)

        # 2) Block opponent's sequences
        for opp in opponent_ids:
            for r in range(board.ROWS):
                for c in range(board.COLS):
                    if board.grid[r][c] is None:
                        board.place_token(r, c, opp)
                        if board.check_sequence_from(r, c):
                            board.remove_token(r, c)
                            return (r, c)  # block here
                        board.remove_token(r, c)

        # 3) Random move
        empty_cells = [(r,c) for r in range(board.ROWS) for c in range(board.COLS) if board.grid[r][c] is None]
        if not empty_cells:
            return None  # No moves left
        return random.choice(empty_cells)

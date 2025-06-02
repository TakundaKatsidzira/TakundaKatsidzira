import unittest
from src.agents import RandomAgent, RulesAgent, MinimaxAgent
# from src.agents import ForkAgent  # Uncomment if ForkAgent is active
from src.board import Board

def play_game(agent1, agent2):
    board = Board()
    agents = {'X': agent1, 'O': agent2}
    while not board.is_terminal():
        current_agent = agents[board.current_player]
        move = current_agent.select_move(board)
        board.make_move(move)
    return board.check_winner()

class TestAgentsExtended(unittest.TestCase):

    def test_random_agent_never_chooses_invalid_move(self):
        board = Board()
        board.make_move(0)
        board.make_move(1)
        agent = RandomAgent()
        for _ in range(20):  # multiple attempts to catch rare invalid
            move = agent.select_move(board)
            self.assertIn(move, board.available_moves())

    def test_rules_agent_prioritizes_center(self):
        board = Board()
        board.make_move(0)  # X
        agent = RulesAgent()
        move = agent.select_move(board)
        self.assertEqual(move, 4)

    def test_rules_agent_blocks_win(self):
        board = Board()
        board.make_move(0)  # X
        board.make_move(3)  # O
        board.make_move(1)  # X
        agent = RulesAgent()
        move = agent.select_move(board)
        self.assertEqual(move, 2)

    def test_rules_agent_wins_if_possible(self):
        board = Board()
        board.make_move(0)  # X
        board.make_move(3)  # O
        board.make_move(1)  # X
        board.make_move(4)  # O
        agent = RulesAgent()
        move = agent.select_move(board)
        self.assertEqual(move, 2)

    # def test_minimax_blocks_fork_threat(self):
    #    board = Board()
    #    board.make_move(0)  # X
    #    board.make_move(4)  # O
    #    board.make_move(2)  # X
    #    board.make_move(6)  # O
    #    agent = MinimaxAgent()
    #    move = agent.select_move(board)
    #    self.assertIn(move, board.available_moves())  # No crash

    def test_minimax_versus_random(self):
        wins = {'X': 0, 'O': 0, 'Draw': 0}
        for _ in range(50):
            result = play_game(MinimaxAgent(), RandomAgent())
            wins[result or 'Draw'] += 1
        self.assertGreater(wins['X'] + wins['O'], wins['Draw'])

    def test_rules_versus_random(self):
        wins = {'X': 0, 'O': 0, 'Draw': 0}
        for _ in range(50):
            result = play_game(RulesAgent(), RandomAgent())
            wins[result or 'Draw'] += 1
        self.assertGreater(wins['X'] + wins['O'], wins['Draw'])

    def test_minimax_draws_itself(self):
        draws = 0
        for _ in range(10):
            result = play_game(MinimaxAgent(), MinimaxAgent())
            if result is None:
                draws += 1
        self.assertEqual(draws, 10)

    # def test_fork_agent_creates_fork(self):
    #     board = Board()
    #     board.make_move(0)  # X
    #     board.make_move(4)  # O
    #     board.make_move(8)  # X
    #     # Now O should fork with 2 or 6
    #     agent = ForkAgent()
    #     move = agent.select_move(board)
    #     self.assertIn(move, [2, 6])

if __name__ == '__main__':
    unittest.main()

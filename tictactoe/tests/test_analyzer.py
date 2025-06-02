import unittest
from unittest.mock import patch, mock_open
from src import analyzer
from src.analyzer import parse_list, analyze_games, read_csv
import io
import builtins

SAMPLE_CSV = """game_id,is_draw,winner,first_player,first_move,last_move,X_move_sequence,O_move_sequence,game_move_sequence,num_moves_X,num_moves_O,win_method,agent_X_type,agent_O_type,agent_X_time,agent_O_time,game_time
1,False,X,X,0,8,"[0, 4, 8]","[1, 2]","[0, 1, 4, 2, 8]",3,2,diag1,MinimaxAgent,RandomAgent,0.123456,0.345678,0.469134
2,True,Draw,O,4,6,"[2, 6, 7]","[4, 0, 3]","[4, 2, 0, 6, 3, 7]",3,3,None,RandomAgent,MinimaxAgent,0.111111,0.222222,0.333333
3,False,O,X,1,5,"[1, 3, 5]","[0, 4, 8]","[1, 0, 3, 4, 5, 8]",3,3,row2,MinimaxAgent,RulesAgent,0.100000,0.200000,0.300000
"""

class TestAnalyzer(unittest.TestCase):
    def test_parse_list_valid(self):
        self.assertEqual(parse_list("[1, 2, 3]"), [1, 2, 3])

    def test_parse_list_invalid(self):
        self.assertEqual(parse_list("invalid"), [])

    @patch('analyzer.open', new_callable=mock_open, read_data=SAMPLE_CSV)
    def test_read_csv_parses_data(self, mock_file):
        data = read_csv("dummy_path.csv")
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['winner'], 'X')
        self.assertEqual(data[1]['is_draw'], 'True')

    @patch('analyzer.open', new_callable=mock_open, read_data=SAMPLE_CSV)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_analyze_games_output(self, mock_stdout, mock_file):
        analyze_games("dummy_path.csv")
        output = mock_stdout.getvalue()
        self.assertIn("📊 Total games analyzed: 3", output)
        self.assertIn("X: 2 times", output)
        self.assertIn("O: 1 times", output)
        self.assertIn("MinimaxAgent vs RandomAgent", output)

if __name__ == "__main__":
    unittest.main()

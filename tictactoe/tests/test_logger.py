import unittest
import os
import tempfile
import csv
from src import logger 
from src.logger import init_log, reset_log, log_game, CSV_FIELDS

class TestLogger(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and override LOG_PATH
        self.temp_dir = tempfile.TemporaryDirectory()
        self.log_path = os.path.join(self.temp_dir.name, "games_log.csv")
        self.patcher = unittest.mock.patch('logger.LOG_PATH', self.log_path)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()
        self.temp_dir.cleanup()

    def test_init_log_creates_file_with_headers(self):
        init_log()
        self.assertTrue(os.path.exists(self.log_path))
        with open(self.log_path, newline='') as f:
            reader = csv.reader(f)
            headers = next(reader)
            self.assertEqual(headers, CSV_FIELDS)

    def test_reset_log_empties_file_but_keeps_headers(self):
        init_log()
        with open(self.log_path, 'a', newline='') as f:
            f.write("dummy\n")
        reset_log()
        with open(self.log_path, newline='') as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 1)
        self.assertIn("game_id", lines[0])

    def test_log_game_appends_row(self):
        init_log()
        example_game = {
            "game_id": 1,
            "is_draw": False,
            "winner": "X",
            "first_player": "X",
            "first_move": 0,
            "last_move": 6,
            "X_move_sequence": [0, 4, 8],
            "O_move_sequence": [1, 2],
            "game_move_sequence": [0, 1, 4, 2, 8, 6],
            "num_moves_X": 3,
            "num_moves_O": 2,
            "win_method": "diag1",
            "agent_X_type": "MinimaxAgent",
            "agent_O_type": "RandomAgent",
            "agent_X_time": 0.123456,
            "agent_O_time": 0.345678,
            "game_time": 0.469134
        }
        log_game(example_game)
        with open(self.log_path, newline='') as f:
            rows = list(csv.DictReader(f))
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['winner'], 'X')
        self.assertEqual(rows[0]['X_move_sequence'], '0,4,8')

if __name__ == '__main__':
    unittest.main()

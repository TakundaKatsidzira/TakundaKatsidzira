import unittest
from src.explorer import Explorer

class TestExplorer(unittest.TestCase):
    def setUp(self):
        self.explorer = Explorer()

    def test_lc_command(self):
        # Ensure we can get the current working directory
        result = self.explorer.cmd_handler.execute(['lc'])
        self.assertIsInstance(result, str)
        self.assertIn('/', result)

    def test_create_and_list(self):
        self.explorer.cmd_handler.execute(['cr', 'test_file'])
        result = self.explorer.cmd_handler.execute(['ls'])
        self.assertIn('test_file', result)

    def test_change_directory_invalid(self):
        result = self.explorer.cmd_handler.execute(['cd', 'nonexistent'])
        self.assertIn('Invalid directory', result)


    def test_help_command(self):
        result = self.explorer.cmd_handler.execute(['hp'])
        self.assertIn('cr: Create a file or directory', result)


    def test_unknown_command(self):
        result = self.explorer.cmd_handler.execute(['unknowncmd'])
        self.assertIn('Unknown command', result)

if __name__ == '__main__':
    unittest.main()

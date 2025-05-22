# tests/test_crawly.py
import unittest
import subprocess

class TestCrawlyCLI(unittest.TestCase):
    def test_crawly_cli_help(self):
        result = subprocess.run(
            ["python3", "src/crawly.py", "--help"],
            capture_output=True,
            text=True
        )
        self.assertIn("usage", result.stdout)

if __name__ == '__main__':
    unittest.main()

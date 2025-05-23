import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the system path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.crawly import main

class TestCrawly(unittest.TestCase):
    @patch("builtins.print")
    @patch("src.graph_builder.requests.get")
    def test_crawly_flow(self, mock_get, mock_print):
        root_url = "https://example.com/root.txt"
        test_args = ["crawly.py", root_url, "--verbose"]

        # Mock responses
        mock_root_response = MagicMock()
        mock_root_response.status_code = 200
        mock_root_response.text = "page1.txt\npage2.txt"

        mock_child_response = MagicMock()
        mock_child_response.status_code = 200
        mock_child_response.text = ""

        def get_side_effect(url, timeout=5):
            if url == root_url:
                return mock_root_response
            return mock_child_response

        mock_get.side_effect = get_side_effect

        with patch.object(sys, 'argv', test_args):
            main()

        mock_print.assert_any_call(f"[INFO] Starting crawl at: {root_url}")
        mock_print.assert_any_call("[INFO] Graph built: 3 nodes, 0 dead links")
        mock_print.assert_any_call(f"[INFO] Report saved to: data/analysis_report.txt")

if __name__ == '__main__':
    unittest.main()

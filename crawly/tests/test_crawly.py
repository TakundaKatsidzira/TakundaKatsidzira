import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the system path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.crawly import main

class TestCrawlyMain(unittest.TestCase):
    @patch("builtins.print")
    @patch("src.graph_builder.requests.get")
    @patch("src.analyzer.requests.head")
    def test_main_flow(self, mock_head, mock_get, mock_print):
        # Mock root file
        root_url = "https://example.com/root.txt"
        test_args = ["crawly.py", root_url, "--verbose"]

        # Simulate root.txt returning two child links
        mock_root_response = MagicMock()
        mock_root_response.status_code = 200
        mock_root_response.text = "page1.txt\npage2.txt"
        
        # Simulate child pages returning no further links
        mock_child_response = MagicMock()
        mock_child_response.status_code = 200
        mock_child_response.text = ""

        def get_side_effect(url, timeout=5):
            if url == root_url:
                return mock_root_response
            return mock_child_response

        mock_get.side_effect = get_side_effect

        # Simulate all HEAD requests for file sizes
        mock_head_response = MagicMock()
        mock_head_response.status_code = 200
        mock_head_response.headers = {'Content-Length': '1234'}
        mock_head.return_value = mock_head_response

        with patch.object(sys, 'argv', test_args):
            main()

        # Verify output printed
        mock_print.assert_any_call(f"[INFO] Starting crawl at: {root_url}")
        mock_print.assert_any_call("[INFO] Graph built with 3 nodes")
        mock_print.assert_any_call(f"[INFO] Report saved to data/analysis_report.txt")

if __name__ == '__main__':
    unittest.main()

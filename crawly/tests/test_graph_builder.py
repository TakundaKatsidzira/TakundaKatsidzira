import unittest
from unittest.mock import patch, Mock
from src.graph_builder import GraphBuilder

class TestGraphBuilder(unittest.TestCase):
    @patch("requests.get")
    def test_build_graph_single_node(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = ""

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/root.txt")

        self.assertEqual(len(graph), 1)
        self.assertEqual(graph["https://test.com/root.txt"], [])
        self.assertEqual(len(dead_links), 0)

    @patch("requests.get")
    def test_dead_link_detection(self, mock_get):
        mock_get.side_effect = Exception("404 Not Found")

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/broken.txt")

        self.assertEqual(len(graph), 0)
        self.assertIn("https://test.com/broken.txt", dead_links)

    @patch("requests.get")
    def test_multiple_links_in_file(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "https://test.com/page1.txt\nhttps://test.com/page2.txt"
        mock_get.return_value = mock_response

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/root.txt")

        self.assertIn("https://test.com/root.txt", graph)
        self.assertEqual(graph["https://test.com/root.txt"], [
            "https://test.com/page1.txt", "https://test.com/page2.txt"])
        self.assertEqual(len(dead_links), 0)

    @patch("requests.get")
    def test_ignores_empty_lines_and_comments(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "\n# Comment\nhttps://test.com/page.txt\n\n"
        mock_get.return_value = mock_response

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/root.txt")

        self.assertEqual(len(graph["https://test.com/root.txt"]), 1)
        self.assertEqual(graph["https://test.com/root.txt"][0], "https://test.com/page.txt")

if __name__ == '__main__':
    unittest.main()

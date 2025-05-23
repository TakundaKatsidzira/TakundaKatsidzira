import unittest
from unittest.mock import patch, Mock
from src.graph_builder import GraphBuilder
from src.page_node import PageNode

class TestGraphBuilder(unittest.TestCase):
    @patch("requests.get")
    def test_build_graph_single_node(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = ""
        mock_response.content = b""
        mock_get.return_value = mock_response

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/root.txt")

        self.assertEqual(len(graph), 1)
        self.assertIsInstance(graph["https://test.com/root.txt"], PageNode)
        self.assertEqual(len(graph["https://test.com/root.txt"].children), 0)
        self.assertEqual(len(dead_links), 0)

    @patch("requests.get")
    def test_dead_link_detection(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.content = b""
        mock_get.return_value = mock_response

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/broken.txt")

        self.assertEqual(len(graph), 1)
        self.assertIn("https://test.com/broken.txt", dead_links)

    @patch("requests.get")
    def test_multiple_links_in_file(self, mock_get):
        def side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            mock_resp.status_code = 200
            mock_resp.content = b"dummy content"
            if url == "https://test.com/root.txt":
                mock_resp.text = "https://test.com/page1.txt\nhttps://test.com/page2.txt"
            else:
                mock_resp.text = ""
            return mock_resp

        mock_get.side_effect = side_effect

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/root.txt")

        self.assertIn("https://test.com/root.txt", graph)
        node = graph["https://test.com/root.txt"]
        self.assertEqual(len(node.children), 2)
        child_urls = [child.url for child in node.children]
        self.assertIn("https://test.com/page1.txt", child_urls)
        self.assertIn("https://test.com/page2.txt", child_urls)

    @patch("requests.get")
    def test_ignores_empty_lines_and_comments(self, mock_get):
        def side_effect(url, *args, **kwargs):
            mock_resp = Mock()
            mock_resp.status_code = 200
            mock_resp.content = b"dummy content"
            if url == "https://test.com/root.txt":
                mock_resp.text = "\n# Comment\nhttps://test.com/page.txt\n\n"
            else:
                mock_resp.text = ""
            return mock_resp

        mock_get.side_effect = side_effect

        builder = GraphBuilder()
        graph, dead_links = builder.build_graph("https://test.com/root.txt")

        node = graph["https://test.com/root.txt"]
        self.assertEqual(len(node.children), 1)
        self.assertEqual(node.children[0].url, "https://test.com/page.txt")

if __name__ == '__main__':
    unittest.main()

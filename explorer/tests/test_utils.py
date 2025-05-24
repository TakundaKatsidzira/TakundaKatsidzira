import unittest
import time
from src.utils import (
    format_error, search, top_n, bottom_n, pretty_print_tree, get_help
)
from src.filesystem import FileNode, DirectoryNode

class TestUtils(unittest.TestCase):
    def setUp(self):
        # Build a mock directory tree
        self.root = DirectoryNode("root", "/")
        self.file1 = FileNode("file1.txt", "/file1.txt")
        self.file1.size = 100
        self.file1.created_time = time.time() - 10
        self.file2 = FileNode("file2.txt", "/file2.txt")
        self.file2.size = 50
        self.file2.created_time = time.time()

        self.dir1 = DirectoryNode("dir1", "/dir1")
        self.file3 = FileNode("file3.txt", "/dir1/file3.txt")
        self.file3.size = 200
        self.file3.created_time = time.time() - 5

        self.root.children = [self.file1, self.file2, self.dir1]
        self.dir1.children = [self.file3]

    def test_format_error(self):
        self.assertEqual(format_error("Bad input"), "[Error] Bad input")

    def test_search_file(self):
        result = search(self.root, "file3.txt")
        self.assertIn("/dir1/file3.txt", result)

    def test_search_directory(self):
        result = search(self.root, "dir1", is_dir=True)
        self.assertIn("/dir1", result)

    import tempfile
    

def test_top_n_by_size(self):
    with tempfile.TemporaryDirectory() as tmpdir:
        file1 = os.path.join(tmpdir, "file1.txt")
        file2 = os.path.join(tmpdir, "file2.txt")
        with open(file1, 'w') as f: f.write("a" * 100)
        with open(file2, 'w') as f: f.write("a" * 10)
        root = build_tree(tmpdir)
        result = top_n(root, 2)
        self.assertIn("file1.txt", result[0])

    def test_bottom_n_by_size(self):
        result = bottom_n(self.root, n=2)
        self.assertEqual(result, ["/file2.txt", "/file1.txt"])

    def test_top_n_by_date(self):
        result = top_n(self.root, n=1, by_date=True)
        self.assertEqual(result, ["/file2.txt"])

    def test_bottom_n_by_date(self):
        result = bottom_n(self.root, n=1, by_date=True)
        self.assertEqual(result, ["/file1.txt"])

    def test_pretty_print_tree(self):
        output = pretty_print_tree(self.root)
        self.assertIn("root/", output[0])
        self.assertTrue(any("file1.txt" in line for line in output))

    def test_get_help_general(self):
        help_text = get_help()
        self.assertIn("cr: Create a file or directory", help_text)

    def test_get_help_specific(self):
        help_cr = get_help("cr")
        self.assertIn("Usage: cr filename", help_cr)

    def test_get_help_invalid(self):
        help_invalid = get_help("nope")
        self.assertIn("No help entry", help_invalid)

if __name__ == '__main__':
    unittest.main()

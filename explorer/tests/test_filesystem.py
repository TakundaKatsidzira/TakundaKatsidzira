import unittest
import os
import shutil
from src.filesystem import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        # Ensure clean state
        self.test_state_path = "data/state.json"
        if os.path.exists(self.test_state_path):
            os.remove(self.test_state_path)
        self.fs = FileSystem()

    def test_create_file(self):
        msg = self.fs.create("test.txt")
        self.assertIn("Created file", msg)
        self.assertIn("/test.txt", self.fs.path_map)

    def test_create_directory(self):
        msg = self.fs.create("folder", is_dir=True)
        self.assertIn("Created directory", msg)
        self.assertIn("/folder", self.fs.path_map)

    def test_change_directory(self):
        self.fs.create("dir1", is_dir=True)
        msg = self.fs.change_dir("dir1")
        self.assertIn("Changed directory to /dir1", msg)

    def test_write_and_read_file(self):
        self.fs.create("file.txt")
        self.fs.write_file("file.txt", "Hello")
        content = self.fs.read_file("file.txt")
        self.assertEqual(content, "Hello")

    def test_append_file(self):
        self.fs.create("append.txt")
        self.fs.write_file("append.txt", "Line1")
        self.fs.write_file("append.txt", "Line2", append=True)
        content = self.fs.read_file("append.txt")
        self.assertEqual(content, "Line1\nLine2")

    def test_delete_node(self):
        self.fs.create("delete_me")
        msg = self.fs.delete("delete_me")
        self.assertIn("Deleted", msg)
        self.assertNotIn("/delete_me", self.fs.path_map)

    def test_list_directory(self):
        self.fs.create("a.txt")
        self.fs.create("b.txt")
        listing = self.fs.list_dir()
        self.assertIn("a.txt", listing)
        self.assertIn("b.txt", listing)

    def test_save_and_load_state(self):
        self.fs.create("persist.txt")
        self.fs.write_file("persist.txt", "data")
        self.fs.save_state()

        # Load from saved state
        new_fs = FileSystem()
        self.assertIn("/persist.txt", new_fs.path_map)
        content = new_fs.read_file("persist.txt")
        self.assertEqual(content, "data")

if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import MagicMock
from src.commands import CommandHandler
from src.utils import format_error


class TestCommandHandler(unittest.TestCase):
    def setUp(self):
        self.mock_fs = MagicMock()
        self.handler = CommandHandler(self.mock_fs)

    def test_cr_file(self):
        self.mock_fs.create.return_value = "File created"
        result = self.handler.execute(["cr", "test.txt"])
        self.assertEqual(result, "File created")
        self.mock_fs.create.assert_called_with("test.txt", False)

    def test_cr_directory(self):
        self.mock_fs.create.return_value = "Directory created"
        result = self.handler.execute(["cr", "folder", "-d"])
        self.assertEqual(result, "Directory created")
        self.mock_fs.create.assert_called_with("folder", True)

    def test_dl(self):
        self.mock_fs.delete.return_value = "Deleted"
        result = self.handler.execute(["dl", "test.txt"])
        self.assertEqual(result, "Deleted")
        self.mock_fs.delete.assert_called_with("test.txt")

    def test_cd(self):
        self.mock_fs.change_dir.return_value = "Changed directory"
        result = self.handler.execute(["cd", "folder"])
        self.assertEqual(result, "Changed directory")
        self.mock_fs.change_dir.assert_called_with("folder")

    def test_lc(self):
        self.mock_fs.get_cwd.return_value = "/home"
        result = self.handler.execute(["lc"])
        self.assertEqual(result, "/home")

    def test_rd_full(self):
        self.mock_fs.read_file.return_value = ["line1", "line2"]
        result = self.handler.execute(["rd", "file.txt"])
        self.assertEqual(result, "line1\nline2")

    def test_rd_limited(self):
        self.mock_fs.read_file.return_value = ["line1"]
        result = self.handler.execute(["rd", "file.txt", "1"])
        self.assertEqual(result, "line1")
        self.mock_fs.read_file.assert_called_with("file.txt", 1)

    def test_wr_write(self):
        self.mock_fs.write_file.return_value = "Written"
        result = self.handler.execute(["wr", "file.txt", "Hello"])
        self.assertEqual(result, "Written")
        self.mock_fs.write_file.assert_called_with("file.txt", "Hello", False)

    def test_wr_append(self):
        self.mock_fs.write_file.return_value = "Appended"
        result = self.handler.execute(["wr", "file.txt", "Hello", "-a"])
        self.assertEqual(result, "Appended")
        self.mock_fs.write_file.assert_called_with("file.txt", "Hello", True)

    def test_fd_no_match(self):
        result = self.handler.execute(["fd", "missing"])
        self.assertEqual(result, "No matches found.")

    def test_ls(self):
        self.mock_fs.list_dir.return_value = ["file1", "file2"]
        result = self.handler.execute(["ls"])
        self.assertEqual(result, "file1\nfile2")

    def test_hp_specific(self):
        result = self.handler.execute(["hp", "cr"])
        self.assertIn("cr:", result)

    def test_ex_skips_save(self):
        with self.assertRaises(SystemExit):
            self.handler.execute(["ex", "!"])

    def test_missing_command(self):
        result = self.handler.execute([])
        self.assertEqual(result, format_error("No command given."))

    def test_unknown_command(self):
        result = self.handler.execute(["unknown"])
        self.assertEqual(result, format_error("Unknown command: unknown"))

    def test_index_error(self):
        result = self.handler.execute(["cr"])
        self.assertEqual(result, format_error("Missing argument(s)."))

    def test_value_error(self):
        result = self.handler.execute(["rd", "file.txt", "invalid"])
        self.assertEqual(result, format_error("Invalid argument type."))

if __name__ == '__main__':
    unittest.main()

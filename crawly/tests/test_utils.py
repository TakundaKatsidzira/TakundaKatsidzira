# tests/test_utils.py
import unittest
from src.utils import is_valid_url, normalize_url, hash_url

class TestUtils(unittest.TestCase):
    def test_is_valid_url(self):
        self.assertTrue(is_valid_url("https://example.com"))
        self.assertFalse(is_valid_url("not_a_url"))

    def test_normalize_url(self):
        self.assertEqual(normalize_url("https://example.com/"), "https://example.com")
        self.assertEqual(normalize_url("  https://a.com/test  "), "https://a.com/test")

    def test_hash_url(self):
        self.assertEqual(hash_url("https://example.com"), hash_url("https://example.com"))

if __name__ == '__main__':
    unittest.main()

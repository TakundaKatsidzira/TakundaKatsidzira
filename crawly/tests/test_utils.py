import unittest
from src.utils import is_valid_url, normalize_url, hash_url

class TestUtils(unittest.TestCase):
    def test_is_valid_url(self):
        self.assertTrue(is_valid_url("https://example.com"))
        self.assertTrue(is_valid_url("http://sub.domain.com/path"))
        self.assertFalse(is_valid_url("not_a_url"))
        self.assertFalse(is_valid_url("ftp://example.com"))
        self.assertFalse(is_valid_url("example.com"))  # Missing scheme

    def test_normalize_url(self):
        self.assertEqual(normalize_url("https://example.com/"), "https://example.com")
        self.assertEqual(normalize_url("  https://a.com/test  "), "https://a.com/test")
        self.assertEqual(normalize_url("https://a.com/path/"), "https://a.com/path")
        self.assertEqual(normalize_url("HTTPS://B.com/Path/"), "https://b.com/Path")  # Case normalization

    def test_hash_url(self):
        url1 = "https://example.com"
        url2 = "https://example.com/"
        self.assertEqual(hash_url(url1), hash_url(url1))  # deterministic
        self.assertNotEqual(hash_url(url1), hash_url("https://different.com"))
        self.assertEqual(hash_url(url1), hash_url(url2))  # if normalize_url is used inside hash_url

    def test_hash_url_consistency(self):
        url = "https://example.com/page"
        self.assertEqual(hash_url(url), hash_url(url))  # should always match

if __name__ == '__main__':
    unittest.main()

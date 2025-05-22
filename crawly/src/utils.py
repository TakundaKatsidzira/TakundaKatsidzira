# src/utils.py
from urllib.parse import urlparse
import hashlib

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ["http", "https"], result.netloc])
    except:
        return False

def normalize_url(url):
    return url.strip().rstrip('/')

def hash_url(url):
    return hashlib.md5(url.encode()).hexdigest()

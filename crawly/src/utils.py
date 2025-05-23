from urllib.parse import urlparse
import hashlib

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme in ["http", "https"], result.netloc])
    except:
        return False

from urllib.parse import urlparse, urlunparse

def normalize_url(url):
    url = url.strip().rstrip('/')
    parsed = urlparse(url)
    normalized = parsed._replace(
        scheme=parsed.scheme.lower(),
        netloc=parsed.netloc.lower()
    )
    return urlunparse(normalized)

def hash_url(url):
    from .utils import normalize_url
    normalized = normalize_url(url)
    return hashlib.md5(normalized.encode()).hexdigest()

from urllib.parse import urlparse, urlunparse
import hashlib

def is_valid_url(url):
    try:
        result = urlparse(url)
        return result.scheme in ["http", "https"] and result.netloc != ""
    except Exception:
        return False

def normalize_url(url):
    url = url.strip().rstrip('/')
    parsed = urlparse(url)
    normalized = parsed._replace(
        scheme=parsed.scheme.lower(),
        netloc=parsed.netloc.lower()
    )
    return urlunparse(normalized)

def hash_url(url):
    normalized = normalize_url(url)
    return hashlib.md5(normalized.encode()).hexdigest()

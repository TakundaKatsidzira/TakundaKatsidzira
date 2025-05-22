# src/graph_builder.py
import requests
from urllib.parse import urljoin
from utils import is_valid_url, normalize_url

class GraphBuilder:
    def __init__(self):
        self.graph = {}
        self.visited = set()
        self.dead_links = set()

    def build_graph(self, root_url):
        normalized_url = normalize_url(root_url)
        self._dfs(normalized_url)
        return self.graph, self.dead_links

    def _dfs(self, url):
        if url in self.visited:
            return
        self.visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                self.dead_links.add(url)
                return
            lines = response.text.strip().splitlines()
            child_urls = []

            for line in lines:
                line = line.strip()
                if not line:
                    continue
                child_url = urljoin(url, line)
                if is_valid_url(child_url):
                    child_url = normalize_url(child_url)
                    child_urls.append(child_url)
                    self._dfs(child_url)

            self.graph[url] = child_urls
        except Exception:
            self.dead_links.add(url)

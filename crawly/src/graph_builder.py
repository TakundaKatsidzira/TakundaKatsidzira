# src/graph_builder.py
import requests
from urllib.parse import urljoin
from .utils import is_valid_url, normalize_url

class GraphBuilder:
    def __init__(self):
        self.graph = {}
        self.visited = set()
        self.dead_links = set()

    def build_graph(self, root_url):
        normalized_url = normalize_url(root_url)
        self._dfs(normalized_url)
        return self.graph, self.dead_links

    def _dfs(self, url, depth=0):
        indent = "  " * depth
        print(f"{indent}↳ Visiting: {url}")
    
        if url in self.visited:
            print(f"{indent}  ⤷ Already visited")
            return
        self.visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                print(f"{indent}  ✖ Dead link (status {response.status_code})")
                self.dead_links.add(url)
                return
            lines = response.text.strip().splitlines()
            child_urls = []

            for line in lines:
                line = line.strip()
                if not line or line.startswith("#"):  # ← add this condition
                    continue
                child_url = urljoin(url, line)
                if is_valid_url(child_url):
                    child_url = normalize_url(child_url)
                    child_urls.append(child_url)
                    self._dfs(child_url, depth + 1)

            self.graph[url] = child_urls
        except Exception as e:
            print(f"{indent}  ⚠ Exception fetching {url}: {e}")
            self.dead_links.add(url)

    def print_graph_tree(self, root_url, depth=0, visited=None):
        if visited is None:
            visited = set()
        indent = "  " * depth
        print(f"{indent}- {root_url}")
        visited.add(root_url)

        for child in self.graph.get(root_url, []):
            if child not in visited:
                self.print_graph_tree(child, depth + 1, visited)
            else:
                print(f"{'  ' * (depth + 1)}↺ {child} (already visited)")

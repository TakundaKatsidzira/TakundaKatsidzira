import requests
from urllib.parse import urljoin
from .utils import is_valid_url, normalize_url
from .page_node import PageNode

class GraphBuilder:
    def __init__(self, verbose=False):
        self.graph = {}  # str → PageNode
        self.visited = set()
        self.dead_links = set()
        self.verbose = verbose

    def build_graph(self, root_url):
        normalized_url = normalize_url(root_url)
        self._dfs(normalized_url)
        return self.graph, self.dead_links

    def _dfs(self, url, depth=0):
        indent = "  " * depth
        if self.verbose:
            print(f"{indent}↳ Visiting: {url}")

        if url in self.visited:
            if self.verbose:
                print(f"{indent}  ⤷ Already visited")
            return

        self.visited.add(url)
        node = self.graph.setdefault(url, PageNode(url))

        try:
            response = requests.get(url, timeout=5)
            node.status_code = response.status_code
            node.size = len(response.content)

            if response.status_code != 200:
                if self.verbose:
                    print(f"{indent}  ✖ Dead link (status {response.status_code})")
                self.dead_links.add(url)
                return

            lines = response.text.strip().splitlines()
            for line in lines:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                child_url = urljoin(url, line)
                if is_valid_url(child_url):
                    normalized_child = normalize_url(child_url)
                    child_node = self.graph.setdefault(normalized_child, PageNode(normalized_child))
                    node.add_child(child_node)
                    self._dfs(normalized_child, depth + 1)

        except requests.RequestException as e:
            if self.verbose:
                print(f"{indent}  ⚠ Error fetching {url}: {e}")
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

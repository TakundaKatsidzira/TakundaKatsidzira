from collections import defaultdict, deque, Counter
import heapq

class Analyzer:
    def __init__(self, graph, dead_links, verbose = False):
        self.verbose = verbose
        self.graph = graph  # {url: PageNode}
        self.dead_links = dead_links
        self.visited = set()
        self.rec_stack = set()
        self.has_cycles = False
        self.leaf_nodes = []
        self.topo_order = []

    def analyze(self):
        if self.verbose:
            print("[INFO] Starting graph analysis...")
        for node in self.graph.values():
            if node.url not in self.visited:
                self._dfs_cycle_detect(node)

        self.leaf_nodes = [n.url for n in self.graph.values() if not n.children]
        self.topo_order = self._topological_sort()

        return {
            "total_nodes": len(self.graph),
            "leaf_nodes": self.leaf_nodes,
            "dead_links": self.dead_links,
            "has_cycles": self.has_cycles,
            "top_frequent": self._top_frequent(),
            "top_size": self._top_file_sizes(),
            "topo_sort": self.topo_order
        }

    def _dfs_cycle_detect(self, node, depth=0):
        indent = "  " * depth
        print(f"{indent}→ DFS visiting {node.url}")

        self.visited.add(node.url)
        self.rec_stack.add(node.url)

        node.visits += 1

        for child_node in node.children:
            child_node.visits += 1
            if child_node.url not in self.visited:
                self._dfs_cycle_detect(child_node, depth + 1)
            elif child_node.url in self.rec_stack:
                print(f"{indent}⚠ Cycle detected: {node.url} → {child_node.url}")
                self.has_cycles = True

        self.rec_stack.remove(node.url)

    def _top_file_sizes(self, k=5):
        return heapq.nlargest(
            k,
            [(node.url, node.size) for node in self.graph.values()],
            key=lambda x: x[1]
        )

    def _top_frequent(self, k=5):
        return heapq.nlargest(
            k,
            [(node.url, node.visits) for node in self.graph.values()],
            key=lambda x: x[1]
        )

    def _topological_sort(self):
        in_degree = defaultdict(int)

        for node in self.graph.values():
            for child in node.children:
                in_degree[child.url] += 1

        queue = deque([node.url for node in self.graph.values() if in_degree[node.url] == 0])
        topo_order = []

        while queue:
            url = queue.popleft()
            topo_order.append(url)
            node = self.graph[url]
            for child in node.children:
                in_degree[child.url] -= 1
                if in_degree[child.url] == 0:
                    queue.append(child.url)

        if len(topo_order) != len(self.graph):
            print("[CYCLE DETECTED] Topological sort incomplete")
        return topo_order

    def print_bfs_layers(self, root_url):
        print(f"\n[INFO] BFS Layer Ranking from {root_url}:")
        visited = set()
        queue = deque([(root_url, 0)])
        layers = defaultdict(list)

        while queue:
            url, level = queue.popleft()
            if url in visited:
                continue
            visited.add(url)
            layers[level].append(url)

            node = self.graph.get(url)
            if not node:
                continue
            for child in node.children:
                if child.url not in visited:
                    queue.append((child.url, level + 1))

        for level in sorted(layers.keys()):
            print(f"Layer {level}:")
            for url in layers[level]:
                print(f"  - {url}")

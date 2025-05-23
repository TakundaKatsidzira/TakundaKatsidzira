# src/analyzer.py
from collections import defaultdict, deque, Counter
import heapq
import requests

class Analyzer:
    def __init__(self, graph, dead_links):
        self.graph = graph
        self.dead_links = dead_links
        self.visited = set()
        self.rec_stack = set()
        self.has_cycles = False
        self.freq_counter = Counter()
        self.file_sizes = {}

    def analyze(self):
        # Analyze graph starting from all root nodes
        for node in self.graph:
            if node not in self.visited:
                self._dfs_cycle_and_freq(node)

        leaf_nodes = [node for node, children in self.graph.items() if not children]
        topo_sort = self._topological_sort()
        top_frequent = self.freq_counter.most_common(5)
        top_size = self._get_top_file_sizes()

        return {
            "total_nodes": len(self.graph),
            "leaf_nodes": leaf_nodes,
            "dead_links": self.dead_links,
            "has_cycles": self.has_cycles,
            "top_frequent": top_frequent,
            "top_size": top_size,
            "topo_sort": topo_sort
        }

    def _dfs_cycle_and_freq(self, node, depth=0):
        indent = "  " * depth
        print(f"{indent}→ DFS visiting {node}")
        self.visited.add(node)
        self.rec_stack.add(node)
        self.freq_counter[node] += 1
        self._record_file_size(node)

        for neighbor in self.graph.get(node, []):
            self.freq_counter[neighbor] += 1
            if neighbor not in self.visited:
                self._dfs_cycle_and_freq(neighbor, depth + 1)
            elif neighbor in self.rec_stack:
                print(f"{indent}⚠ Cycle detected: {node} → {neighbor}")
                self.has_cycles = True

        self.rec_stack.remove(node)

    def _record_file_size(self, url):
        try:
            response = requests.head(url, timeout=3)
            size = int(response.headers.get('Content-Length', 0))
        except Exception:
            size = 0
        self.file_sizes[url] = size

    def _get_top_file_sizes(self, k=5):
        return heapq.nlargest(k, self.file_sizes.items(), key=lambda x: x[1])

    from collections import deque, defaultdict

    from collections import deque, defaultdict

    def _topological_sort(self):
        in_degree = defaultdict(int)
        referenced_nodes = set()

        print("[INFO] Computing in-degrees for topological sort...")
        for u in list(self.graph.keys()):
            for v in self.graph.get(u, []):
                in_degree[v] += 1
                referenced_nodes.add(v)

        for v in referenced_nodes:
            if v not in self.graph:
                print(f"[WARN] {v} was referenced but not fetched (possibly a dead link?)")
                self.graph[v] = []

        queue = deque([u for u in self.graph if in_degree[u] == 0])
        print(f"[INFO] Starting nodes (in-degree 0): {list(queue)}")
        topo_order = []

        while queue:
            u = queue.popleft()
            topo_order.append(u)
            print(f"→ {u}")

            for v in self.graph.get(u, []):
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

                if len(topo_order) != len(self.graph):
                    print("[CYCLE DETECTED] Topological sort incomplete — graph has cycles.")
                return topo_order
            
    def print_bfs_layers(self, root_url):
        print(f"\n[INFO] BFS Layer Ranking from {root_url}:")
        visited = set()
        queue = deque([(root_url, 0)])
        layers = defaultdict(list)
    
        while queue:
            node, level = queue.popleft()
            if node in visited:
                continue
            visited.add(node)
            layers[level].append(node)

            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, level + 1))

        for level in sorted(layers.keys()):
            print(f"Layer {level}:")
            for node in layers[level]:
                print(f"  - {node}")


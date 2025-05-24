import time
import heapq
from typing import List, Union
from .filesystem import Node, DirectoryNode, FileNode

HELP_MANUAL = {
    'cr': {'desc': 'Create a file or directory', 'usage': 'cr filename | cr dirname -d'},
    'dl': {'desc': 'Delete a file or directory', 'usage': 'dl filename | dl dirname -d'},
    'cd': {'desc': 'Change current directory', 'usage': 'cd [dirname]'},
    'lc': {'desc': 'List current directory', 'usage': 'lc'},
    'rd': {'desc': 'Read file content', 'usage': 'rd filename [n]'},
    'wr': {'desc': 'Write or append to file', 'usage': 'wr filename "text" [-a]'},
    'fd': {'desc': 'Find file or directory', 'usage': 'fd name [-d]'},
    'tp': {'desc': 'Top-N files/directories', 'usage': 'tp [n] [-d]'},
    'bt': {'desc': 'Bottom-N files/directories', 'usage': 'bt [n] [-d]'},
    'ls': {'desc': 'List contents of path', 'usage': 'ls [path]'},
    'tr': {'desc': 'Print directory tree', 'usage': 'tr [path]'},
    'hp': {'desc': 'Help manual', 'usage': 'hp [command]'},
    'ex': {'desc': 'Exit and optionally skip saving', 'usage': 'ex [!]'}
}

def pretty_print_tree(node: Node, prefix: str = "") -> List[str]:
    lines = [prefix + node.name + ("/" if node.type == 'directory' else "")]
    if isinstance(node, DirectoryNode):
        for child in sorted(node.children, key=lambda x: x.name):
            lines.extend(pretty_print_tree(child, prefix + "    "))
    return lines

def format_error(msg: str) -> str:
    return f"[Error] {msg}"

def search(node: Node, name: str, is_dir: bool = False, use_dfs: bool = True) -> List[str]:
    results = []
    stack = [node] if use_dfs else [node]
    while stack:
        current = stack.pop() if use_dfs else stack.pop(0)
        if current.name == name and (not is_dir or current.type == 'directory'):
            results.append(current.path)
        if isinstance(current, DirectoryNode):
            stack.extend(current.children)
    return results

def top_n(node: Node, n: int = 1, by_date: bool = False) -> List[str]:
    heap = []
    def visit(node: Node):
        if isinstance(node, FileNode):
            metric = node.created_time if by_date else node.size
            heapq.heappush(heap, (-metric, node.path))
        elif isinstance(node, DirectoryNode):
            for child in node.children:
                visit(child)
    visit(node)
    return [path for _, path in heapq.nsmallest(n, heap)]

def bottom_n(node: Node, n: int = 1, by_date: bool = False) -> List[str]:
    heap = []
    def visit(node: Node):
        if isinstance(node, FileNode):
            metric = node.created_time if by_date else node.size
            heapq.heappush(heap, (metric, node.path))
        elif isinstance(node, DirectoryNode):
            for child in node.children:
                visit(child)
    visit(node)
    return [path for _, path in heapq.nsmallest(n, heap)]

def get_help(cmd: str = None) -> str:
    if cmd:
        entry = HELP_MANUAL.get(cmd)
        return f"{cmd}: {entry['desc']}\nUsage: {entry['usage']}" if entry else f"No help entry for '{cmd}'"
    return '\n'.join([f"{cmd}: {info['desc']}" for cmd, info in HELP_MANUAL.items()])
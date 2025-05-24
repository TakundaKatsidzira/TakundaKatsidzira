import os
import json
import time
from typing import Union, List

class Node:
    def __init__(self, name: str, path: str, node_type: str):
        self.name = name
        self.path = path
        self.type = node_type  # 'file' or 'directory'
        self.created_time = time.time()
        self.size = 0

class FileNode(Node):
    def __init__(self, name: str, path: str):
        super().__init__(name, path, 'file')
        self.content = ""

class DirectoryNode(Node):
    def __init__(self, name: str, path: str):
        super().__init__(name, path, 'directory')
        self.children = []  # List[Node]

class FileSystem:
    def __init__(self):
        self.root = DirectoryNode("/", "/")
        self.current_dir = self.root
        self.path_map = {"/": self.root}
        self.state_file = "data/state.json"
        self.load_state()

    def save_state(self):
        def serialize(node):
            if node.type == 'file':
                return {
                    'type': node.type,
                    'name': node.name,
                    'path': node.path,
                    'created_time': node.created_time,
                    'size': node.size,
                    'content': node.content
                }
            else:
                return {
                    'type': node.type,
                    'name': node.name,
                    'path': node.path,
                    'created_time': node.created_time,
                    'size': node.size,
                    'children': [serialize(child) for child in node.children]
                }

        with open(self.state_file, 'w') as f:
            json.dump(serialize(self.root), f)

    def load_state(self):
        if not os.path.exists(self.state_file):
            return

        def deserialize(data):
            if data['type'] == 'file':
                node = FileNode(data['name'], data['path'])
                node.content = data.get('content', '')
            else:
                node = DirectoryNode(data['name'], data['path'])
                node.children = [deserialize(child) for child in data.get('children', [])]
            node.created_time = data.get('created_time', time.time())
            node.size = data.get('size', 0)
            self.path_map[node.path] = node
            return node

        with open(self.state_file, 'r') as f:
            data = json.load(f)
            self.root = deserialize(data)
            self.current_dir = self.root

    def _resolve_path(self, name: str) -> Union[Node, None]:
        if name == "..":
            path_parts = self.current_dir.path.rstrip('/').split('/')[:-1]
            target_path = '/' if not path_parts else '/'.join(path_parts)
            return self.path_map.get(target_path, self.root)
        full_path = self.current_dir.path.rstrip('/') + '/' + name if self.current_dir.path != '/' else '/' + name
        return self.path_map.get(full_path)

    def create(self, name: str, is_dir: bool = False) -> str:
        if '/' in name:
            return f"Invalid name: {name}"
        full_path = self.current_dir.path.rstrip('/') + '/' + name if self.current_dir.path != '/' else '/' + name
        if full_path in self.path_map:
            return f"{name} already exists."

        if is_dir:
            node = DirectoryNode(name, full_path)
        else:
            node = FileNode(name, full_path)

        self.path_map[full_path] = node
        self.current_dir.children.append(node)
        return f"Created {'directory' if is_dir else 'file'}: {name}"

    def delete(self, name: str) -> str:
        node = self._resolve_path(name)
        if not node:
            return f"{name} not found."
        if node == self.root:
            return "Cannot delete root directory."

        parent_path = '/'.join(node.path.rstrip('/').split('/')[:-1]) or '/'
        parent = self.path_map.get(parent_path)
        if isinstance(parent, DirectoryNode):
            parent.children = [child for child in parent.children if child.name != name]
        self._remove_from_path_map(node)
        return f"Deleted {name}"

    def _remove_from_path_map(self, node: Node):
        del self.path_map[node.path]
        if node.type == 'directory':
            for child in getattr(node, 'children', []):
                self._remove_from_path_map(child)

    def change_dir(self, name: Union[str, None]) -> str:
        target = self._resolve_path(name or "..")
        if not target or target.type != 'directory':
            return f"Invalid directory: {name}"
        self.current_dir = target
        return f"Changed directory to {self.current_dir.path}"

    def get_cwd(self) -> str:
        return self.current_dir.path

    def list_dir(self, path: str = None) -> List[str]:
        node = self._resolve_path(path) if path else self.current_dir
        if not node or node.type != 'directory':
            return [f"Invalid path: {path}"]
        return sorted([child.name for child in node.children])

    def read_file(self, name: str, lines: int = None) -> Union[str, List[str]]:
        node = self._resolve_path(name)
        if not node or node.type != 'file':
            return f"Invalid file: {name}"
        return node.content.splitlines()[:lines] if lines else node.content

    def write_file(self, name: str, content: str, append: bool = False) -> str:
        node = self._resolve_path(name)
        if not node or node.type != 'file':
            return f"Invalid file: {name}"
        if append:
            node.content += f"\n{content}"
        else:
            node.content = content
        node.size = len(node.content)
        return f"{'Appended to' if append else 'Wrote to'} file: {name}"

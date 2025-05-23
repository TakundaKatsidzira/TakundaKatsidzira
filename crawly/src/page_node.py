# src/page_node.py
class PageNode:
    def __init__(self, url):
        self.url = url
        self.children = []
        self.status_code = None
        self.size = 0
        self.visits = 0

    def add_child(self, child_node):
        if child_node.url not in [child.url for child in self.children]:
            self.children.append(child_node)

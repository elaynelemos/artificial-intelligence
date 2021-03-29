class Edge:
    def __init__(self, root):
        self.nodes = array(root)

    def is_empty(self):
        return not bool(len(self.nodes))

    def pop(self):
        return self.nodes.pop(0)

    def insert(self, node):
        self.nodes.append(node)
        return self

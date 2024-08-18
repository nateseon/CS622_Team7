class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BPlusTree:
    def __init__(self, t):
        self.root = BPlusTreeNode(True)
        self.t = t  # t is the order of the B+ tree

    def insert(self, key):
        # Insert logic for B+ tree
        pass

    def search(self, key):
        # Search logic for B+ tree
        pass

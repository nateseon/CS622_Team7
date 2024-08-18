class Node:
    def __init__(self, data, color="red"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0, color="black")
        self.root = self.TNULL

    def insert(self, key):
        # Insert logic with fixing the tree balance (rotation and recoloring)
        pass

    def delete(self, key):
        # Delete logic with fixing the tree balance (rotation and recoloring)
        pass

    def search(self, key):
        node = self.root
        while node != self.TNULL:
            if key == node.data:
                return node
            elif key < node.data:
                node = node.left
            else:
                node = node.right
        return None

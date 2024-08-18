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
        node = Node(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "red"

        parent = None
        current = self.root

        while current != self.TNULL:
            parent = current
            if node.data < current.data:
                current = current.left
            else:
                current = current.right

        node.parent = parent
        if parent is None:
            self.root = node
        elif node.data < parent.data:
            parent.left = node
        else:
            parent.right = node

        if node.parent is None:
            node.color = "black"
            return

        if node.parent.parent is None:
            return

        self._fix_insert(node)

    def _fix_insert(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.right:
                u = node.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._left_rotate(node.parent.parent)
            else:
                u = node.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self._right_rotate(node.parent.parent)
            if node == self.root:
                break
        self.root.color = "black"

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def search(self, key):
        return self._search_tree_helper(self.root, key)

    def _search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self._search_tree_helper(node.left, key)
        return self._search_tree_helper(node.right, key)

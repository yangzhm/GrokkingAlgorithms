import reprlib


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node(%s)' % reprlib.repr(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._search(self.root, value) is not None

    def _search(self, node, value):
        if node is None:
            return None
        elif node.value == value:
            return node
        elif value > node.value:
            return self._search(node.right, value)
        else:
            return self._search(node.left, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            print("No node to delete.")
        elif node.value > value:
            node.left = self._delete(node.left, value)
        elif node.value < value:
            node.right = self._delete(node.right, value)
        elif node.value == value:
            if node.left is None and node.right is None:
                node = None
            elif node.left is not None and node.right is not None:
                minnode = self.findmin(node.right)
                node.value = minnode.value
                node.right = self._delete(node.right, minnode.value)
            elif node.left is not None:
                node = node.left
            else:
                node = node.right

        return node

    def findmin(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        else:
            return self.findmin(node.left)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            node = Node(value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            print("The node is exist!")

        return node


bst = BinarySearchTree()
bst.insert(10)
bst.insert(3)
bst.insert(20)
bst.insert(1)
bst.insert(7)
bst.insert(25)
bst.insert(5)
bst.insert(9)
bst.insert(23)

print(bst.search(9))
print(bst.search(19))

bst.delete(9)

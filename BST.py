from queue_array import QueueArray


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None


class BinarySearchTree:
    # write the __init__() method here. The tree has at least a ‘root’ node.
    #
    def __init__(self) -> None:
        self.root = None

    def find(self, key):  # returns True if key is in a node of the tree, else False
        if self.root == None:
            raise (IndexError("Tree is empty"))
        return self._find(key, self.root)

    def _find(self, key, node):
        if node == None:
            return False
        elif key < node.key:
            return self._find(key, node.left)
        elif key > node.key:
            return self._find(key, node.right)
        else:
            return True

    def find_min(self):  # returns min value in the tree
        if self.root == None:
            raise (IndexError("Tree is empty"))
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left == None:
            return node.key
        else:
            return self._find_min(node.left)

    def find_max(self):  # returns max value in the tree
        if self.root == None:
            raise (IndexError("Tree is empty"))
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right == None:
            return node.key
        else:
            return self._find_max(node.right)

    def insert(
        self, newkey
    ):  # inserts a node with key into the correct position if not a duplicate.
        if self.root == None:
            self.root = TreeNode(newkey)
        else:
            self._insert(newkey, self.root)

    def _insert(self, newkey, node):
        # print("node", node)
        # print("node key", node.key)
        if newkey < node.key:
            if node.left == None:
                node.left = TreeNode(newkey)
            else:
                self._insert(newkey, node.left)
        elif newkey > node.key:
            if node.right == None:
                node.right = TreeNode(newkey)
            else:
                self._insert(newkey, node.right)

    def delete(
        self, key
    ):  # deletes the node containing key, assumes such a node exists
        if self.root.key == key:
            self.root.key = None
        else:
            self._delete(key, self.root)
        print("done")

    def _delete(self, key, node):
        pass

    def print_tree(self):  # print inorder the entire tree
        self._print_tree(self.root)

    def _print_tree(self, node):
        if node:
            self._print_tree(node.left)
            print(node.key)
            self._print_tree(node.right)

    def is_empty(self):  # returns True if tree is empty, else False
        if self.root == None:
            return True

    def inorder_print_tree(self):  # print inorder the subtree of self
        self._print_tree(self.root)

    def print_levels(
        self,
    ):  # inorder traversal prints lists of pairs, [key, level of the node] where root is level ()
        queue = QueueArray(100)
        queue.enqueue(self.root)
        while queue.is_empty() is not True:
            node = queue.dequeue()
            print(node.key)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

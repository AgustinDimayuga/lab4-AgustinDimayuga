import matplotlib.pyplot as plt
import networkx as nx

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

    def _build_graph(self, node, graph, pos, x=0, y=0, layer=1):
        """Build a NetworkX graph representation of the tree"""
        if node is not None:
            # Add the current node to the graph
            graph.add_node(node.key)

            # Position the node
            pos[node.key] = (x, y)

            # Calculate horizontal spacing
            spacing = 1.0 / (2**layer)

            # Process left child
            if node.left:
                graph.add_edge(node.key, node.left.key)
                self._build_graph(node.left, graph, pos, x - spacing, y - 1, layer + 1)

            # Process right child
            if node.right:
                graph.add_edge(node.key, node.right.key)
                self._build_graph(node.right, graph, pos, x + spacing, y - 1, layer + 1)

        return graph, pos

    def visualize(self, title="Binary Search Tree"):
        """Visualize the binary search tree using NetworkX and Matplotlib"""
        if self.root is None:
            print("Tree is empty")
            return

        # Create a directed graph
        G = nx.DiGraph()
        pos = {}

        # Build the graph
        G, pos = self._build_graph(self.root, G, pos)

        plt.figure(figsize=(10, 8))
        plt.title(title)

        # Draw the graph
        nx.draw(
            G,
            pos,
            with_labels=True,
            arrows=False,
            node_size=2000,
            node_color="skyblue",
            font_size=15,
            font_weight="bold",
        )

        plt.tight_layout()
        plt.show()


tree = BinarySearchTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)

tree.visualize("My BST Visualization")

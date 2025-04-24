import unittest

from BST import BinarySearchTree  # Adjust import based on your file name


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        for key in [50, 30, 70, 20, 40, 60, 80]:
            self.bst.insert(key)

    def test_insert_and_find(self):
        self.assertTrue(self.bst.find(30))
        self.assertTrue(self.bst.find(70))
        self.assertFalse(self.bst.find(100))

    def test_find_min(self):
        self.assertEqual(self.bst.find_min(), 20)

    def test_find_max(self):
        self.assertEqual(self.bst.find_max(), 80)

    def test_delete_leaf(self):
        self.bst.delete(20)
        self.assertFalse(self.bst.find(20))

    def test_delete_node_with_one_child(self):
        self.bst.insert(65)
        self.bst.delete(60)
        self.assertFalse(self.bst.find(60))
        self.assertTrue(self.bst.find(65))

    def test_delete_node_with_two_children(self):
        self.bst.delete(70)
        self.assertFalse(self.bst.find(70))
        self.assertTrue(self.bst.find(60))
        self.assertTrue(self.bst.find(80))

    def test_is_empty(self):
        empty_bst = BinarySearchTree()
        self.assertTrue(empty_bst.is_empty())
        self.assertFalse(self.bst.is_empty())


if __name__ == "__main__":
    unittest.main()

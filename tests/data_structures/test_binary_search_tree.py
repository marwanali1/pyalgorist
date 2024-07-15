import unittest
from src.data_structures.binary_search_tree import BinarySearchTree, TreeNode


class TestTreeNode(unittest.TestCase):
    def test_TreeNode_init(self) -> None:
        treenode = TreeNode(1)
        self.assertEqual(treenode.value, 1)

    def test_TreeNode_init_child_nodes(self) -> None:
        treenode = TreeNode(1)
        treenode.left = TreeNode(2)
        treenode.right = TreeNode(3)
        self.assertEqual(treenode.value, 1)
        self.assertEqual(treenode.left.value, 2)
        self.assertEqual(treenode.right.value, 3)


class TestBinarySearchTree(unittest.TestCase):
    def test_eq_true(self) -> None:
        tree1 = BinarySearchTree()
        tree1.insert(1)
        tree1.insert(5)
        tree1.insert(2)

        tree2 = BinarySearchTree()
        tree2.insert(1)
        tree2.insert(5)
        tree2.insert(2)

        self.assertEqual(tree1, tree2)

    def test_eq_false(self) -> None:
        tree1 = BinarySearchTree()
        tree1.insert(1)
        tree1.insert(5)
        tree1.insert(2)

        tree2 = BinarySearchTree()
        tree2.insert(1)
        tree2.insert(2)
        tree2.insert(3)

        self.assertNotEqual(tree1, tree2)

    def test_BinarySearchTree_init(self) -> None:
        bst = BinarySearchTree()
        self.assertIsNotNone(bst)

    def test_insert_single_insert(self) -> None:
        tree = BinarySearchTree()
        tree.insert(1)

        self.assertTrue(tree.search(1))

    def test_insert_multiple_inserts(self) -> None:
        tree = BinarySearchTree()
        tree.insert(1)
        tree.insert(5)
        tree.insert(2)
        tree.insert(4)
        tree.insert(3)

        self.assertTrue(tree.search(3))
        self.assertTrue(tree.search(5))

#!python3

############################################################

from typing import Tuple
import unittest
import random

from leetcode.tools.binary_tree import (
    TreeNode,
    tree_from_data,
)

############################################################
#   Tools
############################################################


def _random_val() -> int:

    return random.randrange(0, 100)


def _random_TreeNode(
) -> Tuple[Tuple[TreeNode, TreeNode, TreeNode], Tuple[int, int, int]]:

    node__val = _random_val()
    left__val = _random_val()
    right__val = _random_val()

    node = TreeNode(val=node__val)
    left = TreeNode(val=left__val)
    right = TreeNode(val=right__val)

    node.left = left
    node.right = right

    return ((node, left, right), (node__val, left__val, right__val))


############################################################
#   Test `TreeNode`
############################################################


class TestTreeNode(unittest.TestCase):

    def test_node_val_is_correct(self):

        ((node, __, __), (node__val, __, __)) = _random_TreeNode()

        self.assertEqual(node.val, node__val)

        return

    def test_left_val_is_correct(self):

        ((node, __, __), (__, left__val, __)) = _random_TreeNode()

        self.assertEqual(node.left.val, left__val)

        return

    def test_right_val_is_correct(self):

        ((node, __, __), (__, __, right__val)) = _random_TreeNode()

        self.assertEqual(node.right.val, right__val)

        return

    def test_left_None_works(self):

        ((node, __, __), __) = _random_TreeNode()
        node.left = None

        self.assertIs(node.left, None)

        return

    def test_right_None_works(self):

        ((node, __, __), __) = _random_TreeNode()
        node.right = None

        self.assertIs(node.right, None)

        return


############################################################
#   Test `tree_from_data`
############################################################


class TestTreeFromData(unittest.TestCase):

    def test_tree_data_of_None_gives_root_None(self):

        root = tree_from_data(None)

        self.assertIs(root, None)

        return

    def test_node_data_of_None_gives_node_None(self):

        node__data = None

        root = tree_from_data([node__data])

        self.assertIs(root, None)

        return

    def test_left_data_of_None_gives_left_None(self):

        node__data = _random_val()
        left__data = None
        right__data = _random_val()

        root = tree_from_data([node__data, left__data, right__data])

        self.assertIs(root.left, None)

        return

    def test_right_data_of_None_gives_right_None(self):

        node__data = _random_val()
        left__data = _random_val()
        right__data = None

        root = tree_from_data([node__data, left__data, right__data])

        self.assertIs(root.right, None)

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

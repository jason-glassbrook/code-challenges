#!python3

############################################################

from typing import Union

from leetcode.tools.binary_tree import TreeNode

#-----------------------------------------------------------


class Solution:

    MAIN = "invertTree"

    def invertTree(self, root: TreeNode) -> TreeNode:

        return self.invertTree__iterative__breadth_first(root)

    def invertTree__recursive(self, root: TreeNode) -> TreeNode:
        """
        Solution to "invert binary tree" that...
        -   Uses recursion.
        """

        # I personally like using local functions instead of `self.<function>`.
        def invert_tree(node: Union[TreeNode, None]) -> Union[TreeNode, None]:

            if node:

                # Swap the left and right branches.
                # We must perform a simultaneous swap or else overwrite a branch.
                # [Otherwise, we could use a temporary variable.]
                (
                    node.left,
                    node.right,
                ) = (
                    invert_tree(node.right),
                    invert_tree(node.left),
                )

            return node

        # Use our local function.
        return invert_tree(root)

    def invertTree__iterative__depth_first(self, root: TreeNode) -> TreeNode:
        """
        Solution to "invert binary tree" that...
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a stack.
        """

        from collections import deque as Deck

        # If `root` is falsy, we can skip everything.
        if not root:
            return root

        stack = Deck([root])

        while stack:

            # Pop!
            node = stack.pop()

            # Swap the left and right branches.
            # We must perform a simultaneous swap or else overwrite a branch.
            # [Otherwise, we could use a temporary variable.]
            (node.left, node.right) = (node.right, node.left)

            # Put branches in stack, but only if they're truthy...
            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root

    def invertTree__iterative__breadth_first(self, root: TreeNode) -> TreeNode:
        """
        Solution to "invert binary tree" that...
        -   Uses iteration.
        -   Visits nodes in a breadth-first order by using a queue.
        """

        from collections import deque as Deck

        # If `root` is falsy, we can skip everything.
        if not root:
            return root

        queue = Deck([root])

        while queue:

            # Pop!
            node = queue.popleft()

            # Swap the left and right branches.
            # We must perform a simultaneous swap or else overwrite a branch.
            # [Otherwise, we could use a temporary variable.]
            (node.left, node.right) = (node.right, node.left)

            # Put branches in queue, but only if they're truthy...
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return root


############################################################

import unittest    # noqa: E402

from tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402

from .same_tree import Solution as SameTreeSolution    # noqa: E402

#-----------------------------------------------------------


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    is_same_tree = testing.getattr_of_instance(SameTreeSolution, SameTreeSolution.MAIN)

    def run_test__is_same_tree(
        self,
        p: Union[TreeNode, None],
        q: Union[TreeNode, None],
        answer: bool = True,
    ):

        return self.run_test(
            args=[p],
            transform_result=self.is_same_tree,
            transform_result__rest=[q],
            answer=answer,
        )

    def test_example_1(self):

        return self.run_test__is_same_tree(
            tree_from_data([
                4,
                [2, 1, 3],
                [7, 6, 9],
            ]),
            tree_from_data([
                4,
                [7, 9, 6],
                [2, 3, 1],
            ]),
        )

    def test_empty_tree(self):

        return self.run_test__is_same_tree(
            tree_from_data([]),
            tree_from_data([]),
        )

    def test_tree_of_depth_1(self):

        return self.run_test__is_same_tree(
            tree_from_data(["A", None, None]),
            tree_from_data(["A", None, None]),
        )

    def test_tree_of_depth_2(self):

        return self.run_test__is_same_tree(
            tree_from_data(["A", "B", "C"]),
            tree_from_data(["A", "C", "B"]),
        )

    def test_tree_of_depth_3(self):

        return self.run_test__is_same_tree(
            tree_from_data([
                "A",
                ["B", "D", "E"],
                ["C", "F", "G"],
            ]),
            tree_from_data([
                "A",
                ["C", "G", "F"],
                ["B", "E", "D"],
            ]),
        )

    def test_tree_of_depth_4(self):

        return self.run_test__is_same_tree(
            tree_from_data([
                "A",
                [
                    "B",
                    ["D", "H", "I"],
                    ["E", "J", "K"],
                ],
                [
                    "C",
                    ["F", "L", "M"],
                    ["G", "N", "O"],
                ],
            ]),
            tree_from_data([
                "A",
                [
                    "C",
                    ["G", "O", "N"],
                    ["F", "M", "L"],
                ],
                [
                    "B",
                    ["E", "K", "J"],
                    ["D", "I", "H"],
                ],
            ]),
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

#!python3

############################################################

from typing import Optional
from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "isSameTree"

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return self.isSameTree__iterative__depth_first(p, q)

    ############################################################
    #   Strategies
    ############################################################

    def isSameTree__recursive(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Solution to "is same tree" that...
        -   Uses recursion.
        -   Performs a depth-first comparision of the trees (because the call stack is depth-first).
        """

        def test_branch(p: TreeNode, q: TreeNode) -> bool:

            result = self.is_same_branch(p, q)

            if result is not None:
                return result

            else:
                return test_branch(p.left, q.left) and test_branch(p.right, q.right)

        return test_branch(p, q)

    def isSameTree__iterative__depth_first(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Solution to "is same tree" that...
        -   Uses iteration.
        -   Performs a depth-first comparision of the trees by with a stack.
        """

        from collections import deque as Deck

        stack = Deck([(p, q)])

        while stack:

            p, q = stack.pop()

            result = self.is_same_branch(p, q)

            if result is False:
                return result

            elif result is None:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

        return True

    ############################################################
    #   Common Tools
    ############################################################

    def is_same_branch(self, p: TreeNode, q: TreeNode) -> Optional[bool]:

        # If both are empty trees, they are the same.
        if not p and not q:
            return True

        # Now, if only one is empty, they are not the same.
        # If we got here, then we ruled out both being empty.
        if not p or not q:
            return False

        # Now, both must be non-empty...

        # If their values are not equal, they are not the same. (Duh!)
        if p.val != q.val:
            return False

        # Inconclusive.
        # We must test if both their left and right branches are equal.
        return None


############################################################

import unittest    # noqa: E402

from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    def test_example_1(self):

        return self.run_test(
            args=[
                tree_from_data([1, 2, 3]),
                tree_from_data([1, 2, 3]),
            ],
            answer=True,
        )

    def test_example_2(self):

        return self.run_test(
            args=[
                tree_from_data([1, 2, None]),
                tree_from_data([1, None, 2]),
            ],
            answer=False,
        )

    def test_example_3(self):

        return self.run_test(
            args=[
                tree_from_data([1, 2, 1]),
                tree_from_data([1, 1, 2]),
            ],
            answer=False,
        )

    def test_empty_trees(self):

        return self.run_test(
            args=[
                tree_from_data([]),
                tree_from_data([]),
            ],
            answer=True,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

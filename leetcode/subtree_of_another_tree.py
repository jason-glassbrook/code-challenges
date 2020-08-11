#!python3

############################################################

from typing import Union

from leetcode.tools.binary_tree import TreeNode

#-----------------------------------------------------------


class Solution:

    MAIN = "isSubtree"

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        pass

    def isSubtree__recursive(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Solution to "subtree of another tree" that...
        -   Uses recursion.
        """

        pass

    def isSubtree__iterative__depth_first(self, root: TreeNode) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a queue.
        """

        from collections import deque as Deck

        pass

    def isSubtree__iterative__breadth_first(self, root: TreeNode) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Uses iteration.
        -   Visits nodes in a breadth-first order by using a queue.
        """

        from collections import deque as Deck

        pass


############################################################

import unittest    # noqa: E402

from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402

#-----------------------------------------------------------


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    def test_example_1(self):

        return self.run_test(
            args=[
                tree_from_data([3, [4, 1, 2], 5]),
                tree_from_data([4, 1, 2]),
            ],
            answer=True,
        )

    def test_example_2(self):

        return self.run_test(
            args=[
                tree_from_data([3, [4, 1, [2, 0, None]], 5]),
                tree_from_data([4, 1, 2]),
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

    def test_equal_trees_of_depth_1(self):

        return self.run_test(
            args=[
                tree_from_data([1, None, None]),
                tree_from_data([1, None, None]),
            ],
            answer=True,
        )

    def test_unequal_trees_of_depth_1(self):

        return self.run_test(
            args=[
                tree_from_data([1, None, None]),
                tree_from_data([2, None, None]),
            ],
            answer=False,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "lowestCommonAncestor"

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        pass


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
                tree_from_data([6, [2, 0, [4, 3, 5]], [8, 7, 9]]),
                2,
                8,
            ],
            answer=6,
        )

    def test_example_2(self):

        return self.run_test(
            args=[
                tree_from_data([6, [2, 0, [4, 3, 5]], [8, 7, 9]]),
                2,
                4,
            ],
            answer=2,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

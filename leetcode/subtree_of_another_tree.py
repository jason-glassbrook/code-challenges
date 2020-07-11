#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "isSubtree"

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        pass


############################################################

import unittest    # noqa: E402

from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    def example_1(self):

        return self.run_test(
            args=[
                tree_from_data([3, [4, 1, 2], 5]),
                tree_from_data([4, 1, 2]),
            ],
            answer=True,
        )

    def example_2(self):

        return self.run_test(
            args=[
                tree_from_data([3, [4, 1, [2, 0, None]], 5]),
                tree_from_data([4, 1, 2]),
            ],
            answer=False,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

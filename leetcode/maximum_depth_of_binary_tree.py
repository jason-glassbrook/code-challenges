#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "maxDepth"

    def maxDepth(self, root: TreeNode) -> int:

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
                tree_from_data([3, [9, None, None], [20, 15, 7]]),
            ],
            answer=3,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

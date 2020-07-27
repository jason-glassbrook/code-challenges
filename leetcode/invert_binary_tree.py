#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "invertTree"

    def invertTree(self, root: TreeNode) -> TreeNode:

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
                tree_from_data([4, [2, 1, 3], [7, 6, 9]]),
            ],
            answer=[
                tree_from_data([4, [7, 6, 9], [2, 3, 1]]),
            ],
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

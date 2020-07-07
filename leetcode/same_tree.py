#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return True


############################################################

import unittest    # noqa: E402
from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = "isSameTree"

    def test_example_1(self):

        self.run_example(
            args=[
                tree_from_data([1, 2, 3]),
                tree_from_data([1, 2, 3]),
            ],
            answer=True,
        )

        return

    def test_example_2(self):

        self.run_example(
            args=[
                tree_from_data([1, 2, None]),
                tree_from_data([1, None, 2]),
            ],
            answer=False,
        )

        return

    def test_example_3(self):

        self.run_example(
            args=[
                tree_from_data([1, 2, 1]),
                tree_from_data([1, 1, 2]),
            ],
            answer=False,
        )

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

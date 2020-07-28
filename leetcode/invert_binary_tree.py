#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "invertTree"

    def invertTree(self, root: TreeNode) -> TreeNode:

        pass


############################################################

from typing import Optional    # noqa: E402
import unittest    # noqa: E402

from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402

from .same_tree import Solution as SameTreeSolution    # noqa: E402


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    is_same_tree = testing.getattr_of_instance(SameTreeSolution, SameTreeSolution.MAIN)

    def run_test__is_same_tree(
        self,
        p: Optional[TreeNode],
        q: Optional[TreeNode],
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
            tree_from_data([4, [2, 1, 3], [7, 6, 9]]),
            tree_from_data([4, [7, 6, 9], [2, 3, 1]]),
        )

    def test_empty_tree(self):

        return self.run_test__is_same_tree(
            tree_from_data([]),
            tree_from_data([]),
        )

    def test_tree_of_depth_1(self):

        return self.run_test__is_same_tree(
            tree_from_data([1, None, None]),
            tree_from_data([1, None, None]),
        )

    def test_tree_of_depth_2(self):

        return self.run_test__is_same_tree(
            tree_from_data([2, 1, 3]),
            tree_from_data([2, 3, 1]),
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

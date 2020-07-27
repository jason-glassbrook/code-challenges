#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "maxDepth"

    def maxDepth(self, root: TreeNode) -> int:

        return self.maxDepth__recursive__adding(root)

    def maxDepth__recursive__adding(self, root: TreeNode) -> int:

        def get_depth_of_branch(node: TreeNode) -> int:

            if node is None:
                return 0

            depth_of_left = get_depth_of_branch(node.left)
            depth_of_right = get_depth_of_branch(node.right)
            depth_of_branch = 1 + max(depth_of_left, depth_of_right)

            return depth_of_branch

        return get_depth_of_branch(root)


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
                tree_from_data([3, [9, None, None], [20, 15, 7]]),
            ],
            answer=3,
        )

    def test_empty_tree(self):

        return self.run_test(
            args=[
                tree_from_data([]),
            ],
            answer=0,
        )

    def test_tree_of_depth_1(self):

        return self.run_test(
            args=[
                tree_from_data([1, None, None]),
            ],
            answer=1,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

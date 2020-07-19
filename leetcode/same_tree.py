#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode


class Solution:

    MAIN = "isSameTree"

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return self.isSameTree__recursive(p, q)

    def isSameTree__recursive(self, p: TreeNode, q: TreeNode) -> bool:

        def test_branch(p: TreeNode, q: TreeNode) -> bool:

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

            # We must test if both their left and right branches are equal.
            else:
                return test_branch(p.left, q.left) and test_branch(p.right, q.right)

        return test_branch(p, q)


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

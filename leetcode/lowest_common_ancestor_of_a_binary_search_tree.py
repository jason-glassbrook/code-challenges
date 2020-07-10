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


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

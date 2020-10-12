#!python3

############################################################

from typing import Union

from leetcode.tools.binary_tree import TreeNode

MaybeTreeNode = Union[TreeNode, None]

#-----------------------------------------------------------


class Solution:

    MAIN = "isSubtree"

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        return self.isSubtree__recursive(s, t)

    ############################################################
    #   Strategies
    ############################################################

    def isSubtree__recursive(self, s: TreeNode, t: TreeNode) -> bool:
        """
        Solution to "subtree of another tree" that...
        -   Uses recursion.
        """

        def is_same_tree(p: MaybeTreeNode, q: MaybeTreeNode) -> bool:
            """Tests `is_same_tree` recursively."""

            # Test if branches `p` and `q` are conclusively the same.
            they_match = self.is_same_branch(p, q)

            # If conclusive, then return the result.
            if they_match is not None:
                return they_match

            # Else, test the left and right branches of `p` and `q`.
            return (is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right))

        def test_subtree(s: MaybeTreeNode, t: MaybeTreeNode) -> bool:
            """Traverses `s` and compares with `t` until they match or `s` is fully traversed."""

            # If there's no `s` and `t` isn't, then `t` can't be a subtree of `s`.
            if s is None and t is not None:
                return False

            # Else, test...
            # -   If `s` and `t` are the same, then `t` is a subtree of `s`.
            # -   If `t` is a subtree of `s`'s left branch.
            # -   If `t` is a subtree of `s`'s right branch.
            return (
                is_same_tree(s, t) or test_subtree(s.left, t) or test_subtree(s.right, t)
            )

        # Do it!
        return test_subtree(s, t)

    def isSubtree__iterative__depth_first(self, s: TreeNode, t: TreeNode) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a queue.
        """

        from collections import deque as Deck

        def is_same_tree(p: MaybeTreeNode, q: MaybeTreeNode) -> bool:
            """Tests `is_same_tree` iteratively, depth-first."""

            pass

        pass

    def isSubtree__iterative__breadth_first(self, s: TreeNode, t: TreeNode) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Uses iteration.
        -   Visits nodes in a breadth-first order by using a queue.
        """

        from collections import deque as Deck

        def is_same_tree(p: MaybeTreeNode, q: MaybeTreeNode) -> bool:
            """Tests `is_same_tree` iteratively, breadth-first."""

            pass

        pass

    ############################################################
    #   Common Tools
    ############################################################

    def is_same_branch(
        self,
        p: MaybeTreeNode,
        q: MaybeTreeNode,
    ) -> Union[bool, None]:

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

        # Inconclusive.
        # We must test if both their left and right branches are equal.
        return None


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

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

            # Test if current `s` and `t` are the same tree (`t` is a subtree of `s`).
            found_subtree = is_same_tree(s, t)

            # If not found, then test the left and right branches of `s`.
            if s and not found_subtree:
                return test_subtree(s.left, t) or test_subtree(s.right, t)

            # Else, return findings.
            return found_subtree

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

            stack = Deck([(p, q)])
            they_match = None

            while stack and they_match is not False:

                (p, q) = stack.pop()

                # Test if the branches match.
                they_match = self.is_same_branch(p, q)

                # If inconclusive, then append the left and right branches of `p` and `q` for testing.
                if they_match is None:
                    stack.append((p.left, q.left))
                    stack.append((p.right, q.right))

            # By here, `they_match` must be `True` or `False`.
            return they_match

        #-----------------------------------------------------------

        stack = Deck([s])
        found_subtree = False

        while stack and found_subtree is not True:

            s = stack.pop()

            # Test if current `s` and `t` are the same tree (`t` is a subtree of `s`).
            found_subtree = is_same_tree(s, t)

            # If not found, then append the left and right branches of `s` for testing.
            if s and not found_subtree:
                stack.append(s.left)
                stack.append(s.right)

        return found_subtree

    def isSubtree__iterative__breadth_first(self, s: TreeNode, t: TreeNode) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Uses iteration.
        -   Visits nodes in a breadth-first order by using a queue.
        """

        from collections import deque as Deck

        def is_same_tree(p: MaybeTreeNode, q: MaybeTreeNode) -> bool:
            """Tests `is_same_tree` iteratively, breadth-first."""

            queue = Deck([(p, q)])
            they_match = None

            while queue and they_match is not False:

                (p, q) = queue.popleft()

                # Test if the branches match.
                they_match = self.is_same_branch(p, q)

                # If inconclusive, then append the left and right branches of `p` and `q` for testing.
                if they_match is None:
                    queue.append((p.left, q.left))
                    queue.append((p.right, q.right))

            # By here, `they_match` must be `True` or `False`.
            return they_match

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

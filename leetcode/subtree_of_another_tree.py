#!python3

############################################################

from typing import Union

from leetcode.tools.binary_tree import TreeNode

MaybeTreeNode = Union[TreeNode, None]

#-----------------------------------------------------------


class Solution:

    MAIN = "isSubtree"

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        return self.isSubtree__trees_as_strings__iterative(s, t)

    ############################################################
    #   Strategies
    #-----------------------------------------------------------
    # -   Comparing Nodes
    #     -   Recursive
    #     -   Iterative, Depth-First
    #     -   Iterative, Breadth-First
    # -   Trees As Strings
    #     -   Recursive
    #     -   Iterative (Depth-First)
    ############################################################

    ########################################
    #   Comparing Nodes
    ########################################

    def isSubtree__comparing_nodes__recursive(
        self,
        s: TreeNode,
        t: TreeNode,
    ) -> bool:
        """
        Solution to "subtree of another tree" that...
        -   Compares tree nodes.
        -   Uses recursion.
        """

        def is_same_tree(p: MaybeTreeNode, q: MaybeTreeNode) -> bool:
            """Tests `is_same_tree` recursively."""

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

        #---------------------------------------

        # Do it!
        return test_subtree(s, t)

    def isSubtree__comparing_nodes__iterative__depth_first(
        self,
        s: TreeNode,
        t: TreeNode,
    ) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Compares tree nodes.
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a queue.
        """

        from collections import deque as Deck

        def is_same_tree(p: MaybeTreeNode, q: MaybeTreeNode) -> bool:
            """Tests `is_same_tree` iteratively, depth-first."""

            stack = Deck([(p, q)])

            while stack:

                (p, q) = stack.pop()

                # If both are empty trees, they are the same.
                if not p and not q:
                    continue

                # Now, if only one is empty, they are not the same.
                # If we got here, then we ruled out both being empty.
                if not p or not q:
                    return False

                # Now, both must be non-empty...

                # If their values are not equal, they are not the same. (Duh!)
                if p.val != q.val:
                    return False

                # Else, then append the left and right branches of `p` and `q` for testing.
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))

            return True

        #---------------------------------------

        stack = Deck([s])

        while stack:

            s = stack.pop()

            # Test if the local `s` and `t` are the same tree (`t` is a subtree of `s`).
            they_match = is_same_tree(s, t)

            # If we found a match, then return.
            if they_match:
                return True

            # Else, if there's more to the local `s`, then append the left and right branches of `s` for testing.
            elif s:
                stack.append(s.left)
                stack.append(s.right)

        return False

    def isSubtree__comparing_nodes__iterative__breadth_first(
        self,
        s: TreeNode,
        t: TreeNode,
    ) -> TreeNode:
        """
        Solution to "subtree of another tree" that...
        -   Compares tree nodes.
        -   Uses iteration.
        -   Visits nodes in a breadth-first order by using a queue.
        """

        from collections import deque as Deck

        def is_same_tree(p: MaybeTreeNode, q: MaybeTreeNode) -> bool:
            """Tests `is_same_tree` iteratively, breadth-first."""

            queue = Deck([(p, q)])

            while queue:

                (p, q) = queue.popleft()

                # If both are empty trees, they are the same.
                if not p and not q:
                    continue

                # Now, if only one is empty, they are not the same.
                # If we got here, then we ruled out both being empty.
                if not p or not q:
                    return False

                # Now, both must be non-empty...

                # If their values are not equal, they are not the same. (Duh!)
                if p.val != q.val:
                    return False

                # Else, then append the left and right branches of `p` and `q` for testing.
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))

            return True

        #---------------------------------------

        queue = Deck([s])

        while queue:

            s = queue.popleft()

            # Test if the local `s` and `t` are the same tree (`t` is a subtree of `s`).
            they_match = is_same_tree(s, t)

            # If we found a match, then return.
            if they_match:
                return True

            # Else, if there's more to the local `s`, then append the left and right branches of `s` for testing.
            elif s:
                queue.append(s.left)
                queue.append(s.right)

        return False

    ########################################
    #   Trees As Strings
    ########################################

    def isSubtree__trees_as_strings__recursive(
        self,
        s: TreeNode,
        t: TreeNode,
    ) -> bool:
        """
        Solution to "subtree of another tree" that...
        -   Converts trees to strings.
        -   Checks if `t`'s string is a substring of `s`'s string.
        -   Uses recursion.
        """

        def tree_as_string(n: MaybeTreeNode) -> str:
            """Builds a string from `n` in NLR order, recursively."""

            if n is None:
                return "~"

            return f"[{n.val} {tree_as_string(n.left)} {tree_as_string(n.right)}]"

        #---------------------------------------

        # Do it!
        return tree_as_string(t) in tree_as_string(s)

    def isSubtree__trees_as_strings__iterative(
        self,
        s: TreeNode,
        t: TreeNode,
    ) -> bool:
        """
        Solution to "subtree of another tree" that...
        -   Converts trees to strings.
        -   Checks if `t`'s string is a substring of `s`'s string.
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a queue.

        NOTE: While a breadth-first solution may be possible, it is not easy with this strategy.
        So I'm not going to attempt that...
        """

        from collections import deque as Deck

        def tree_as_string(n: MaybeTreeNode) -> str:
            """Builds a string from `n` in NLR order, iteratively."""

            stack = Deck([(n, 0)])
            result = ""

            while stack:

                (n, right_count) = stack.pop()
                # ⬆ We are tracking the number of "rights" we've taken so we can balance brackets.

                if n is None:
                    result += " ~" + ("]" * right_count)

                else:
                    result += f" [{n.val}"
                    stack.append((n.right, right_count + 1))
                    stack.append((n.left, 0))

            return result[1 ::]
            # ⬆ Removes initial space.

        #---------------------------------------

        # Do it!
        return tree_as_string(t) in tree_as_string(s)


############################################################

import unittest    # noqa: E402

from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402

#---------------------------------------


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

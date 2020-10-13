#!python3

############################################################

from typing import Union

from leetcode.tools.binary_tree import TreeNode

MaybeTreeNode = Union[TreeNode, None]

#-----------------------------------------------------------


class Solution:

    MAIN = "isSameTree"

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return self.isSameTree__comparing_nodes__recursive(p, q)

    ############################################################
    #   Strategies
    #-----------------------------------------------------------
    # -   Comparing Nodes
    #     -   Recursive
    #     -   Iterative, Depth-First
    #     -   Iterative, Breadth-First
    # -   Trees As Strings
    #     -   Recursive
    #     -   Iterative, Depth-First
    #     -   Iterative, Breadth-First
    ############################################################

    ########################################
    #   Comparing Nodes
    ########################################

    def isSameTree__comparing_nodes__recursive(
        self,
        p: TreeNode,
        q: TreeNode,
    ) -> bool:
        """
        Solution to "is same tree" that...
        -   Uses recursion.
        -   Performs a depth-first comparision of the trees (because the call stack is depth-first).
        """

        def test_branch(
            p: MaybeTreeNode,
            q: MaybeTreeNode,
        ) -> bool:

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
            return test_branch(p.left, q.left) and test_branch(p.right, q.right)

        return test_branch(p, q)

    def isSameTree__comparing_nodes__iterative__depth_first(
        self,
        p: TreeNode,
        q: TreeNode,
    ) -> bool:
        """
        Solution to "is same tree" that...
        -   Uses iteration.
        -   Performs a depth-first comparision of the trees by with a stack.
        """

        from collections import deque as Deck

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

    def isSameTree__comparing_nodes__iterative__breadth_first(
        self,
        p: TreeNode,
        q: TreeNode,
    ) -> bool:
        """
        Solution to "is same tree" that...
        -   Uses iteration.
        -   Performs a breadth-first comparision of the trees by with a queue.
        """

        from collections import deque as Deck

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

    ########################################
    #   Trees As Strings
    ########################################

    def isSameTree__trees_as_strings__recursive(
        self,
        p: TreeNode,
        q: TreeNode,
    ) -> bool:
        """
        Solution to "is same tree" that...
        -   Converts trees to strings.
        -   Checks if `p`'s string is a substring of `q`'s string.
        -   Uses recursion.
        """

        pass

        def tree_as_string(n: MaybeTreeNode) -> str:
            """Builds a string from `n` in NLR order, recursively."""

            if n is None:
                return "~"

            return f"{n.val} {tree_as_string(n.left)} {tree_as_string(n.right)}"

        #---------------------------------------

        # Do it!
        return tree_as_string(p) == tree_as_string(q)

    def isSameTree__trees_as_strings__iterative__depth_first(
        self,
        p: TreeNode,
        q: TreeNode,
    ) -> bool:
        """
        Solution to "is same tree" that...
        -   Converts trees to strings.
        -   Checks if `p`'s string is a substring of `q`'s string.
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a queue.
        """

        pass

        from collections import deque as Deck

        def tree_as_string(n: MaybeTreeNode) -> str:
            """Builds a string from `n` in DFT-NLR order, iteratively."""

            stack = Deck([n])
            result = ""

            while stack:

                n = stack.pop()

                if n is None:
                    result += " ~"

                else:
                    result += f" {n.val}"
                    stack.append(n.right)
                    stack.append(n.left)

            return result[1 ::]
            # ⬆ Removes initial space.

        #---------------------------------------

        # Do it!
        return tree_as_string(p) == tree_as_string(q)

    def isSameTree__trees_as_strings__iterative__breadth_first(
        self,
        p: TreeNode,
        q: TreeNode,
    ) -> bool:
        """
        Solution to "is same tree" that...
        -   Converts trees to strings.
        -   Checks if `p`'s string is a substring of `q`'s string.
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a queue.
        """

        pass

        from collections import deque as Deck

        def tree_as_string(n: MaybeTreeNode) -> str:
            """Builds a string from `n` in BFT-LR order, iteratively."""

            queue = Deck([n])
            result = ""

            while queue:

                n = queue.popleft()

                if n is None:
                    result += " ~"

                else:
                    result += f" {n.val}"
                    queue.append(n.left)
                    queue.append(n.right)

            return result[1 ::]
            # ⬆ Removes initial space.

        #---------------------------------------

        # Do it!
        return tree_as_string(p) == tree_as_string(q)


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

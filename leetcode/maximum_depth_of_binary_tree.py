#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode

#-----------------------------------------------------------


class Solution:

    MAIN = "maxDepth"

    def maxDepth(self, root: TreeNode) -> int:

        return self.maxDepth__iterative__depth_first(root)

    def maxDepth__recursive__adding(self, root: TreeNode) -> int:
        """
        Solution to "maximum depth of binary tree" that...
        -   Uses recursion.
        -   Adds recursively found depths with base case of 0.
        """

        def get_depth_of_branch(node: TreeNode) -> int:

            depth_of_left = depth_of_right = 0

            if node.left:
                depth_of_left = get_depth_of_branch(node.left)

            if node.right:
                depth_of_right = get_depth_of_branch(node.right)

            depth_of_branch = 1 + max(depth_of_left, depth_of_right)

            return depth_of_branch

        if not root:
            return 0

        return get_depth_of_branch(root)

    def maxDepth__recursive__drilling(self, root: TreeNode) -> int:
        """
        Solution to "maximum depth of binary tree" that...
        -   Uses recursion.
        -   "Drills" the current depth into each branch and adds to it if more nodes are found.
        """

        def get_depth_of_branch(node: TreeNode, depth: int) -> int:

            depth_of_left = depth_of_right = depth

            if node.left:
                depth_of_left = get_depth_of_branch(node.left, depth)

            if node.right:
                depth_of_right = get_depth_of_branch(node.right, depth)

            depth_of_branch = 1 + max(depth_of_left, depth_of_right)

            return depth_of_branch

        if not root:
            return 0

        return get_depth_of_branch(root, 0)

    def maxDepth__iterative__depth_first(self, root: TreeNode) -> int:
        """
        Solution to "maximum depth of binary tree" that...
        -   Uses iteration.
        -   Visits nodes in a depth-first order by using a stack.
        """

        from collections import deque as Deck

        #---------------------------------------

        max_depth = 0

        if not root:
            return max_depth

        stack = Deck([(root, 1)])

        while stack:

            node, depth = stack.pop()
            next_depth = depth + 1

            if node.left:
                stack.append((node.left, next_depth))

            if node.right:
                stack.append((node.right, next_depth))

            max_depth = max(max_depth, depth)

        return max_depth

    def maxDepth__iterative__breadth_first(self, root: TreeNode) -> int:
        """
        Solution to "maximum depth of binary tree" that...
        -   Uses iteration.
        -   Visits nodes in a breadth-first order by using a queue.
        """

        from collections import deque as Deck

        #---------------------------------------

        max_depth = 0

        if not root:
            return max_depth

        queue = Deck([(root, 1)])

        while queue:

            node, depth = queue.popleft()
            next_depth = depth + 1

            if node.left:
                queue.append((node.left, next_depth))

            if node.right:
                queue.append((node.right, next_depth))

            max_depth = max(max_depth, depth)

        return max_depth


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

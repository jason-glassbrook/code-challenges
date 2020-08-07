#!python3

############################################################

from leetcode.tools.binary_tree import TreeNode

#-----------------------------------------------------------


class Solution:

    MAIN = "lowestCommonAncestor"

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        pass


############################################################

import unittest    # noqa: E402

from typing import Any    # noqa: E402

from leetcode.tools import testing    # noqa: E402
from leetcode.tools.binary_tree import tree_from_data    # noqa: E402

#-----------------------------------------------------------


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    def get_val(self, node: Union[TreeNode, None]) -> Any:

        return (node.val if node else None)

    def run_test__is_same_node(
        self,
        args: Any,
        answer: Any,
    ):

        (tree_data, p_data, q_data) = args

        root = tree_from_data(tree_data)
        p = TreeNode(p_data) if p_data else None
        q = TreeNode(q_data) if q_data else None

        return self.run_test(
            args=[root, p, q],
            transform_result=self.get_val,
            answer=answer,
        )

    def test_example_1(self):

        return self.run_test__is_same_node(
            args=[
                [6, [2, 0, [4, 3, 5]], [8, 7, 9]],
                2,
                8,
            ],
            answer=6,
        )

    def test_example_2(self):

        return self.run_test__is_same_node(
            args=[
                [6, [2, 0, [4, 3, 5]], [8, 7, 9]],
                2,
                4,
            ],
            answer=2,
        )

    def test_empty_tree(self):

        return self.run_test__is_same_node(
            args=[
                [],
                1,
                2,
            ],
            answer=None,
        )

    def test_tree_of_depth_1(self):

        return self.run_test__is_same_node(
            args=[
                [1],
                1,
                None,
            ],
            answer=None,
        )

    def test_tree_of_depth_2(self):

        return self.run_test__is_same_node(
            args=[
                [1, 2, None],
                1,
                2,
            ],
            answer=1,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

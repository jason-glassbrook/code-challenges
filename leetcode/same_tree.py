#!python3

############################################################

from typing import Optional, Iterable


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, value=0, left=None, right=None):

        self.value = value
        self.left = left
        self.right = right

        return


# Deserialize a tree.
def tree_from_data(data: Optional[Iterable]):
    """
    Deserialize a binary tree from `data`, which should be of the form `[n, l, r]` or `None`,
    -   where `n` is a scalar value,
    -   where `l` and `r` may be `[n, l, r]`, scalar, or `None`.
    """

    def branch(value, left, right):

        return TreeNode(
            value,
            branch(*left) if isinstance(left, Iterable) else left,
            branch(*right) if isinstance(right, Iterable) else right,
        )

    return branch(*data) if isinstance(data, Iterable) else None


############################################################


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        return True


############################################################

import unittest    # noqa: E402


class TestSolution(unittest.TestCase):

    def _run_solution(self, *args):

        return Solution().isSameTree(*args)

    def _run_example(self, args, answer):

        result = self._run_solution(*args)

        self.assertEqual(result, answer)

        return

    def test_example_1(self):

        self._run_example(
            args=[
                tree_from_data([1, 2, 3]),
                tree_from_data([1, 2, 3]),
            ],
            answer=True,
        )

        return

    def test_example_2(self):

        self._run_example(
            args=[
                tree_from_data([1, 2, None]),
                tree_from_data([1, None, 2]),
            ],
            answer=False,
        )

        return

    def test_example_3(self):

        self._run_example(
            args=[
                tree_from_data([1, 2, 1]),
                tree_from_data([1, 1, 2]),
            ],
            answer=False,
        )

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

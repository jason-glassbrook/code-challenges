#!python3

############################################################


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return True


############################################################

import unittest    # noqa: E402
import random    # noqa: E402


class TestSolution(unittest.TestCase):

    def _run_solution(self, *args):

        return Solution().isSameTree(*args)

    def test_example_1(self):

        trees = [
            [1, 2, 3],
            [1, 2, 3],
        ]
        answer = True

        result = self._run_solution(*trees)

        self.assertEqual(result, answer)

        return

    def test_example_2(self):

        trees = [
            [1, 2, None],
            [1, None, 2],
        ]
        answer = True

        result = self._run_solution(*trees)

        self.assertEqual(result, answer)

        return

    def test_example_3(self):

        trees = [
            [1, 2, 1],
            [1, 1, 2],
        ]
        answer = True

        result = self._run_solution(*trees)

        self.assertEqual(result, answer)

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

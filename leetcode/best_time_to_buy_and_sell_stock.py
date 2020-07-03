#!python3

############################################################

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        return 0


############################################################

import unittest    # noqa: E402


class TestSolution(unittest.TestCase):

    def _run_solution(self, args):

        return Solution().maxProfit(*args)

    def test_example_1(self):

        args = [[7, 1, 5, 3, 6, 4]]
        answer = 5

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    def test_example_2(self):

        args = [[7, 6, 4, 3, 1]]
        answer = 0

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    def test_empty_list(self):

        args = [[]]
        answer = 0

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

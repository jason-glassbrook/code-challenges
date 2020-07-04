#!python3

############################################################

from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        return 0


############################################################

import unittest    # noqa: E402
import random    # noqa: E402


class TestSolution(unittest.TestCase):

    _MIN_VALUE = 0
    _MAX_VALUE = 100
    _LENGTH = 10

    def _run_solution(self, *args):

        return Solution().maxProfit(*args)

    def test_example_1(self):

        series = [7, 1, 5, 3, 6, 4]
        answer = 5

        result = self._run_solution(series)

        self.assertEqual(result, answer)

        return

    def test_example_2(self):

        series = [7, 6, 4, 3, 1]
        answer = 0

        result = self._run_solution(series)

        self.assertEqual(result, answer)

        return

    def test_empty_series(self):

        series = []
        answer = 0

        result = self._run_solution(series)

        self.assertEqual(result, answer)

        return

    def test_flat_series(self):

        series = [random.randint(self._MIN_VALUE, self._MAX_VALUE)] * self._LENGTH
        answer = 0

        result = self._run_solution([series])

        self.assertEqual(result, answer)

        return

    def test_all_ascending_series(self):

        series = list(range(self._MIN_VALUE, self._MAX_VALUE + 1, +1))
        answer = max(0, max(series) - min(series))

        result = self._run_solution(series)

        self.assertEqual(result, answer)

        return

    def test_all_descending_series(self):

        series = list(range(self._MAX_VALUE, self._MIN_VALUE - 1, -1))
        answer = max(0, min(series) - max(series))

        result = self._run_solution(series)

        self.assertEqual(result, answer)

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

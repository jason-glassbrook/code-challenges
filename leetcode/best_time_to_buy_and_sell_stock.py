#!python3

############################################################

from typing import List


class Solution:

    MAIN = "maxProfit"

    def maxProfit(self, prices: List[int]) -> int:

        return 0


############################################################

import unittest    # noqa: E402
import random    # noqa: E402

from leetcode.tools import testing    # noqa: E402


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN

    _MIN_VALUE = 0
    _MAX_VALUE = 100
    _LENGTH = 10

    def test_example_1(self):

        return self.run_test(
            args=[[7, 1, 5, 3, 6, 4]],
            answer=5,
        )

    def test_example_2(self):

        return self.run_test(
            args=[[7, 6, 4, 3, 1]],
            answer=0,
        )

    def test_empty_series(self):

        return self.run_test(
            args=[[]],
            answer=0,
        )

    def test_flat_series(self):

        series = [random.randint(self._MIN_VALUE, self._MAX_VALUE)] * self._LENGTH
        answer = 0

        return self.run_test(
            args=[series],
            answer=answer,
        )

    def test_all_ascending_series(self):

        series = list(range(self._MIN_VALUE, self._MAX_VALUE + 1, +1))
        answer = max(0, series[-1] - series[0])

        return self.run_test(
            args=[series],
            answer=answer,
        )

    def test_all_descending_series(self):

        series = list(range(self._MAX_VALUE, self._MIN_VALUE - 1, -1))
        answer = max(0, series[-1] - series[0])

        return self.run_test(
            args=[series],
            answer=answer,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

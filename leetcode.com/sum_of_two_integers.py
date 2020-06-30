#!python3

import unittest
import random


class TestSolution(unittest.TestCase):

    def _run_solution(self, args):
        return Solution().getSum(*args)

    def test_sum(self):

        a = random.randint(0, 0xFFFFFFFF)
        b = random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return


class Solution:

    def getSum(self, a: int, b: int) -> int:

        return self.getSum__cheating(a, b)

    def getSum__cheating(self, a: int, b: int) -> int:

        return sum((a, b))    # This is cheating!


if __name__ == "__main__":
    unittest.main()

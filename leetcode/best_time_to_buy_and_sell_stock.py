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


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

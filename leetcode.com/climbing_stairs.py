#!python3

############################################################


class Solution:

    def climbStairs(self, n: int) -> int:

        return 0


############################################################

############################################################

import unittest    # noqa: E402


class TestSolution(unittest.TestCase):

    def _run_solution(self, args):
        return Solution().climbStairs(*args)

    def test_something(self):

        args = tuple()
        answer = None

        result = self._run_solution(args)

        self.assertEquals(result, answer)

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

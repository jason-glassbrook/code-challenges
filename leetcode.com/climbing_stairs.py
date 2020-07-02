#!python3

############################################################


class Solution:

    def climbStairs(self, n: int) -> int:

        return 1


############################################################

############################################################

import unittest    # noqa: E402


class TestSolution(unittest.TestCase):

    EXAMPLES = [{
        "args": [1],
        "answer": 1,
    }, {
        "args": [2],
        "answer": 2,
    }, {
        "args": [3],
        "answer": 3,
    }, {
        "args": [4],
        "answer": 5,
    }, {
        "args": [5],
        "answer": 8,
    }, {
        "args": [6],
        "answer": 13,
    }]

    def _run_solution(self, args):
        return Solution().climbStairs(*args)

    def test_examples(self):

        for example in self.EXAMPLES:

            result = self._run_solution(example["args"])

            self.assertEqual(result, example["answer"])

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

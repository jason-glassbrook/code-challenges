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
        "args": [0],
        "answer": 1,
    }, {
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
    }, {
        "args": [7],
        "answer": 21,
    }, {
        "args": [8],
        "answer": 34,
    }, {
        "args": [9],
        "answer": 55,
    }, {
        "args": [10],
        "answer": 89,
    }, {
        "args": [11],
        "answer": 144,
    }, {
        "args": [12],
        "answer": 233,
    }, {
        "args": [13],
        "answer": 377,
    }, {
        "args": [14],
        "answer": 610,
    }, {
        "args": [15],
        "answer": 987,
    }, {
        "args": [16],
        "answer": 1597,
    }, {
        "args": [17],
        "answer": 2584,
    }, {
        "args": [18],
        "answer": 4181,
    }, {
        "args": [19],
        "answer": 6765,
    }, {
        "args": [20],
        "answer": 10946,
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

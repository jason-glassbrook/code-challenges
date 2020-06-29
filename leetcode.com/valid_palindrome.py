#!python3

import unittest
import random
import string


class TestSolution(unittest.TestCase):

    def _run_solution(self, args):

        return Solution().isPalindrome(*args)

    def test_length_0(self):

        args = ("",)
        answer = True

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_length_1(self):

        args = (random.choice(string.printable),)
        answer = True

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_example_1(self):

        args = ("A man, a plan, a canal: Panama",)
        answer = True

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_example_2(self):

        args = ("race a car",)
        answer = False

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return


class Solution:

    def isPalindrome(self, s: str) -> bool:

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters.

        return None


if __name__ == "__main__":
    unittest.main(verbosity=2)

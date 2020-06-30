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

        return self.isPalindrome__recursive(s)

    def isPalindrome__reverse_slice(self, s: str) -> bool:

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters and ignore case.
        s = "".join(c for c in s if c.isalnum()).lower()

        # Compare with reversed version.
        result = (s == s[::-1])

        return result

    def isPalindrome__reversed(self, s: str) -> bool:

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters and ignore case.
        s = "".join(c for c in s if c.isalnum()).lower()

        # Compare with reversed version.
        result = (s == "".join(reversed(s)))

        return result

    def isPalindrome__pointers(self, s: str) -> bool:

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters and ignore case.
        s = "".join(c for c in s if c.isalnum()).lower()

        # Iterate from outside to middle with left and right pointers.
        # -   If the length is even, then when we reach the middle,
        #     then we've made it to the base/trivial case of a string of length 0.
        # -   If the length is odd, then when we reach the middle,
        #     then we've made it to the base/trivial case of a string of length 1.
        for i in range(0, len(s) // 2):
            left = i    # (LEFTMOST + i) where LEFTMOST = 0
            right = (-1 - i)    # (RIGHTMOST - i) where RIGHTMOST = len(s) - 1
            if s[left] != s[right]:
                return False

        return True

    def isPalindrome__recursive(self, s: str) -> bool:
        """
        Because why not?
        """

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters and ignore case.
        s = "".join(c for c in s if c.isalnum()).lower()

        # Iterate from outside to middle with left and right pointers.
        # -   If the length is even, then when we reach the middle,
        #     then we've made it to the base/trivial case of a string of length 0.
        # -   If the length is odd, then when we reach the middle,
        #     then we've made it to the base/trivial case of a string of length 1.

        middle = len(s) // 2

        def compare_outside_to_inside(i: int) -> bool:

            # Handle trivial cases.
            if i >= middle:
                return True

            # Compare left and right.
            elif s[i] != s[-1 - i]:
                return False

            # Continue.
            else:
                return compare_outside_to_inside(i + 1)

        return compare_outside_to_inside(0)


if __name__ == "__main__":
    unittest.main(verbosity=2)

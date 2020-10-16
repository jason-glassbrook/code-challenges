#!python3

############################################################


class Solution:

    def isPalindrome(self, s: str) -> bool:

        return self.isPalindrome__pointers(s)

    def isPalindrome__reverse_slice(self, s: str) -> bool:

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters and ignore case.
        s = "".join(c.lower() for c in s if c.isalnum())

        # Compare with reversed version.
        result = (s == s[::-1])

        return result

    def isPalindrome__reversed(self, s: str) -> bool:

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters and ignore case.
        s = "".join(c.lower() for c in s if c.isalnum())

        # Compare with reversed version.
        result = (s == "".join(reversed(s)))

        return result

    def isPalindrome__pointers(self, s: str) -> bool:

        # Handle trivial cases.
        if len(s) < 2:
            return True

        # Strip non-alphanumeric characters and ignore case.
        s = "".join(c.lower() for c in s if c.isalnum())

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
        s = "".join(c.lower() for c in s if c.isalnum())

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


############################################################

############################################################

import unittest    # noqa: E402
import random    # noqa: E402
import string    # noqa: E402

from tools import testing    # noqa: E402

#-----------------------------------------------------------


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = "isPalindrome"

    def test_length_0(self):

        return self.run_test(
            args=[""],
            answer=True,
        )

    def test_length_1(self):

        return self.run_test(
            args=[random.choice(string.printable)],
            answer=True,
        )

    def test_example_1(self):

        return self.run_test(
            args=["A man, a plan, a canal: Panama"],
            answer=True,
        )

    def test_example_2(self):

        return self.run_test(
            args=["race a car"],
            answer=False,
        )


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

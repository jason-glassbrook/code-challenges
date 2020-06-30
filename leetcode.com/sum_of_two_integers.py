#!python3

import unittest
import random


class TestSolution(unittest.TestCase):

    def _run_solution(self, args):
        return Solution().getSum(*args)

    def test_both_positive(self):

        a = +random.randint(0, 0xFFFFFFFF)
        b = +random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    def test_both_negative(self):

        a = -random.randint(0, 0xFFFFFFFF)
        b = -random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    def test_positive_a_negative_b(self):

        a = +random.randint(0, 0xFFFFFFFF)
        b = -random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    def test_negative_a_positive_b(self):

        a = -random.randint(0, 0xFFFFFFFF)
        b = +random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return


class Solution:

    def getSum(self, a: int, b: int) -> int:

        return self.getSum__bitwise_operations__recursive(a, b)

    def getSum__cheating(self, a: int, b: int) -> int:

        return sum((a, b))    # This is cheating!

    def getSum__bitwise_operations__iterative(self, a: int, b: int) -> int:

        total = max(a, b)    # Initial "total"
        carry = min(a, b)    # Initial "carry" -- min of a, b for fewer iterations

        # Fiddle with bits while bits still need to be carried.
        while (carry > 0):

            # Remember the previous state.
            prev__total = total
            prev__carry = carry

            # Compute the next state.
            # -   `a XOR b` gives the bits that differ -- these don't need to be carried.
            # -   `a AND b` gives the bits that are both 1 -- these need to be carried.
            # -   `(a AND b) LSHIFT 1` carries the bits whose sum overflow the range 0 to 1.
            total = (prev__total ^ prev__carry)
            carry = (prev__total & prev__carry) << 1

        return total

    def getSum__bitwise_operations__recursive(self, a: int, b: int) -> int:
        """
        Because why not?
        """

        def __next(total: int, carry: int) -> int:

            if (carry > 0):

                return __next(
                    total=(total ^ carry),
                    carry=((total & carry) << 1),
                )

            else:

                return total

        return __next(
            total=max(a, b),    # Initial "total"
            carry=min(a, b),    # Initial "carry" -- min of a, b for fewer iterations
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)

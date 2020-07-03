#!python3

############################################################


class Solution:
    # Throughout this solution, a mask is used.
    # This is only necessary because LeetCode uses 32-bit ints, but Python can use arbitrary length ints.

    PYTHON__INT_MASK = 0xFFFFFFFFFFFFFFFF
    LEETCODE__INT_MASK = 0xFFFFFFFF

    def _modified_continue(self, total: int, carry: int, mask: int) -> bool:
        return (carry & mask)

    def _modified_return(self, total: int, carry: int, mask: int) -> int:
        return (total & mask) if carry > mask else total

    def getSum(self, a: int, b: int, mask=LEETCODE__INT_MASK) -> int:

        return self.getSum__bitwise_operations__iterative(a, b, mask)

    def getSum__cheating(self, a: int, b: int, mask: int) -> int:

        return sum((a, b))    # This is cheating!

    def getSum__bitwise_operations__iterative(self, a: int, b: int, mask: int) -> int:

        total = max(a, b)    # Initial "total"
        carry = min(a, b)    # Initial "carry" -- min of a, b for fewer iterations

        # Fiddle with bits while bits still need to be carried.
        while self._modified_continue(total, carry, mask):

            # Remember the previous state.
            prev__total = total
            prev__carry = carry

            # Compute the next state.
            # -   `a XOR b` gives the bits that differ -- these don't need to be carried.
            # -   `a AND b` gives the bits that are both 1 -- these need to be carried.
            # -   `(a AND b) LSHIFT 1` carries the bits whose sum overflow the range 0 to 1.
            total = (prev__total ^ prev__carry)
            carry = (prev__total & prev__carry) << 1

        return self._modified_return(total, carry, mask)

    def getSum__bitwise_operations__recursive(self, a: int, b: int, mask: int) -> int:
        """
        Because why not?
        """

        def __next(total: int, carry: int) -> int:

            if self._modified_continue(total, carry, mask):

                return __next(
                    total=(total ^ carry),
                    carry=((total & carry) << 1),
                )

            else:

                return self._modified_return(total, carry, mask)

        return __next(
            total=max(a, b),    # Initial "total"
            carry=min(a, b),    # Initial "carry" -- min of a, b for fewer iterations
        )


############################################################

import unittest    # noqa: E402
import random    # noqa: E402


class TestSolution(unittest.TestCase):

    def _run_solution(self, args):
        return Solution().getSum(*args, Solution.PYTHON__INT_MASK)

    def test_both_positive(self):

        a = +random.randint(0, 0xFFFFFFFF)
        b = +random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    @unittest.skip("not sure how to deal with 32 bit ints")
    def test_both_negative(self):

        a = -random.randint(0, 0xFFFFFFFF)
        b = -random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    @unittest.skip("not sure how to deal with 32 bit ints")
    def test_positive_a_negative_b(self):

        a = +random.randint(0, 0xFFFFFFFF)
        b = -random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return

    @unittest.skip("not sure how to deal with 32 bit ints")
    def test_negative_a_positive_b(self):

        a = -random.randint(0, 0xFFFFFFFF)
        b = +random.randint(0, 0xFFFFFFFF)

        args = (a, b)
        answer = (a + b)

        result = self._run_solution(args)

        self.assertEqual(result, answer)

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

#!python3

from typing import List
import unittest
import random


class TestSolution(unittest.TestCase):

    def _runner(self, args):

        return Solution().missingNumber(*args)

    def test_empty_nums(self):

        args = ([],)
        answer = 0

        result = self._runner(args)

        self.assertEqual(answer, result)

        return

    def test_length_n_missing_0(self):

        n = random.randint(1, 100)
        args = ([x for x in range(1, n + 1)],)
        answer = 0

        result = self._runner(args)

        self.assertEqual(answer, result)

        return

    def test_length_n_missing_n(self):

        n = random.randint(1, 100)
        args = ([x for x in range(0, n)],)
        answer = n

        result = self._runner(args)

        self.assertEqual(answer, result)

        return

    def test_example_1(self):

        args = ([3, 0, 1],)
        answer = 2

        result = self._runner(args)

        self.assertEqual(answer, result)

        return

    def test_example_2(self):

        args = ([9, 6, 4, 2, 3, 5, 7, 0, 1],)
        answer = 8

        result = self._runner(args)

        self.assertEqual(answer, result)

        return


class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        return self.missingNumber__xor(nums)

    def missingNumber__brute_force(self, nums: List[int]) -> int:

        n = len(nums)

        # Sort the list. Now this isn't linear time!
        nums = sorted(nums)

        # Check each number in the list:
        # - Each number should equal its index.
        # - If not, then the expected number (index) is missing.
        for expected in range(0, n):
            if nums[expected] != expected:
                return expected

        # If we made it here, then `n` is missing.
        return n

    def missingNumber__hash_set(self, nums: List[int]) -> int:

        n = len(nums)

        # Create a hash set of `nums`.
        nums_set = set(nums)

        # Check each number in the list:
        for expected in range(0, n):
            if expected not in nums_set:
                return expected

        # If we made it here, then `n` is missing.
        return n

    def missingNumber__xor(self, nums: List[int]) -> int:
        """
        This method uses XOR to find the missing number.
        I don't fully understand how it works, but it's clever.
        It sort of "bubbles" out the bits for the missing number.
        """

        n = len(nums)

        # Construct the missing number:
        missing = n
        for (i, num) in enumerate(nums):
            missing ^= i ^ num

        return missing

    def missingNumber__sum(self, nums: List[int]) -> int:

        n = len(nums)

        # Compute the expected and actual sums.
        expected_sum = n * (n + 1) // 2    # <- Gauss formula.
        actual_sum = sum(nums)
        missing = expected_sum - actual_sum

        # Maybe nothing was missing?
        return missing


if __name__ == "__main__":

    unittest.main(verbosity=2)

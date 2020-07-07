#!python3

############################################################

from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        return self.missingNumber__hash_set(nums)

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


############################################################

import unittest    # noqa: E402
import random    # noqa: E402

from leetcode.tools import testing    # noqa: E402


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = "missingNumber"

    def test_example_1(self):

        return self.run_test(
            args=[[3, 0, 1]],
            answer=2,
        )

    def test_example_2(self):

        return self.run_test(
            args=[[9, 6, 4, 2, 3, 5, 7, 0, 1]],
            answer=8,
        )

    def test_empty_nums(self):

        return self.run_test(
            args=[[]],
            answer=0,
        )

    def test_length_n_missing_0(self):

        n = random.randint(1, 100)

        return self.run_test(
            args=[[x for x in range(1, n + 1)]],
            answer=0,
        )

    def test_length_n_missing_n(self):

        n = random.randint(1, 100)

        return self.run_test(
            args=[[x for x in range(0, n)]],
            answer=n,
        )


############################################################

if __name__ == "__main__":

    unittest.main(verbosity=2)

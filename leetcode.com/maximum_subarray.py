#!python3

from typing import List


class Solution:

    DEFAULT_SUM = 0
    WORST_SUM = float("-inf")

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Caller for "maximum subarray sum".
        NOTE: The empty subarray with sum 0 is not an allowed solution.
        """

        return self.maxSubArray__brute_force__v2(nums)

    def maxSubArray__brute_force__v1(self, nums: List[int]) -> int:
        """
        Solution to "maximum subarray sum" that
        - loops through all subarrays
        - calculates the subarray sum by slicing the array
        """

        # Handle empty input `nums`.
        if not nums:
            return self.DEFAULT_SUM

        n = len(nums)
        best_sum = self.WORST_SUM
        # best_start = None
        # best_stop = None

        for start in range(0, n):

            for stop in range(start + 1, n + 1):

                curr_sum = sum(nums[start : stop])

                if curr_sum > best_sum:

                    best_sum = curr_sum
                    # best_start = start
                    # best_stop = stop

        return best_sum    # (best_sum, best_start, best_stop)

    def maxSubArray__brute_force__v2(self, nums: List[int]) -> int:
        """
        Solution to "maximum subarray sum" that
        - loops through all subarrays
        - builds the subarray sum by simple addition
        """

        # Handle empty input `nums`.
        if not nums:
            return self.DEFAULT_SUM

        n = len(nums)
        best_sum = self.WORST_SUM
        # best_start = None
        # best_stop = None

        for start in range(0, n):

            curr_sum = self.DEFAULT_SUM

            for stop in range(start + 1, n + 1):

                curr_sum = curr_sum + nums[stop - 1]

                if curr_sum > best_sum:

                    best_sum = curr_sum
                    # best_start = start
                    # best_stop = stop

        return best_sum    # (best_sum, best_start, best_stop)

    def maxSubArray__implicit_subarray(self, nums: List[int]) -> int:
        """
        Solution to "maximum subarray sum" that
        - loops through the numbers once
        - builds the subarray sum as it goes
        """

        # Handle empty input `nums`.
        if not nums:
            return self.DEFAULT_SUM

        best_sum = self.WORST_SUM    # -- the sum of the best sub-array
        curr_sum = self.DEFAULT_SUM    # -- the sum of the current sub-array

        # The sub-array is implicit and its information is handled by `curr_sum`.

        for num in nums:
            # Add `num` to `curr_sum` while they're still more than `DEFAULT_SUM`.
            curr_sum = max(self.DEFAULT_SUM, curr_sum + num)
            # Choose the max of the current `best_sum` and `curr_sum`.
            best_sum = max(best_sum, curr_sum)

        return best_sum

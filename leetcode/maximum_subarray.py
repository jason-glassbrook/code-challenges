#!python3

from typing import List

INITIAL__CURR_SUM = 0
INITIAL__BEST_SUM = float("-inf")


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Caller for "maximum subarray sum".
        NOTE: The empty subarray with sum 0 is not an allowed solution.
        """

        return self.maxSubArray__implicit_subarray(nums)

    def maxSubArray__brute_force__v1(self, nums: List[int]) -> int:
        """
        Solution to "maximum subarray sum" that
        - loops through all subarrays
        - calculates the subarray sum by slicing the array
        """

        # Handle empty input `nums`.
        if not nums:
            return INITIAL__CURR_SUM

        n = len(nums)
        best_sum = INITIAL__BEST_SUM
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
            return INITIAL__CURR_SUM

        n = len(nums)
        best_sum = INITIAL__BEST_SUM
        # best_start = None
        # best_stop = None

        for start in range(0, n):

            curr_sum = INITIAL__CURR_SUM

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
            return INITIAL__CURR_SUM

        best_sum = nums[0]
        curr_sum = INITIAL__CURR_SUM

        # The sub-array is implicit and its information is handled by `num` and `curr_sum`.

        for num in nums:
            # Ensure that `curr_sum` is at least `INITIAL__CURR_SUM`.
            if curr_sum < INITIAL__CURR_SUM:
                # When `curr_sum` becomes less than `INITIAL__CURR_SUM`,
                # then it cannot possibly contribute to a maximum sum,
                # so reset it.
                curr_sum = INITIAL__CURR_SUM

            curr_sum += num

            # Choose the maximum of the current `best_sum` and `curr_sum`.
            if curr_sum > best_sum:
                best_sum = curr_sum

        return best_sum

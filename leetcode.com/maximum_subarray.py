#!python3

from typing import List


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        DEFAULT_SUM = 0

        best_sum = DEFAULT_SUM    # -- the sum of the best sub-array
        curr_sum = DEFAULT_SUM    # -- the sum of the current sub-array

        # The sub-array is implicit and its information is handled by `curr_sum`.

        for num in nums:
            # Add `num` to `curr_sum` while they're still more than `DEFAULT_SUM`.
            curr_sum = max(DEFAULT_SUM, curr_sum + num)
            # Choose the max of the current `best_sum` and `curr_sum`.
            best_sum = max(best_sum, curr_sum)

        return best_sum

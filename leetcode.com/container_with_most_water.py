from typing import List


class Solution:

    def maxArea(self, heights: List[int]) -> int:

        return self.maxArea__step_inward(heights)

    def maxArea__step_inward(self, heights: List[int]) -> int:

        max_area = 0
        left = 0
        right = len(heights) - 1

        while (left < right):

            # Calculate trial area.
            trial_height = min(heights[left], heights[right])
            trial_width = right - left
            trial_area = trial_height * trial_width

            # Pick larger of current max area and trial area.
            max_area = max(max_area, trial_area)

            # Keep the larger of the current heights for the next trial.
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

    def maxArea__brute_force(self, heights: List[int]) -> int:

        n = len(heights)
        max_area = 0

        for left in range(0, n):

            for right in range(left + 1, n):

                # Calculate trial area.
                trial_height = min(heights[left], heights[right])
                trial_width = right - left
                trial_area = trial_height * trial_width

                # Pick larger of current max area and trial area.
                max_area = max(max_area, trial_area)

        return max_area

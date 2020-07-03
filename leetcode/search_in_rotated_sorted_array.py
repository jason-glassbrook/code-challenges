#!python3

from typing import List


class Solution:

    SEARCH__NOT_FOUND = -1

    def search__is_sorted(self, part):

        return (part and part[0] <= part[-1])

    def search__is_in_range(self, part, target):

        return (part and part[0] <= target <= part[-1])

    def search__resolve(self, start, part, target):

        result = self.search(part, target)

        if result != self.SEARCH__NOT_FOUND:
            return start + result

        return self.SEARCH__NOT_FOUND

    def search(self, nums: List[int], target: int) -> int:

        count = len(nums)

        if count > 1:

            middle = count // 2

            part_a__start = 0
            part_a__stop = middle
            part_a = nums[part_a__start : part_a__stop]
            part_a__is_sorted = self.search__is_sorted(part_a)
            part_a__is_in_range = self.search__is_in_range(part_a, target)

            if part_a__is_sorted and part_a__is_in_range:

                return self.search__resolve(part_a__start, part_a, target)

            part_b__start = middle
            part_b__stop = None
            part_b = nums[part_b__start : part_b__stop]
            part_b__is_sorted = self.search__is_sorted(part_b)
            part_b__is_in_range = self.search__is_in_range(part_b, target)

            if part_b__is_sorted and part_b__is_in_range:

                return self.search__resolve(part_b__start, part_b, target)

            if not part_a__is_sorted:

                return self.search__resolve(part_a__start, part_a, target)

            if not part_b__is_sorted:

                return self.search__resolve(part_b__start, part_b, target)

        elif count == 1 and nums[0] == target:

            return 0

        return self.SEARCH__NOT_FOUND

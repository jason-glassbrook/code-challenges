#!python3

from typing import List


class Solution:

    def findDuplicate(self, nums: List[int]) -> int:

        nums_set = set()    # which is like a hash

        for num in nums:

            if num in nums_set:

                return num

            else:

                nums_set.add(num)

        # only occurs if the caller violates the constraints of the problem
        return None

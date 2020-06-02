#!python3

from typing import List


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_set = set()    # which is like a hash

        for n in nums:

            if n in nums_set:

                return True

            else:

                nums_set.add(n)

        return False

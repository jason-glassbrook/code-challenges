#!python3

from typing import List
from collections import defaultdict as DefaultDict


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # make dict of nums, with possible repeats
        nums_dict = DefaultDict(list)

        for (i, num) in enumerate(nums):

            nums_dict[num].append(i)

        # search nums_dict for target
        for (i_1, num_1) in enumerate(nums):

            num_2 = target - num_1

            if num_2 in nums_dict:

                i_2s = nums_dict[num_2]
                i_2 = None

                # handle possible repeats
                if i_1 in i_2s:

                    if len(i_2s) > 1:

                        i_2 = tuple(i for i in i_2s if i != i_1)[0]

                else:

                    i_2 = i_2s[0]

                # return if match found
                if i_2 is not None:

                    return [i_1, i_2]

        return []

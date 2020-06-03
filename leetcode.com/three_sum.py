from typing import List
from collections import defaultdict as DefaultDict


class Solution:

    def threeSum(self, num_list: List[int]) -> List[List[int]]:

        return self.threeSum__hash__v2(num_list)

    def threeSum__brute_force__v1(self, num_list: List[int]) -> List[List[int]]:
        """
        Solution to "three sum" that
        - loops through all triplets
        - stores results in a list
        """

        target = 0
        match_list = list()

        # Iterate through every combination...

        n = len(num_list)

        for i1 in range(0, n - 2):
            for i2 in range(i1 + 1, n - 1):
                for i3 in range(i2 + 1, n):

                    num1 = num_list[i1]
                    num2 = num_list[i2]
                    num3 = num_list[i3]

                    trial = tuple(sorted((num1, num2, num3)))

                    if sum(trial) == target and trial not in match_list:

                        match_list.append(trial)

        return match_list

    def threeSum__brute_force__v2(self, num_list: List[int]) -> List[List[int]]:
        """
        Solution to "three sum" that:
        - loops through all triplets
        - stores results in a hash set
        """

        target = 0
        match_hash = DefaultDict(int)

        # Iterate through every combination...

        n = len(num_list)

        for i1 in range(0, n - 2):
            for i2 in range(i1 + 1, n - 1):
                for i3 in range(i2 + 1, n):

                    num1 = num_list[i1]
                    num2 = num_list[i2]
                    num3 = num_list[i3]

                    trial = tuple(sorted((num1, num2, num3)))

                    if sum(trial) == target:

                        match_hash[trial] += 1

        return tuple(match_hash.keys())

    def threeSum__brute_force__v3(self, num_list: List[int]) -> List[List[int]]:
        """
        Solution to "three sum" that
        - loops through all triplets
        - uses hash sets of num1, num2, num3 to avoid duplicates
        - stores results in a hash set
        """

        target = 0
        match_hash = DefaultDict(int)

        # Iterate through every combination...

        n = len(num_list)

        # Track duplicates of num1.
        visited_num1_hash = set()

        for i1 in range(0, n - 2):

            num1 = num_list[i1]

            # Skip duplicate of num1, else record it.
            if num1 in visited_num1_hash:
                continue
            else:
                visited_num1_hash.add(num1)

            # Track duplicates of num2 (reseting for every num1).
            visited_num2_hash = set()

            for i2 in range(i1 + 1, n - 1):

                num2 = num_list[i2]

                # Skip duplicate of num2, else record it.
                if num2 in visited_num2_hash:
                    continue
                else:
                    visited_num2_hash.add(num2)

                # Track duplicates of num3 (reseting for every num2 and num1).
                visited_num3_hash = set()

                for i3 in range(i2 + 1, n):

                    num3 = num_list[i3]

                    # Skip duplicate of num3, else record it.
                    if num3 in visited_num3_hash:
                        continue
                    else:
                        visited_num3_hash.add(num3)

                    trial = tuple(sorted((num1, num2, num3)))

                    if sum(trial) == target:

                        match_hash[trial] += 1

        return tuple(match_hash.keys())

    def threeSum__hash__v1(self, num_list: List[int]) -> List[List[int]]:
        """
        Solution to "three sum" that
        - uses a hash map from numbers to indices
        - stores results in a hash set
        """

        target = 0
        match_hash = DefaultDict(int)

        # Hash num_list to indices...

        num_hash = DefaultDict(set)

        for (i, num) in enumerate(num_list):

            num_hash[num].add(i)

        # Iterate through combinations...

        n = len(num_list)

        for i1 in range(0, n - 2):
            for i2 in range(i1 + 1, n - 1):

                num1 = num_list[i1]
                num2 = num_list[i2]
                num3 = target - num1 - num2

                if num3 in num_hash:

                    # Find whether i3 is available. We cannot duplicate i1 or i2.
                    i3_set = set.difference(num_hash[num3], set((i1, i2)))

                    if i3_set:

                        trial = tuple(sorted((num1, num2, num3)))
                        match_hash[trial] += 1

        return tuple(match_hash.keys())

    def threeSum__hash__v2(self, num_list: List[int]) -> List[List[int]]:
        """
        Solution to "three sum" that
        - uses a hash map from numbers to indices
        - uses hash sets of num1, num2 to avoid duplicates
        - stores results in a hash set
        """

        target = 0
        match_hash = DefaultDict(int)

        # Hash num_list to indices...

        num_hash = DefaultDict(set)

        for (i, num) in enumerate(num_list):

            num_hash[num].add(i)

        # Iterate through combinations...

        n = len(num_list)

        # Track duplicates of num1.
        visited_num1_hash = set()

        for i1 in range(0, n - 2):

            num1 = num_list[i1]

            # Skip duplicate of num1, else record it.
            if num1 in visited_num1_hash:
                continue
            else:
                visited_num1_hash.add(num1)

            # Track duplicates of num2 (reseting for every num1).
            visited_num2_hash = set()

            for i2 in range(i1 + 1, n - 1):

                num2 = num_list[i2]

                # Skip duplicate of num2, else record it.
                if num2 in visited_num2_hash:
                    continue
                else:
                    visited_num2_hash.add(num2)

                num3 = target - num1 - num2

                if num3 in num_hash:

                    # Find whether i3 is available. We cannot duplicate i1 or i2.
                    i3_set = set.difference(num_hash[num3], set((i1, i2)))

                    if i3_set:

                        trial = tuple(sorted((num1, num2, num3)))
                        match_hash[trial] += 1

        return tuple(match_hash.keys())

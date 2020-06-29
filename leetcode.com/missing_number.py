#!python3

from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        return self.missingNumber__hash_set(nums)

    def missingNumber__brute_force(self, nums: List[int]) -> int:

        if not nums:
            return None

        # Sort the list. Now this isn't linear time!
        nums = sorted(nums)

        # Check each number in the list:
        # - Each number should equal its index.
        # - If not, then the expected number (index) is missing.
        for expected in range(0, len(nums)):
            if nums[expected] != expected:
                return expected

        # Maybe nothing was missing?
        return None

    def missingNumber__hash_set(self, nums: List[int]) -> int:

        if not nums:
            return None

        # Create a hash set of `nums`.
        nums_set = set(nums)

        # Check each number in the list:
        for expected in range(0, len(nums)):
            if expected not in nums_set:
                return expected

        # Maybe nothing was missing?
        return None

    def missingNumber__xor(self, nums: List[int]) -> int:
        """
        This method uses XOR to find the missing number.
        I don't fully understand how it works, but it's clever.
        It sort of "bubbles" out the bits for the missing number.
        """

        if not nums:
            return None

        # Construct the missing number:
        missing = len(nums)
        for (i, num) in enumerate(nums):
            missing ^= i ^ num

        # Maybe nothing was missing?
        return (missing if missing != len(nums) else None)

    def missingNumber__sum(self, nums: List[int]) -> int:
        """
        I don't think this method can determine if zero is missing...
        """

        if not nums:
            return None

        # Compute the expected and actual sums.
        expected_sum = len(nums) * (len(nums) + 1) // 2    # <- Gauss formula.
        actual_sum = sum(nums)
        missing = expected_sum - actual_sum

        # Maybe nothing was missing?
        return missing


if __name__ == "__main__":

    tests = [{
        "args": ([3, 0, 1],),
        "answer": 2,
    }, {
        "args": ([9, 6, 4, 2, 3, 5, 7, 0, 1],),
        "answer": 8,
    }]

    solution = Solution()

    for test in tests:

        args = test["args"]
        answer = test["answer"]

        print("\n--- test case ---\n")
        print(args)
        print("expected:", answer)
        print("returned:", solution.missingNumber(*args))

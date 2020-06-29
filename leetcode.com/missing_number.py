#!python3

from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        return self.missingNumber__brute_force(nums)

    def missingNumber__brute_force(self, nums: List[int]) -> int:

        if not nums:
            return None

        return 0

    def missingNumber__hash_set(self, nums: List[int]) -> int:

        if not nums:
            return None

        return 0

    def missingNumber__xor(self, nums: List[int]) -> int:

        if not nums:
            return None

        return 0

    def missingNumber__sum(self, nums: List[int]) -> int:

        if not nums:
            return None

        return 0


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

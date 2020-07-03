#!python3


class Solution:

    def longestPalindrome(self, string: str) -> str:

        result = ""

        for i in range(len(string)):

            # print("center:", i)

            odd_palindrome = self.find_odd_palindrome_from_center(string, i)
            # print("odd palindrome:", odd_palindrome)

            if len(odd_palindrome) > len(result):
                result = odd_palindrome
                # print("new result:", result)

            even_palindrome = self.find_even_palindrome_from_center(string, i)
            # print("even palindrome:", even_palindrome)

            if len(even_palindrome) > len(result):
                result = even_palindrome
                # print("new result:", result)

        return result

    def find_palindrome_from_center(
        self,
        string: str,
        center: int,
        left_offset: int,
        right_offset: int,
    ) -> str:

        left_stop = 0
        right_stop = len(string) - 1

        left = center + left_offset
        right = center + right_offset

        if center < left_stop or center > right_stop:

            raise IndexError("center outside of string's bounds")

        if left >= left_stop and right <= right_stop and string[left] == string[right]:

            while left - 1 >= left_stop and right + 1 <= right_stop:

                if string[left - 1] == string[right + 1]:
                    left -= 1
                    right += 1
                else:
                    break

        else:

            left = right = center

        return string[left : right + 1]
        # Use need `right + 1` because we're slicing.

    def find_odd_palindrome_from_center(self, string: str, center: int) -> str:

        return self.find_palindrome_from_center(string, center, 0, 0)

    def find_even_palindrome_from_center(self, string: str, center: int) -> str:

        return self.find_palindrome_from_center(string, center, 0, 1)

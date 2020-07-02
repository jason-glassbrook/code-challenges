#!python3

############################################################


class Solution:

    def isAnagram(self, s1: str, s2: str) -> bool:

        return self.isAnagram__python_counter__equals_operator(s1, s2)

    def isAnagram__python_counter__equals_operator(self, s1: str, s2: str) -> bool:
        """
        Solves "valid anagram" problem...
        -   using Python's `collections.Counter`
        -   using Python's equals operator `==`

        This is the easiest way to solve this problem that I can think of.
        """

        from collections import Counter

        #---------------------------------------

        # If `s1` and `s2` aren't the same length, then they can't be anagrams.
        if len(s1) != len(s2):
            return False

        # And then it's just...
        return (Counter(s1) == Counter(s2))

    def isAnagram__python_counter__comparing_keys(self, s1: str, s2: str) -> bool:
        """
        Solves "valid anagram" problem...
        -   using Python's `collections.Counter`
        -   by iteratively comparing the counts of keys
        """

        from collections import Counter

        #---------------------------------------

        # If `s1` and `s2` aren't the same length, then they can't be anagrams.
        if len(s1) != len(s2):
            return False

        # Count the characters in `s1` and `s2`.
        c1 = Counter(s1)
        c2 = Counter(s2)

        # If `c1` and `c2` don't have the same number of keys, then `s1` and `s2` can't be anagrams.
        if len(c1) != len(c2):
            return False

        # Compare the counts of keys.
        # -   Because `c1` and `c2` have the same number of keys,
        #     they must share all letters (but not necessarily their counts)
        #     or they have the same number of unique letters (but their letters are different).
        for letter in c1.keys():
            # Does `letter` occur in `s2`?
            if letter in c2.keys():
                # Does `letter` occur in `s1` and `s2` the same number of times?
                if c1[letter] == c2[letter]:
                    # 🥳 Move on to the next letter!
                    continue

            return False

        # If we made it here, then `s1` and `s2` are anagrams!
        return True


############################################################

import unittest    # noqa: E402
import random    # noqa: E402
import string    # noqa: E402


class TestSolution(unittest.TestCase):

    def _random_string(self, length, alphabet=string.printable):
        return "".join(random.choice(alphabet) for i in range(length))

    def _shuffle_string(self, original):
        return "".join(random.sample(original, len(original)))

    def _run_solution(self, args):
        return Solution().isAnagram(*args)

    def test_example_1(self):

        args = ("anagram", "nagaram")
        answer = True

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_example_2(self):

        args = ("rat", "car")
        answer = False

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_empty_strings(self):

        args = ("", "")
        answer = True

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_strings_of_different_lengths(self):

        (n1, n2) = random.sample(range(2, 10), 2)
        s1 = self._random_string(n1)
        s2 = self._random_string(n2)

        args = (s1, s2)
        answer = False

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_random_matching_strings(self):

        n = random.randrange(2, 10)
        s1 = self._random_string(n)
        s2 = self._shuffle_string(s1)

        args = (s1, s2)
        answer = True

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return

    def test_random_nonmatching_strings(self):

        n = random.randrange(2, 10)
        s1 = self._random_string(n, string.ascii_letters)
        s2 = self._random_string(n, string.digits)

        args = (s1, s2)
        answer = False

        result = self._run_solution(args)

        self.assertIs(result, answer)

        return


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

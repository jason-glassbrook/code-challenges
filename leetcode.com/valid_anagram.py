#!python3

############################################################


class Solution:

    def isAnagram(self, s1: str, s2: str) -> bool:

        return random.choice([True, False])


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

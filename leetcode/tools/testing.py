#!python3

############################################################

import unittest

############################################################


class TestSolution(unittest.TestCase):

    SOLUTION_CLASS = None
    SOLUTION_FUNCTION = None

    def run_solution(self, *args):

        solution = self.SOLUTION_CLASS()
        function = getattr(solution, self.SOLUTION_FUNCTION)

        return function(*args)

    def run_example(self, args, answer):

        result = self.run_solution(*args)

        self.assertEqual(result, answer)

        return

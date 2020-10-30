#!python3

############################################################
#   TESTING
#-----------------------------------------------------------
#   A module of tools for testing solutions to code
#   challenges.
############################################################

import unittest

from tools.oak__ing import (
    Any as _Any,
    Union as _Union,
)
from tools.oak__abc import (
    Callable as _Callable,
    Iterable as _Iterable,
)

#-----------------------------------------------------------


def getattr_of_instance(some_class: type, attr_name: str) -> _Any:

    return getattr(some_class(), attr_name)


class TestSolution(unittest.TestCase):

    SOLUTION_CLASS = None
    SOLUTION_FUNCTION = None

    def run_solution(self, *args: _Iterable) -> _Any:

        function = getattr_of_instance(
            self.SOLUTION_CLASS,
            self.SOLUTION_FUNCTION,
        )

        return function(*args)

    def run_test(
        self,
        args: _Iterable,
        answer: _Any,
        assertion: _Union[_Callable, str, None] = None,
        assertion__rest: _Union[_Iterable, None] = None,
        transform_result: _Union[_Callable, None] = None,
        transform_result__rest: _Union[_Iterable, None] = None,
        transform_answer: _Union[_Callable, None] = None,
        transform_answer__rest: _Union[_Iterable, None] = None,
    ) -> _Any:

        #---------------------------------------
        #   Defaults
        #---------------------------------------

        if assertion is None:
            assertion = "assertEqual"

        if isinstance(assertion, str):
            assertion = getattr(self, assertion)

        if assertion__rest is None:
            assertion__rest = tuple()

        if transform_result is None:
            transform_result = lambda *args: args[0]    # noqa: E731

        if transform_result__rest is None:
            transform_result__rest = tuple()

        if transform_answer is None:
            transform_answer = lambda *args: args[0]    # noqa: E731

        if transform_answer__rest is None:
            transform_answer__rest = tuple()

        #---------------------------------------

        result = transform_result(
            self.run_solution(*args),
            *transform_result__rest,
        )

        answer = transform_answer(
            answer,
            *transform_answer__rest,
        )

        return assertion(result, answer, *assertion__rest)

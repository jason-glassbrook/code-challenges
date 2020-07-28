#!python3

############################################################

from typing import (
    Any,
    Type,
    Union,
    Callable,
    Iterable,
)
import unittest

#-----------------------------------------------------------


def getattr_of_instance(some_class: Type, attr_name: str) -> Any:

    return getattr(some_class(), attr_name)


class TestSolution(unittest.TestCase):

    SOLUTION_CLASS = None
    SOLUTION_FUNCTION = None

    def run_solution(self, *args: Iterable) -> Any:

        function = getattr_of_instance(
            self.SOLUTION_CLASS,
            self.SOLUTION_FUNCTION,
        )

        return function(*args)

    def run_test(
        self,
        args: Iterable,
        answer: Any,
        assertion: Union[Callable, str, None] = None,
        assertion__rest: Union[Iterable, None] = None,
        transform_result: Union[Callable, None] = None,
        transform_result__rest: Union[Iterable, None] = None,
        transform_answer: Union[Callable, None] = None,
        transform_answer__rest: Union[Iterable, None] = None,
    ) -> Any:

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

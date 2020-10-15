#!python3

############################################################

from typing import Union

from leetcode.tools.singly_linked_list import ListNode

MaybeListNode = Union[ListNode, None]

#-----------------------------------------------------------


class Solution:

    MAIN = "hasCycle"

    def hasCycle(self, head: ListNode) -> bool:

        pass


############################################################

import unittest    # noqa: E402

from leetcode.tools import testing    # noqa: E402

#-----------------------------------------------------------


class TestSolution(testing.TestSolution):

    SOLUTION_CLASS = Solution
    SOLUTION_FUNCTION = Solution.MAIN


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

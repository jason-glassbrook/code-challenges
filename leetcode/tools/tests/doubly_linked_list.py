#!python3

############################################################

import unittest
import random

from leetcode.tools.doubly_linked_list import (
    ListNode,
    list_from_data,
)

############################################################
#   Tools
############################################################


def _random_val() -> int:

    return random.randrange(0, 100)


def _random_ListNode() -> tuple:

    pass


############################################################
#   Test `ListNode`
############################################################


class TestListNode(unittest.TestCase):

    pass


############################################################
#   Test `list_from_data`
############################################################


class TestListFromData(unittest.TestCase):

    pass


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

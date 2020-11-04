#!python3

############################################################

import unittest
import random

from tools.oak__ing import (
    Any as _Any,
    Union as _Union,
    TypedDict as _TypedDict,
)

from leetcode.tools.singly_linked_list import (
    ListNode,
    node_from_data,
    data_from_node,
    list_from_data,
)

############################################################
#   Tools
############################################################

_MAIN_ATTR = None
_NODE_ATTR_LIST = (_MAIN_ATTR, "next")
_NODE_RANGE = range(len(_NODE_ATTR_LIST))


class _ListNodeDict(_TypedDict):
    attr: _Union[_MAIN_ATTR, str]
    node: ListNode
    node__val: _Any


def _random_val() -> int:

    return random.randrange(0, 100)


def _random_ListNode() -> tuple[_ListNodeDict, ...]:

    # Make random nodes.
    node_dict_tuple = tuple(
        _ListNodeDict(
            attr=attr,
            node=ListNode(val=None),
            node__val=None,
        ) for attr in _NODE_ATTR_LIST
    )

    # Assign attrs.
    main_node = node_dict_tuple[_NODE_ATTR_LIST.index(_MAIN_ATTR)]["node"]
    for node_dict in node_dict_tuple:
        # Prepare items.
        attr = node_dict["attr"]
        node = node_dict["node"]
        node__val = _random_val()
        # Assign `val`.
        node.val = node__val
        node_dict["node__val"] = node__val
        # Link other nodes to main node.
        if attr is not None:
            setattr(main_node, attr, node)

    return node_dict_tuple


############################################################
#   Test `ListNode`
############################################################


class TestListNode(unittest.TestCase):

    def test_node_val_is_correct(self):

        (node_dict, __) = _random_ListNode()

        node = node_dict["node"]
        node__val = node_dict["node__val"]

        self.assertEqual(node.val, node__val)

        return

    def test_next_val_is_correct(self):

        (node_dict, next_dict) = _random_ListNode()

        node = node_dict["node"]
        next__val = next_dict["node__val"]

        self.assertEqual(node.next.val, next__val)

        return

    def test_next_None_works(self):

        (node_dict, __) = _random_ListNode()

        node = node_dict["node"]
        node.next = None

        self.assertIs(node.next, None)

        return


############################################################
#   Test `node_from_data`
############################################################


class TestNodeFromData(unittest.TestCase):

    pass


############################################################
#   Test `data_from_node`
############################################################


class TestDataFromNode(unittest.TestCase):

    pass


############################################################
#   Test `list_from_data`
############################################################


class TestListFromData(unittest.TestCase):

    pass


############################################################

if __name__ == "__main__":
    unittest.main(verbosity=2)

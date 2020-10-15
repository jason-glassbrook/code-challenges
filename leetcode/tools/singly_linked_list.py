#!python3

############################################################

from typing import (
    Any,
    Union,
)

#-----------------------------------------------------------


# Definition for a singly-linked list node.
class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

        return


#-----------------------------------------------------------

MaybeListNode = Union[ListNode, None]


# Deserialize a singly-linked list node.
def node_from_data(data: Any) -> MaybeListNode:
    """
    Deserialize a singly-linked list node from `data`, which should be something or `None`.
    """

    if data is None:
        return None

    return ListNode(val=data)


# Serialize a singly-linked list node.
def data_from_node(node: MaybeListNode) -> Any:
    """
    Serialize data from a singly-linked list `node`, which should be a `ListNode` or `None`.
    """

    if node is None:
        return None

    return node.val

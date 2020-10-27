#!python3

############################################################

from typing import (Any, Union)
from collections.abc import Iterable

from tools import oak as _oak

#-----------------------------------------------------------


# Definition for a singly-linked list node.
class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

        return


#-----------------------------------------------------------

MaybeIterable = Union[Iterable, None]
MaybeListNode = Union[ListNode, None]


# Deserialize a singly-linked list node.
def node_from_data(data: Any, use_dict: bool = True) -> MaybeListNode:
    """
    Deserialize a singly-linked list node from `data`, which must be something or `None`.

    This optionally accepts `use_dict` as an argument.
    -   If `use_dict` is `True` (default), then...
        1.  this attempts to interpret `data` as a `dict` like `{ "val": Any, ... }`
            (ignoring _all_ other fields) and use `data["val"]` as the `val`;
        2.  and if that fails, this will use `data` as the `val`.
    -   If `use_dict` is `False`, then this will simply use `data` as the `val`.

    If `data` is `None`, this will return `None`.
    """

    if data is None:
        return None

    if use_dict and _oak.is_dict(data) and "val" in data:
        return ListNode(val=data["val"])

    return ListNode(val=data)


# Serialize a singly-linked list node.
def data_from_node(node: MaybeListNode, use_dict: bool = True) -> Any:
    """
    Serialize data from a singly-linked list `node`, which must be a `ListNode` or `None`.

    This optionally accepts `use_dict` as an argument.
    -   If `use_dict` is `True` (default), then this will return a `dict` like
        `{ "val": (node.val), "next": bool }`.
        The `"next"` item will only reflect _whether_ `node.next` exists.
    -   If `use_dict` is `False`, then this will return `node.val`.

    If `data` is `None`, this will return `None`.
    """

    if node is None:
        return None

    if not _oak.is_of(node, ListNode):
        raise TypeError("The provided `node` must be a `ListNode` or `None`.")

    if use_dict:
        return {
            "val": node.val,
            "next": node.next is not None,
        }

    return node.val


# Deserialize a singly-linked list.
def list_from_data(data: MaybeIterable) -> MaybeListNode:
    """
    Deserialize a singly-linked list from `data`, which must be a `list` or `None`.
    If `data` is a list, then it must be a list of items, where each item is...
    -   a `dict` like `{ "val": Any, "next_index": int, ... }`,
        where `next_index` is the index the item's `next` `ListNode` in `data`;
    -   a `dict` like `{ "val": Any, ... }`;
    -   or something else.
    """

    if data is None:
        return None

    if not _oak.is_Iterable(data):
        raise TypeError("The provided `data` must be `Iterable` or `None`.")

    n = len(data)
    node_list = [None] * n
    next_list = [None] * n

    # Process `data` list into `node_list` and `next_list`.
    for (i, item) in enumerate(data):

        if _oak.is_dict(item):
            # If `item` is like `{ "val": Any, ... }`...
            if "val" in item:
                node_list[i] = ListNode(val=item["val"])

                # If `item` is like `{ "val": Any, "next_index": int, ... }`...
                if "next_index" in item:
                    next_list[i] = item["next_index"]

        else:
            node_list[i] = ListNode(val=item)

    # Link up nodes based on `next_list`.
    for (i, next_index) in enumerate(next_list):
        if next_index:
            node_list[i].next = node_list[next_index]
        elif i < (n - 1):
            node_list[i].next = node_list[i + 1]

    return node_list[0]

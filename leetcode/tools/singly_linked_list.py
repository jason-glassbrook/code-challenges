#!python3

############################################################

from tools import oak as _oak
from tools.oak__ing import (
    Any as _Any,
    Union as _Union,
)
from tools.oak__abc import (
    Iterable as _Iterable,
)

_MaybeIterable = _Union[_Iterable, None]

#-----------------------------------------------------------


# Definition for a singly-linked list node.
class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next

        return


MaybeListNode = _Union[ListNode, None]

#-----------------------------------------------------------


# Deserialize a singly-linked list node.
def node_from_data(data: _Any, use_dict: bool = True) -> MaybeListNode:
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
def data_from_node(node: MaybeListNode, use_dict: bool = True) -> _Any:
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
def list_from_data(data: _MaybeIterable) -> MaybeListNode:
    """
    Deserialize a singly-linked list from `data`, which must be a `list` or `None`.
    If `data` is a list, then it must be a list of items, where each item is...
    -   a `dict` like `{ "val": _Any, "next": _Union[int, bool, None], ... }`, where if `data[i]["next"]`...
        -   is an `int`, then `node[i].next` will link to the node specified by `data[data[i]["next"]]`;
        -   is a `bool` or `None`, then it indicates _whether_ the `node[i].next` exists, where...
            -   if `True`, then `node[i].next` will link to the node specified by `data[i+1]`;
            -   if `False` or `None`, then `node[i].next` will be `None`;
        -   otherwise, this raises a `TypeError`;
    -   a `dict` like `{ "val": _Any, ... }`, where `node[i].next` links to `node[i+1]` if available;
    -   or something else, where `node[i].next` links to `node[i+1]` if available.
    """

    if data is None:
        return None

    if not _oak.is_Iterable(data):
        raise TypeError("The provided `data` must be `_Iterable` or `None`.")

    n = len(data)
    node_list = [None] * n
    next_dict = {}    # ⬅ Only store irregular links.

    # Process `data` list into `node_list` and `next_dict`.
    for (i, item) in enumerate(data):

        # If `item` is like `_Any` or `{ "val": _Any, ... }`...
        node_list[i] = node_from_data(item, use_dict=True)

        # If `item` is like `{ "val": _Any, "next": int, ... }`...
        if _oak.is_dict(item) and "next" in item:
            item__next = item["next"]
            if (_oak.is_bool(item__next) or item__next is None) and not item__next:
                next_dict[i] = None
            elif _oak.is_int(item__next):
                next_dict[i] = item__next
            else:
                raise TypeError(f"`data[{i}][\"next\"]` must be a `bool` or `int`.")

    # Link up nodes based on `next_dict`.
    for (i, node) in enumerate(node_list):
        if i in next_dict:
            if next_dict[i] is not None:
                node_list[i].next = node_list[next_dict[i]]
        elif i < (n - 1):
            node_list[i].next = node_list[i + 1]

    return node_list[0]

#!python3

############################################################

from typing import (
    Optional,
    Iterable,
)

############################################################


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

        return


# Deserialize a binary tree.
def tree_from_data(data: Optional[Iterable]):
    """
    Deserialize a binary tree from `data`, which should be of the form `[n, l, r]` or `None`,
    -   where `n` is a scalar value,
    -   where `l` and `r` may be `[n, l, r]`, scalar, or `None`.
    """

    def convert_data_to_tree(val, left, right):

        return TreeNode(
            val,
            convert_data_to_tree(*left) if isinstance(left, Iterable) else left,
            convert_data_to_tree(*right) if isinstance(right, Iterable) else right,
        )

    return convert_data_to_tree(*data) if isinstance(data, Iterable) else None

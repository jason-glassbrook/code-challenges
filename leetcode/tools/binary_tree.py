#!python3

############################################################

from typing import (
    Union,
    Iterable,
)

#-----------------------------------------------------------


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

        return


# Deserialize a binary tree.
def tree_from_data(data: Union[Iterable, None]) -> Union[TreeNode, None]:
    """
    Deserialize a binary tree from `data`, which should be of the form `[n, l, r]` or `None`,
    -   where `n` is a scalar value,
    -   where `l` and `r` may be `[n, l, r]`, scalar, or `None`.
    """

    def convert_scalar_data(scalar_data) -> Union[TreeNode, None]:

        if scalar_data is None:
            return None

        return TreeNode(val=scalar_data)

    def convert_list_data(list_data: Iterable) -> Union[TreeNode, None]:

        n = len(list_data)
        node = None

        if n == 0:
            return node

        if n >= 1:
            node = convert_scalar_data(list_data[0])

        if node is None:
            return node

        if n >= 2:
            node.left = convert_data(list_data[1])

        if n >= 3:
            node.right = convert_data(list_data[2])

        if n > 3:
            print("[binary_tree.tree_from_data] Warning: Ignoring extra child nodes.")

        return node

    def convert_data(data) -> Union[TreeNode, None]:

        if isinstance(data, Iterable):
            return convert_list_data(data)

        else:
            return convert_scalar_data(data)

    return convert_data(data)

#!python3

############################################################

from leetcode.tools.singly_linked_list import ListNode


class Solution:

    def addTwoNumbers(self, l_1: ListNode, l_2: ListNode) -> ListNode:

        BASE = 10

        def has_val(node):
            return (node is not None)

        def has_next(node):
            return (node is not None and node.next is not None)

        #-----------------------------------------------------------

        l_result = ListNode(None)
        l_result_tail = l_result

        d_carry = 0

        while l_1 or l_2 or d_carry:

            # digits

            d_1 = l_1.val if l_1 else 0
            d_2 = l_2.val if l_2 else 0
            d_x = d_1 + d_2 + d_carry

            if d_x >= BASE:
                d_carry = d_x // BASE
                d_x -= d_carry * BASE
            else:
                d_carry = 0

            # next digit node

            l_result_tail.next = ListNode(d_x)
            l_result_tail = l_result_tail.next

            # advance other lists

            l_1 = l_1.next if l_1 else None
            l_2 = l_2.next if l_2 else None

        return l_result.next

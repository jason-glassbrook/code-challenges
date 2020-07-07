#!python3

############################################################

from leetcode.tools.singly_linked_list import ListNode


class Solution:

    def mergeTwoLists(self, list_1: ListNode, list_2: ListNode) -> ListNode:

        result_head = ListNode(None)
        result_tail = result_head

        while list_1 or list_2:

            val_1 = list_1.val if list_1 else None
            val_2 = list_2.val if list_2 else None

            if val_1 is None and val_2 is None:

                break

            elif val_1 is not None and val_2 is None:

                result_tail.next = ListNode(val_1)
                list_1 = list_1.next

            elif val_1 is None and val_2 is not None:

                result_tail.next = ListNode(val_2)
                list_2 = list_2.next

            else:

                if val_1 < val_2:

                    result_tail.next = ListNode(val_1)
                    list_1 = list_1.next

                else:

                    result_tail.next = ListNode(val_2)
                    list_2 = list_2.next

            result_tail = result_tail.next

        return result_head.next

#!python3

############################################################

from leetcode.tools.singly_linked_list import ListNode


class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        return self.removeNthFromEnd__one_pass__v2(head, n)

    def removeNthFromEnd__two_pass(self, head: ListNode, n: int) -> ListNode:

        if n < 1 or head is None:

            return head

        # Create a "dummy" head for the list.
        # This simplifies the case when the nth node from the end is the head.
        dummy = ListNode(
            val=None,
            next=head,
        )

        # Find the length of the list:

        list__length = 0
        runner = dummy.next    # ... starting from `dummy.next == head`

        while runner is not None:

            list__length += 1
            runner = runner.next

        # Remove the nth node from the end of the list:

        ith_from_removal = list__length - n
        runner = dummy    # ... starting from `dummy`

        while ith_from_removal > 0:

            ith_from_removal -= 1
            runner = runner.next

        # `runner.next` is the `n`th from the end.
        runner.next = runner.next.next

        return dummy.next

    def removeNthFromEnd__one_pass__v1(self, head: ListNode, n: int) -> ListNode:

        if n < 1 or head is None:

            return head

        # Create a "dummy" head for the list.
        # This simplifies the case when the nth node from the end is the head.
        dummy = ListNode(
            val=None,
            next=head,
        )

        # Create fast and slow "runner" pointers to move through the list.
        faster = dummy
        slower = dummy

        # Move runners through the list:

        slow_countdown = n

        while faster.next is not None:

            if slow_countdown > 0:

                slow_countdown -= 1

            else:

                slower = slower.next

            faster = faster.next

        # `slower.next` is the `n`th from the end.
        slower.next = slower.next.next

        return dummy.next

    def removeNthFromEnd__one_pass__v2(self, head: ListNode, n: int) -> ListNode:

        if n < 1 or head is None:

            return head

        # Move a fast "runner" through `n` nodes:

        faster = head
        i = 0

        while i < n and faster is not None:

            faster = faster.next
            i += 1

        # Are there more nodes in the list?
        # print(i, ":", faster)

        if faster is None:

            if i == n:
                # There are `n` nodes, so `head` is the `n`th from the end.
                return head.next

            else:
                # There are less than `n` nodes, so there's nothing to remove.
                return head

        # Move the fast and a new slow "runner" while more nodes remain:

        slower = head

        while faster.next is not None:

            faster = faster.next
            # print("faster", ":", faster)
            slower = slower.next
            # print("slower", ":", slower)

        # `slower.next` is the `n`th from the end.
        slower.next = slower.next.next

        return head

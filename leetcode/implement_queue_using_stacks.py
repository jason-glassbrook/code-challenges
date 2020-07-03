#!python3

from collections import deque as Deck


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.__stack_a = Deck()
        self.__stack_b = Deck()

        return

    def __flip(self) -> None:
        """
        Flip items from stack_a into stack_b.
        """

        # if stack_b is empty
        if not self.__stack_b:

            # while there are items in stack_a
            while self.__stack_a:

                # flip items from stack_a into stack_b
                self.__stack_b.append(self.__stack_a.pop())

        return

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """

        self.__stack_a.append(x)

        return

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        # flip stack_a into stack_b
        self.__flip()

        return self.__stack_b.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """

        # flip stack_a into stack_b
        self.__flip()

        # return the top item in stack_b
        return self.__stack_b[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """

        return (not self.__stack_a and not self.__stack_b)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

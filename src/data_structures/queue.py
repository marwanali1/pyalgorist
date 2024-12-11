# pylint: disable=R0801

from typing import TypeVar

T = TypeVar("T")


class QueueNode:
    def __init__(self, data: T) -> None:
        self._data = data
        self._next_node = None

    @property
    def data(self) -> T:
        return self._data

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        self._next_node = node


class Queue:
    """
    The Queue class represents a first-in-first-out (FIFO) queue of objects.
    """

    def __init__(self) -> None:
        self._first = None
        self._last = None

    def __contains__(self, elem: T) -> bool:
        """
        Returns true if this queue contains the specified element.
        Time Complexity: O(n)
        """
        curr = self._first
        while curr:
            if curr.data == elem:
                return True
            curr = curr.next_node

        return False

    def __str__(self) -> str:
        """
        Returns a string representation of this Queue, containing the String representation of each
        element.
        """
        if not self._first:
            return "[]"

        elems = []
        curr = self._first
        while curr:
            elems.append(curr.data)
            curr = curr.next_node

        return str(elems)

    def enqueue(self, elem: T) -> None:
        """
        Inserts the specified element to the end this queue.
        Time Complexity: O(1)
        """
        new_elem = QueueNode(elem)
        if self._last:
            self._last.next_node = new_elem
        self._last = new_elem

        if self.empty():
            self._first = self._last

    def dequeue(self) -> T:
        """
        Retrieves and removes the head of this queue.
        Time Complexity: O(1)
        """
        if self.empty():
            raise IndexError("Queue is empty")

        elem = self._first.data
        self._first = self._first.next_node
        if not self._first:
            self._last = None

        return elem

    def peek(self) -> T:
        """
        Retrieves, but does not remove, the head of this queue, or returns null if this queue is
        empty.
        Time Complexity: O(1)
        """
        if self.empty():
            return None

        return self._first.data

    def empty(self) -> bool:
        """
        Tests if this queue is empty.
        Time Complexity: O(1)
        """
        return not self._first

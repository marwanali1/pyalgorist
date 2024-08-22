from typing import TypeVar, Generic

T = TypeVar("T")


class QueueNode:
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None


class Queue:
    """
    The Queue class represents a first-in-first-out (FIFO) queue of objects.
    """

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def __str__(self) -> str:
        """
        Returns a string representation of this Queue, containing the String representation of each element.
        """
        if not self.first:
            return "[]"

        elems = []
        curr = self.first
        while curr:
            elems.append(curr.data)
            curr = curr.next

        return str(elems)

    def contains(self, elem: T) -> bool:
        """
        Returns true if this queue contains the specified element.
        Time Complexity: O(n)
        """
        curr = self.first
        while curr:
            if curr.data == elem:
                return True
            curr = curr.next

        return False

    def enqueue(self, elem: T) -> None:
        """
        Inserts the specified element to the end this queue.
        Time Complexity: O(1)
        """
        new_elem = QueueNode(elem)
        if self.last:
            self.last.next = new_elem
        self.last = new_elem

        if self.empty():
            self.first = self.last

    def dequeue(self) -> T:
        """
        Retrieves and removes the head of this queue.
        Time Complexity: O(1)
        """
        if self.empty():
            raise IndexError("Queue is empty")

        elem = self.first.data
        self.first = self.first.next
        if not self.first:
            self.last = None
        
        return elem

    def peek(self) -> T:
        """
        Retrieves, but does not remove, the head of this queue, or returns null if this queue is empty.
        Time Complexity: O(1)
        """
        if self.empty():
            return None

        return self.first.data

    def empty(self) -> bool:
        """
        Tests if this queue is empty.
        Time Complexity: O(1)
        """
        return not self.first

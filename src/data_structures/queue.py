from typing import TypeVar, Generic

T = TypeVar("T")


class QueueNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None


class Queue(Generic[T]):
    """
    The Queue class represents a first-in-first-out (FIFO) queue of objects.
    """

    def __init__(self) -> None:
        self.first = None
        self.last = None

    def enqueue(self, item: T) -> None:
        """
        Adds an item to the end of the queue.
        Time Complexity: O(1)
        """
        new_item = QueueNode(item)
        if self.last != None:
            self.last.next = new_item

        self.last = new_item
        if self.first == None:
            self.first = self.last

    def dequeue(self) -> T:
        """
        Removes the first item in the queue.
        Time Complexity: O(1)
        """
        if self.first == None:
            raise Exception("Empty queue")

        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None

        return data

    def peek(self) -> T:
        """
        Returns the first item in the queue.
        Time Complexity: O(1)
        """
        if self.first == None:
            raise Exception("Empty queue")

        return self.first.data

    def isEmpty(self) -> bool:
        """
        Tests if this queue is empty.
        Time Complexity: O(1)
        """
        return self.first == None

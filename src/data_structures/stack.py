from typing import TypeVar, Generic

T = TypeVar("T")


class StackNode(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None


class Stack(Generic[T]):
    """
    The Stack class represents a last-in-first-out (LIFO) stack of objects.
    """

    def __init__(self) -> None:
        self.top = None

    def push(self, item: T) -> None:
        """
        Pushes an item onto the top of this stack.
        Time Complexity: O(1)
        """
        new_item = StackNode(item)
        new_item.next = self.top
        self.top = new_item

    def pop(self) -> T:
        """
        Removes the object at the top of this stack and returns that object as the value of this function.
        Time Complexity: O(1)
        """
        if self.top == None:
            raise Exception("Empty stack")

        top_item = self.top.data
        self.top = self.top.next
        return top_item

    def peek(self) -> T:
        """
        Looks at the object at the top of this stack without removing it from the stack.
        Time Complexity: O(1)
        """
        if self.top == None:
            raise Exception("Empty stack")

        return self.top.data

    def isEmpty(self) -> bool:
        """
        Tests if this stack is empty.
        Time Complexity: O(1)
        """
        return self.top == None

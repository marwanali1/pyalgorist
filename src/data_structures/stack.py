from typing import TypeVar

T = TypeVar("T")


class StackNode:
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None


class Stack:
    """
    The Stack class represents a last-in-first-out (LIFO) stack of objects.
    """

    def __init__(self) -> None:
        self.top = None

    def __str__(self) -> str:
        """
        Returns a string representation of this Stack, containing the String representation of each element.
        """
        if not self.top:
            return "[]"

        elems = []
        curr = self.top
        while curr:
            elems.append(curr.data)
            curr = curr.next

        return str(elems)

    def contains(self, elem: T) -> bool:
        """
        Returns true if this stack contains the specified element.
        Time Complexity: O(n)
        """
        curr = self.top
        while curr:
            if curr.data == elem:
                return True
            curr = curr.next
        
        return False

    def empty(self) -> bool:
        """
        Tests if this stack is empty.
        Time Complexity: O(1)
        """
        return not self.top

    def peek(self) -> T:
        """
        Looks at the object at the top of this stack without removing it from the stack.
        Time Complexity: O(1)
        """
        if self.empty():
            raise IndexError("Stack is empty")
        
        return self.top.data

    def pop(self) -> T:
        """
        Removes the object at the top of this stack and returns that object as the value of this function.
        Time Complexity: O(1)
        """
        if self.empty():
            raise IndexError("Stack is empty")

        elem = self.top.data
        self.top = self.top.next
        return elem

    def push(self, elem: T) -> None:
        """
        Pushes an element onto the top of this stack.
        Time Complexity: O(1)
        """
        new_top = StackNode(elem)
        new_top.next = self.top
        self.top = new_top

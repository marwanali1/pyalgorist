from typing import TypeVar

T = TypeVar("T")


class ListNode:
    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class LinkedList:
    """
    Linked list implementation of the List abstract data type.
    """

    def __init__(self) -> None:
        self.head = None
        self._size = 0

    def __str__(self) -> str:
        """
        Returns a string representation of this LinkedList, containing the String representation of each element.
        """
        if not self.head:
            return "[]"

        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next

        return str(elems)

    @property
    def size(self) -> int:
        """
        Returns the number of elements in this list.
        Time Complexity: O(1)
        """
        return self._size

    def contains(self, elem: T) -> bool:
        """
        Returns true if this list contains the specified element.
        Time Complexity: O(n)
        """
        curr = self.head
        while curr:
            if curr.data == elem:
                return True
            curr = curr.next

        return False

    def get(self, index: int) -> T:
        """
        Returns the element at the specified position in this list.
        Time Complexity: O(n)
        """
        if index < 0 or index >= self._size:
            raise IndexError("List index is out of range")

        curr_index = 0
        curr = self.head
        while curr and curr_index < index:
            curr = curr.next
            curr_index += 1

        return curr.data

    def add(self, index, elem: T) -> None:
        """
        Inserts the specified element at the specified position in this list.
        Time Complexity: O(n)
        """
        if index < 0 or index > self._size:
            raise IndexError("List index is out of range")

        if index == 0:
            self.add_first(elem)
            return

        curr, curr_index = ListNode(), 0
        curr.next = self.head
        while curr.next and curr_index < index:
            curr = curr.next
            curr_index += 1

        new_node = ListNode(elem)
        new_node.next = curr.next
        curr.next = new_node
        self._size += 1

    def add_first(self, elem: T) -> None:
        """
        Inserts the specified element at the beginning of this list.
        Time Complexity: O(1)
        """
        new_node = ListNode(elem)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def add_last(self, elem: T) -> None:
        """
        Appends the specified element to the end of this list.
        Time Complexity: O(n)
        """
        if not self.head:
            self.head = ListNode(elem)
            self._size += 1
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = ListNode(elem)
        self._size += 1

    def remove(self, index: int) -> T:
        """
        Removes and returns the element at the specified position in this list.
        Time Complexity: O(n)
        """
        if index < 0 or index >= self._size:
            raise IndexError("List index is out of range")

        if index == 0:
            return self.remove_first()

        curr, curr_index = ListNode(), 0
        curr.next = self.head
        while curr.next and curr_index < index:
            curr = curr.next
            curr_index += 1

        data = curr.next.data
        curr.next = curr.next.next
        self._size -= 1

        return data

    def remove_first(self) -> T:
        """
        Removes and returns the first element from this list.
        Time Complexity: O(1)
        """
        if not self.head:
            raise IndexError("List is empty")

        data = self.head.data
        self.head = self.head.next
        self._size -= 1

        return data

    def remove_last(self) -> T:
        """
        Removes and returns the last element from this list.
        Time Complexity: O(n)
        """
        if not self.head:
            raise IndexError("List is empty")

        curr = self.head
        while curr.next.next:
            curr = curr.next

        data = curr.next.data
        curr.next = None
        self._size -= 1

        return data

    def reverse(self) -> None:
        """
        Reverses the order of elements in this list.
        Time Complexity: O(n)
        """
        prev_node = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node

        self.head = prev_node

from typing import Any, Iterable, TypeVar

T = TypeVar("T")


class DynamicArray:
    """
    Resizable-array implementation of the List abstract data type.
    """

    def __init__(self, capacity: int = 10) -> None:
        self._capacity = capacity
        self._size = 0
        self.array = [None] * capacity

    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __str__(self) -> str:
        """
        Returns a string representation of this DynamicArray, containing the String representation of each element.
        """
        if self._size == 0:
            return "[]"

        return str(self.array[: self._size])

    def __repr__(self) -> str:
        pass

    def __eq__(self, other: Any) -> bool:
        pass

    @property
    def capacity(self) -> int:
        """
        Returns the capacity of this array
        Time Complexity: O(1)
        """
        return self._capacity

    @property
    def size(self) -> int:
        """
        Returns the number of elements in this array.
        Time Complexity: O(1)
        """
        return self._size

    def contains(self, item: T) -> bool:
        """
        Returns true if this list contains the specified element.
        Time Complexity: O(n)
        """
        return item in self.array

    def get(self, index: int) -> T:
        """
        Returns the element at the specified position in this array.
        Time Complexity: O(1)
        """
        if index < 0 or index >= self._size:
            raise IndexError("Array index is out of range")

        return self.array[index]

    def add(self, index: int, item: T) -> None:
        """
        Inserts the specified element at the specified position in this array.
        Time Complexity: O(n)
        """
        if index < 0 or index >= self._size:
            raise IndexError("Array index is out of range")

        if self._size + 1 > self._capacity:
            self._resize()

        if not self.array[index]:
            self.array[index] = item
            self._size += 1
            return

        new_array = self.array[:index]
        new_array.append(item)
        new_array += self.array[index:]
        self.array = new_array
        self._size += 1

    def add_last(self, item: T) -> None:
        """
        Appends the specified element to the end of this array.
        Time Complexity: O(n)
        """
        if self._size == self._capacity:
            self._resize()

        self.array[self._size] = item
        self._size += 1

    def remove(self, index: int) -> T:
        """
        Removes the element at the specified position in this array.
        Time Complexity: O(n)
        """
        if index < 0 or index >= self._size:
            raise IndexError("Array index is out of range")

        removed_elem = self.array[index]
        new_array = self.array[:index]
        new_array += self.array[index + 1 :]
        self.array = new_array
        self._size -= 1
        return removed_elem

    def remove_last(self) -> T:
        """
        Removes and returns the last element in this array.
        Time Complexity: O(1)
        """
        if not self._size:
            raise IndexError("Array is empty")

        removed_elem = self.array[self._size - 1]
        self.array[self._size - 1] = None
        self._size -= 1
        return removed_elem

    def _resize(self) -> None:
        """
        Doubles the capacity of the array.
        Time Complexity: O(n)
        """
        self._capacity *= 2
        new_array = [None] * self._capacity
        for i, elem in enumerate(self.array):
            new_array[i] = elem
        self.array = new_array

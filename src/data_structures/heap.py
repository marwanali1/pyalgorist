from typing import TypeVar

T = TypeVar("T")


class Heap:
    """
    Array based heap implementation.
    """

    def __init__(self) -> None:
        self._data: list[T] = []

    def __len__(self) -> int:
        return len(self._data)

    def __str__(self) -> str:
        """
        Returns a string representation of this Heap, containing the String representation of each
        element.
        """
        return str(self._data)

    @property
    def root_node(self) -> T:
        return self._data[0]

    @property
    def last_node(self) -> T:
        return self._data[-1]

    def _get_left_child_index(self, index: int) -> int:
        return (index * 2) + 1

    def _get_right_child_index(self, index: int) -> int:
        return (index * 2) + 2

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _get_larger_child_index(self, index: int) -> int:
        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)

        if right_child_index >= len(self):
            return left_child_index

        return (
            left_child_index
            if self._data[left_child_index] > self._data[right_child_index]
            else right_child_index
        )

    def _has_larger_child(self, index: int) -> bool:
        left_child_index = self._get_left_child_index(index)
        right_child_index = self._get_right_child_index(index)

        has_larger_left_child = (left_child_index < len(self)) and (
            self._data[left_child_index] > self._data[index]
        )

        has_larger_right_child = (right_child_index < len(self)) and (
            self._data[right_child_index] > self._data[index]
        )

        return has_larger_left_child or has_larger_right_child

    def is_empty(self) -> bool:
        return len(self) == 0

    def peek(self) -> T:
        if self.is_empty():
            return None

        return self.root_node

    def push(self, elem: T) -> None:
        """
        Inserts the specified element into this heap
        Time Complexity: O(log n)
        """
        self._data.append(elem)
        new_node_index = len(self) - 1

        parent_index = self._get_parent_index(new_node_index)
        while (new_node_index > 0) and (
            self._data[new_node_index] > self._data[parent_index]
        ):
            self._data[new_node_index], self._data[parent_index] = (
                self._data[parent_index],
                self._data[new_node_index],
            )
            new_node_index = parent_index
            parent_index = self._get_parent_index(new_node_index)

    def pop(self) -> T:
        """
        Retrieves and removes the top element of this heap.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Heap is empty")

        popped_elem = self.root_node
        if len(self) == 1:
            self._data.pop()
            return popped_elem

        self._data[0] = self._data.pop()
        trickle_node_index = 0
        while self._has_larger_child(trickle_node_index):
            larger_child_index = self._get_larger_child_index(trickle_node_index)
            self._data[trickle_node_index], self._data[larger_child_index] = (
                self._data[larger_child_index],
                self._data[trickle_node_index],
            )
            trickle_node_index = larger_child_index

        return popped_elem

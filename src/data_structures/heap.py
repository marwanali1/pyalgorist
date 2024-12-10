from typing import TypeVar

T = TypeVar("T")


class Heap:
    """
    Array based heap implementation.
    """

    def __init__(self) -> None:
        self.__data: list[T] = []

    def __len__(self) -> int:
        return len(self.__data)

    def __str__(self) -> str:
        """
        Returns a string representation of this Heap, containing the String representation of each element.
        """
        return str(self.__data)

    @property
    def root_node(self) -> T:
        return self.__data[0]

    @property
    def last_node(self) -> T:
        return self.__data[-1]

    def __get_left_child_index(self, index: int) -> int:
        return (index * 2) + 1

    def __get_right_child_index(self, index: int) -> int:
        return (index * 2) + 2

    def __get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def __get_larger_child_index(self, index: int) -> int:
        left_child_index = self.__get_left_child_index(index)
        right_child_index = self.__get_right_child_index(index)

        if right_child_index >= len(self):
            return left_child_index

        return (
            left_child_index
            if self.__data[left_child_index] > self.__data[right_child_index]
            else right_child_index
        )

    def __has_larger_child(self, index: int) -> bool:
        left_child_index = self.__get_left_child_index(index)
        right_child_index = self.__get_right_child_index(index)

        has_larger_left_child = (left_child_index < len(self)) and (
            self.__data[left_child_index] > self.__data[index]
        )

        has_larger_right_child = (right_child_index < len(self)) and (
            self.__data[right_child_index] > self.__data[index]
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
        self.__data.append(elem)
        new_node_index = len(self) - 1

        parent_index = self.__get_parent_index(new_node_index)
        while (new_node_index > 0) and (
            self.__data[new_node_index] > self.__data[parent_index]
        ):
            self.__data[new_node_index], self.__data[parent_index] = (
                self.__data[parent_index],
                self.__data[new_node_index],
            )
            new_node_index = parent_index
            parent_index = self.__get_parent_index(new_node_index)

    def pop(self) -> T:
        """
        Retrieves and removes the top element of this heap.
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Heap is empty")

        popped_elem = self.root_node
        if len(self) == 1:
            self.__data.pop()
            return popped_elem

        self.__data[0] = self.__data.pop()
        trickle_node_index = 0
        while self.__has_larger_child(trickle_node_index):
            larger_child_index = self.__get_larger_child_index(trickle_node_index)
            self.__data[trickle_node_index], self.__data[larger_child_index] = (
                self.__data[larger_child_index],
                self.__data[trickle_node_index],
            )
            trickle_node_index = larger_child_index

        return popped_elem

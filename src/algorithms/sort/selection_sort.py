from typing import TypeVar

T = TypeVar("T")


def selection_sort(arr: list[T]) -> list[T]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(arr) - 1):
        lowest_num_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowest_num_index]:
                lowest_num_index = j

        if lowest_num_index != i:
            arr[i], arr[lowest_num_index] = arr[lowest_num_index], arr[i]

    return arr

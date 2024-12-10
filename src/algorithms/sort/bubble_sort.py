from typing import TypeVar

T = TypeVar("T")


def bubble_sort(arr: list[T]) -> list[T]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    unsorted_until_index = len(arr) - 1
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_until_index):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
        unsorted_until_index -= 1

    return arr

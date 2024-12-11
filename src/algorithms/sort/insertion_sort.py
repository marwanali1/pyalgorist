from typing import TypeVar

T = TypeVar("T")


def insertion_sort(arr: list[T]) -> list[T]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        temp_value = arr[i]
        position = i - 1

        while position >= 0:
            if arr[position] > temp_value:
                arr[position + 1] = arr[position]
                position = position - 1
            else:
                break

        arr[position + 1] = temp_value

    return arr


# def insertion_sort(arr: list) -> list:
#     """
#     Time Complexity: O(n^2)
#     Space Complexity: O(1)
#     """
#     for i in range(len(arr)):
#         j = i
#         while (j > 0) and (arr[j] < arr[j-1]):
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#             j -= 1

#     return arr

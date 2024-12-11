from typing import TypeVar

T = TypeVar("T")


def binary_search(arr: list[T], target: T) -> int:
    """
    Iterative approach
    Time Complexity: O(logn)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        mid_value = arr[mid]
        if target == mid_value:
            return mid

        if target < mid_value:
            right = mid - 1
        else:
            left = mid + 1

    return -1


# def binary_search(arr: list[int], target: int) -> int:
#     """
#     Recursive approach
#     Time Complexity: O(log n)
#     Space Complexity: O(log n)
#     """
#     def search(left, right):
#         if left > right:
#             return -1

#         mid = left + ((right - left) // 2)
#         if arr[mid] == target:
#             return mid

#         if (arr[mid] < target):
#             return search(mid + 1, right)
#         else:
#             return search(left, mid - 1)

#     left, right = 0, len(arr) - 1
#     return search(left, right)

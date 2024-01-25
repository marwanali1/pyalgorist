def binary_search(nums: list[int], target: int) -> int:
    """
    Iterative approach
    Time Complexity: O(logn)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + ((right - left) // 2)
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid

    return -1


# def binary_search(nums: list[int], target: int) -> int:
#     """
#     Recursive approach
#     Time Complexity: O(log n)
#     Space Complexity: O(log n)
#     """
#     def search(left, right):
#         if left > right:
#             return -1
        
#         mid = left + ((right - left) // 2)
#         if nums[mid] == target:
#             return mid
        
#         if (nums[mid] < target):
#             return search(mid + 1, right)
#         else:
#             return search(left, mid - 1)
    
#     left, right = 0, len(nums) - 1
#     return search(left, right)
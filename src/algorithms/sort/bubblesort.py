
def bubble_sort(nums: list[int]) -> list[int]:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

    return nums

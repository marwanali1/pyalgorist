def insertion_sort(arr: list) -> list:
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    for i in range(len(arr)):
        j = i
        while (j > 0) and (arr[j] < arr[j-1]):
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1

    return arr

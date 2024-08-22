from typing import TypeVar

T = TypeVar("T")


class QuicksortArray:

    def __init__(self, array: list[T] = []) -> None:
        self.array = array

    def __len__(self) -> int:
        return len(self.array)
    
    def __repr__(self) -> str:
        return f"QuicksortArray({self.array})"

    def __str__(self) -> str:
        return str(self.array)


    def partition(self, left: int, right: int) -> int:
        # Set pivot to the right most value in the array
        pivot_index = right
        pivot = self.array[right]

        # Move right pointer to value directly before the pivot
        right -= 1

        while True:
            
            # Shift left point until it reaches a value greater than or equal to the pivot
            while self.array[left] < pivot:
                left += 1
            
            # Shift right pointer until it reaches a value less than of equalt to the pivot
            while self.array[right] > pivot:
                right -= 1
            
            # If left and right pointers meet or pass each other break out of the loop
            if left >= right:
                break
            
            # Swap the values of left and right when both pointers have stopped
            self.array[left], self.array[right] = self.array[right], self.array[left]
            left += 1
        
        # If the pivot is less than the left value, swap the pivot and the left value
        if pivot < self.array[left]:
            self.array[left], self.array[pivot_index], = self.array[pivot_index], self.array[left]
        
        return left


    def quicksort(self, left: int, right: int) -> None:
        """
        Time Complexity: O(nlogn)
        """
        if right - left <= 0:
            return
        
        pivot_index = self.partition(left, right)
        self.quicksort(left, pivot_index - 1)
        self.quicksort(pivot_index + 1, right)
    

    def quickselect(self, kth_value: int, left: int, right: int) -> int:
        """
        Time Complexity: O(n)
        """
        if right - left <= 0:
            return self.array[left]
        
        pivot_index = self.partition(left, right)
        
        if kth_value < pivot_index:
            return self.quickselect(kth_value, left, pivot_index - 1)
        elif kth_value > pivot_index:
            return self.quickselect(kth_value, pivot_index + 1, right)
        else:
            return self.array[pivot_index]


if __name__ == "__main__":
    array = QuicksortArray([0, 5, 2, 1, 6, 3])

    array.quicksort(0, len(array) - 1)
    print(array)

    kth_value = array.quickselect(1, 0, len(array) - 1)
    print(kth_value)
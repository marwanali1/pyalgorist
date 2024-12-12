from typing import TypeVar

T = TypeVar("T")


class QuicksortArray:
    def __init__(self, elems: list[T]) -> None:
        self._elems = elems if elems else []

    @property
    def elems(self) -> list[T]:
        return self._elems

    def __len__(self) -> int:
        return len(self.elems)

    def __repr__(self) -> str:
        return f"QuicksortArray({self.elems})"

    def __str__(self) -> str:
        return str(self.elems)

    def partition(self, left: int, right: int) -> int:
        # Set pivot to the right most value in the array
        pivot_index = right
        pivot = self.elems[right]

        # Move right pointer to value directly before the pivot
        right -= 1

        while True:
            # Shift left point until it reaches a value greater than or equal to the pivot
            while self.elems[left] < pivot:
                left += 1

            # Shift right pointer until it reaches a value less than of equalt to the pivot
            while self.elems[right] > pivot:
                right -= 1

            # If left and right pointers meet or pass each other break out of the loop
            if left >= right:
                break

            # Swap the values of left and right when both pointers have stopped
            self.elems[left], self.elems[right] = (
                self.elems[right],
                self.elems[left],
            )
            left += 1

        # If the pivot is less than the left value, swap the pivot and the left value
        if pivot < self.elems[left]:
            (
                self.elems[left],
                self.elems[pivot_index],
            ) = (
                self.elems[pivot_index],
                self.elems[left],
            )

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
            return self.elems[left]

        pivot_index = self.partition(left, right)

        if kth_value < pivot_index:
            return self.quickselect(kth_value, left, pivot_index - 1)

        if kth_value > pivot_index:
            return self.quickselect(kth_value, pivot_index + 1, right)

        return self.elems[pivot_index]

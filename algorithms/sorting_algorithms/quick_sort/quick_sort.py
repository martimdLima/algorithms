from typing import List, Tuple
import random


def quick_sort(self, arr: List[int]) -> None:
    def partition_3way(arr: List[int], low: int, high: int) -> Tuple[int, int]:
        """
        Partitions the array into three parts: elements less than the pivot,
        elements equal to the pivot, and elements greater than the pivot.

        Args:
            arr (List[int]): The list of integers to partition.
            low (int): The starting index of the partition range.
            high (int): The ending index of the partition range.

        Returns:
            (int, int): The indices where the middle (equal to pivot) section starts and ends.
        """
        pivot_index = random.randint(low, high)
        pivot = arr[pivot_index]

        arr[low], arr[pivot_index] = arr[pivot_index], arr[low]

        lt = low  # Partition boundary for elements less than pivot
        gt = high  # Partition boundary for elements greater than pivot
        i = low  # Current element index

        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                arr[gt], arr[i] = arr[i], arr[gt]
                gt -= 1
            else:
                i += 1

        return lt, gt

    def quick_sort_recursive(arr: List[int], low: int, high: int) -> None:
        """
        Recursively applies the 3-way quick sort algorithm to the array.

        Args:
            arr (List[int]): The list of integers to sort.
            low (int): The starting index of the sort range.
            high (int): The ending index of the sort range.
        """
        if low < high:
            lt, gt = partition_3way(arr, low, high)
            quick_sort_recursive(arr, low, lt - 1)
            quick_sort_recursive(arr, gt + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)

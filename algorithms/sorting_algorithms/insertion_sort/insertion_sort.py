from Typing import List


def insertion_sort(self, nums: List[int]) -> None:
    """
    Sorts a list of integers in ascending order using the insertion sort algorithm.

    Insertion sort is a simple comparison-based sorting algorithm that builds the final
    sorted array one item at a time. It is much less efficient on large lists compared
    to more advanced algorithms like quicksort, heapsort, or merge sort. However, it is
    efficient for small datasets or partially sorted lists. It works by repeatedly picking
    the next element and inserting it into its correct position among the previously sorted
    elements.

    Parameters
    ----------
    nums : List[int]
        A list of integers to be sorted in place.

    Returns
    -------
    None
        The input list is modified in place to be in ascending order.

    Example
    -------
    >>> nums = [12, 11, 13, 5, 6]
    >>> insertion_sort(nums)
    >>> print(nums)
    [5, 6, 11, 12, 13]

    Notes
    -----
    - This implementation sorts the list in ascending order.
    - The time complexity of insertion sort is O(n^2) in the worst case, where n is the
      number of elements in the list. It has a best-case time complexity of O(n) when the
      list is already sorted.
    - The space complexity is O(1), as insertion sort is an in-place sorting algorithm.
    - Insertion sort is a stable sorting algorithm, meaning that it preserves the relative
      order of equal elements.

    """
    arr_length = len(nums)

    if arr_length <= 1:
        return
    for i in range(1, arr_length):
        current_element = nums[i]
        j = i - 1  # previous element index
        while j >= 0 and current_element < nums[j]:
            nums[j + 1] = nums[j]  # shift elements to the right
            j -= 1
        # Place current_element at its correct position
        nums[j + 1] = current_element

from Typing import List


def bubble_sort(self, arr: List[int]) -> None:
    """
    Sorts a list of integers in ascending order using the bubble sort algorithm.

    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order. The pass
    through the list is repeated until the list is sorted. The algorithm is known for
    its simplicity but is not suitable for large datasets due to its O(n^2) time complexity.

    Parameters:
    ----------
    arr : List[int]
        A list of integers to be sorted in place.

    Returns:
    -------
    None
        The input list is modified in place to be in ascending order.

    Example:
    -------
    >>> arr = [64, 34, 25, 12, 22, 11, 90]
    >>> bubble_sort(arr)
    >>> print(arr)
    [11, 12, 22, 25, 34, 64, 90]

    Notes:
    -----
    - This implementation sorts the list in ascending order.
    - It has a worst-case and average-case time complexity of O(n^2), where n is the
      number of elements in the list.
    - Bubble sort is stable; it does not change the relative order of elements with
      equal keys.
    """

    arr_length = len(arr)

    for i in range(arr_length):
        # Last i elements are already in place
        for j in range(0, arr_length - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

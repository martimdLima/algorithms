from Typing import List


def selection_sort(self, arr: List[int]) -> None:
    """
    Sorts a list of integers in ascending order using the selection sort algorithm.

    Selection sort is an in-place comparison-based sorting algorithm. It works by
    dividing the list into a sorted and an unsorted region. It repeatedly selects the
    smallest (or largest, depending on sorting order) element from the unsorted region and
    moves it to the end of the sorted region.

    Parameters
    ----------
    arr : List[int]
        A list of integers to be sorted in place.

    Returns
    -------
    None
        The input list is modified in place to be in ascending order.

    Example
    -------
    >>> arr = [64, 25, 12, 22, 11]
    >>> selection_sort(arr)
    >>> print(arr)
    [11, 12, 22, 25, 64]

    Notes
    -----
    - This implementation sorts the list in ascending order.
    - The time complexity of selection sort is O(n^2), where n is the number of elements
      in the list. This is due to the nested loops that find the minimum element and perform
      the swap.
    - The space complexity is O(1), as selection sort is an in-place sorting algorithm.
    - Selection sort is not a stable sorting algorithm, meaning that it may change the
      relative order of equal elements.

    """
    arr_length = len(arr)

    for idx in range(0, arr_length):
        min_val = idx

        for jidx in range(idx + 1, arr_length):
            # update minimum value
            if arr[jidx] < arr[min_val]:
                min_val = jidx

        # Swap only if a smaller element was found
        if min_val != idx:
            arr[idx], arr[min_val] = arr[min_val], arr[idx]

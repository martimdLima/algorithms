from Typing import List


def merge_sort(self, arr: List[int]) -> None:
    """
    Sorts a list of integers in ascending order using the merge sort algorithm.

    Merge sort is a divide-and-conquer sorting algorithm that divides the list into two
    halves, recursively sorts each half, and then merges the two sorted halves to produce
    a fully sorted list. Merge sort is efficient and has a guaranteed time complexity of
    O(n log n) in the worst, average, and best cases.

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
    >>> arr = [38, 27, 43, 3, 9, 82, 10]
    >>> merge_sort(arr)
    >>> print(arr)
    [3, 9, 10, 27, 38, 43, 82]

    Notes
    -----
    - This implementation sorts the list in place.
    - The time complexity of merge sort is O(n log n) for all cases.
    - The space complexity is O(n) due to the additional space used for merging.
    - Merge sort is a stable sorting algorithm, meaning it preserves the relative order of equal elements.

    """

    def merge(left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    arr_length = len(arr)
    if arr_length <= 1:
        return

    mid = arr_length // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    self.merge_sort(left)
    self.merge_sort(right)

    # Merge sorted halves
    sorted_arr = merge(left, right)

    # Copy the sorted array back into the original array
    arr[:] = sorted_arr

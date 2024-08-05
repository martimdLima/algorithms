def binary_search_iterative(array, target, left, right):
    """
    Performs an iterative binary search on a sorted array.

    This function searches for a specified element `target` within the `array`
    using an iterative approach. It returns the index of the element if 
    found, or -1 if the element is not present.

    Parameters
    ----------
    array : List[int]
        A sorted list of integers in which to search for the element `target`.
    target : int
        The target element to search for in the array.
    left : int
        The starting index of the subarray to search within.
    right : int
        The ending index of the subarray to search within.

    Returns
    -------
    int
        The index of the target element `target` if found; otherwise, -1.

    Example
    -------
    >>> arr = [1, 2, 3, 4, 5]
    >>> binary_search_iterative(arr, 3, 0, len(arr)-1)
    2

    Notes
    -----
    - The input array must be sorted in ascending order for the binary search 
      algorithm to work correctly.
    - The time complexity of binary search is O(log n), where n is the number 
      of elements in the array.
    - This function uses an iterative approach to avoid potential stack overflow 
      issues associated with deep recursion.
    """
    
    
    while left <= right:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(array, target, left, right):
    """
    Performs a recursive binary search on a sorted array.

    This function searches for a specified element `target` within the `array`
    using a recursive approach. It returns the index of the element if found,
    or -1 if the element is not present.

    Parameters
    ----------
    array : List[int]
        A sorted list of integers in which to search for the element `target`.
    target : int
        The target element to search for in the array.
    left : int
        The starting index of the subarray to search within.
    right : int
        The ending index of the subarray to search within.

    Returns
    -------
    int
        The index of the target element `target` if found; otherwise, -1.

    Example
    -------
    >>> arr = [1, 2, 3, 4, 5]
    >>> binary_search_recursive(arr, 3, 0, len(arr)-1)
    2

    Notes
    -----
    - The input array must be sorted in ascending order for the binary search 
      algorithm to work correctly.
    - The time complexity of binary search is O(log n), where n is the number 
      of elements in the array.
    - This function uses recursion and may lead to a stack overflow for very large 
      arrays due to excessive recursive depth.
    """
    if right >= left:
        mid = left + (right - left) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search_recursive(array, target, left, mid - 1)
        else:
            return binary_search_recursive(array, target, mid + 1, right)

    else:
        return -1

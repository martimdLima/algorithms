<p align="center">

  <h3 align="center">912. Sort an Array</h3>

  <p align="center">
    Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
    <br>
  </p>
</p>

## Problem Description

Given an array of integers $nums$, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in $O(nlog(n))$ time complexity and with the smallest space complexity possible.

## Examples

- **Example 1**:

  - **Input:** nums = [5,2,3,1]
  - **Output:** [1,2,3,5]
  - **Explanation:** After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

- **Example 2**:

  - **Input:** nums = [5,1,1,2,0,0]
  - **Output:** [0,0,1,1,2,5]
  - **Explanation:** Note that the values of nums are not necessairly unique.

## Constraints

- $1 \leq nums.length \leq 5 * 10^4$
- $-5 * 10^4 \leq nums[i] \leq 5 * 10^4$

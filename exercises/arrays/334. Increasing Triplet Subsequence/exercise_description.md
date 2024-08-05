<p align="center">

  <h3 align="center">334. Increasing Triplet Subsequence</h3>

  <p align="center">
    Array, Greedy
    <br>
  </p>
</p>

## Problem Description

Given an integer array $nums$, return $true$ if there exists a triple of indices (i, j, k)$ such that $i < j < k$ and $nums[i] < nums[j] < nums[k]$. If no such indices exists, return false.

## Examples

- **Example 1**:

  - **Input:** nums = [1,2,3,4,5]
  - **Output:** true
  - **Explanation:** Any triplet where i < j < k is valid.

- **Example 2**:

  - **Input:** nums = [5,4,3,2,1]
  - **Output:** false
  - **Explanation:** No triplet exists.

- **Example 3**:

  - **Input:** nums = [2,1,5,0,4,6]
  - **Output:** true
  - **Explanation:** The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

## Constraints

- $1 \leq nums.length \leq 5 * 10^5$
- $-2^31 \leq nums.length \leq 2^31 - 1$

## Folow Up

- Could you implement a solution that runs in $O(n)$ time complexity and $O(1)$ space complexity?

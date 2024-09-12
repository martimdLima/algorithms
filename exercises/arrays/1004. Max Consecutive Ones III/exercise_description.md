<p align="center">

  <h3 align="center">1004. Max Consecutive Ones III</h3>

  <p align="center">
    Array, Binary Search, Sliding Window, Prefix Sum
    <br>
  </p>
</p>

## Problem Description

Given a binary array $nums$ and an integer $k$, return the _maximum number of consecutive $1$'s in the array if you can flip at most $k$ $0$'s_.

## Examples

- **Example 1**:

  - **Input:** nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
  - **Output:** 6
  - **Explanation:** [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

- **Example 2**:

  - **Input:** nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
  - **Output:** 10
  - **Explanation:** [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

## Constraints

- $1 \leq nums.length \leq 10^5$
- $nums[i]$ is either $0$ or $1$.
- $0 \leq k \leq nums.length$

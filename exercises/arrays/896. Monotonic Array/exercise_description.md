<p align="center">

  <h3 align="center">896. Monotonic Array</h3>

  <p align="center">
    Array
    <br>
  </p>
</p>

## Problem Description

An array is **monotonic** if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all $i \leq j$, $nums[i] \leq nums[j]$. An array nums is monotone decreasing if for all $i \leq j$, $nums[i] \geq nums[j]$.

Given an integer array `nums`, *return* `true` *if the given array is monotonic, or* `false` *otherwise*.

## Examples
- **Example 1**:
  - **Input**: nums = [1,2,2,3]
  - **Output**: true

- **Example 2**:
  - **Input**: nums = [6,5,4,4]
  - **Output**: true

- **Example 3**:
  - **Input**: nums = [1,3,2]
  - **Output**: false

## Constraints
- $1 \leq nums.length \leq 10^5$
- $10^5 \leq nums[i] \leq 10^5$
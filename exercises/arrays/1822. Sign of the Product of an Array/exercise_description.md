<p align="center">

  <h3 align="center">1822. Sign of the Product of an Array</h3>

  <p align="center">
    Array, Math
    <br>
  </p>
</p>

## Problem Description

There is a function $signFunc(x)$ that returns:

- $1$ if $x$ is positive.
- -$1$ if $x$ is negative.
- $0$ if $x$ is equal to 0.

You are given an integer array $nums$. Let $product$ be the product of all values in the array $nums$.

Return $signFunc(product)$.

## Examples

- **Example 1**:

  - **Input**: nums = [-1,-2,-3,-4,3,2,1]
  - **Output**: 1
  - **Explanation**: The product of all values in the array is 144, and signFunc(144) = 1

- **Example 2**:

  - **Input**: nums = [1,5,0,2,-3]
  - **Output**: 0
  - **Explanation**: The product of all values in the array is 0, and signFunc(0) = 0

- **Example 3**:
  - **Input**: nums = [-1,1,-1,1,-1]
  - **Output**: -1
  - **Explanation**: The product of all values in the array is -1, and signFunc(-1) = -1

## Constraints

- $1 \leq nums.length \leq 1000$
- $-100 \leq nums[i] \leq 100$
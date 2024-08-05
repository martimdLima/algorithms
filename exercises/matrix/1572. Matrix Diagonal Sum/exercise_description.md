<p align="center">

  <h3 align="center">1572. Matrix Diagonal Sum</h3>

  <p align="center">
    Arrays, Matrix
    <br>
  </p>
</p>

## Problem Description

Given a square matrix $mat$, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

## Examples

- **Example 1**:
    <p><img align="top"  height="180" width="340" src="https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png"><p>

  - **Input**: mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
  - **Output**: 25
  - **Explanation**: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
    Notice that element mat[1][1] = 5 is counted only once.

- **Example 2**:

  - **Input**: mat = [[1,1,1,1],
        [1,1,1,1],
        [1,1,1,1],
        [1,1,1,1]]
  - **Output**: 8

- **Example 3**:

  - **Input**: mat = [[5]]
  - **Output**: 5

- **Example 3**:
  - **Input**: accounts = [[2,8,7],[7,1,3],[1,9,5]]
  - **Output**: 17

## Constraints

- $n == mat.length == mat[i].length$
- $1 \leq n \leq 100$
- $1 \leq mat[i][j] \leq 100$

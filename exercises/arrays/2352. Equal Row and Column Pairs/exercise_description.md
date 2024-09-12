<p align="center">

  <h3 align="center">2352. Equal Row and Column Pairs</h3>

  <p align="center">
    Array, Two Pointers, Greedy
    <br>
  </p>
</p>

## Problem Description

Given a **0-indexed** $n x n$ integer matrix $grid$, _return the number of pairs $(ri, cj)$ such that row $ri$ and column $cj$ are equal_.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

## Examples

- **Example 1**:
    <p><img align="top" width="150" height="153" src="https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg"></p>

  - **Input:** grid = [[3,2,1],[1,7,6],[2,7,7]]
  - **Output:** 1
  - **Explanation:** There is 1 equal row and column pair:
    - (Row 2, Column 1): [2,7,7]

- **Example 2**:
    <p><img align="top" width="200" height="209" src="https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg"></p>

  - **Input:** grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
  - **Output:** 3
  - **Explanation:** There are 3 equal row and column pairs:
    - (Row 0, Column 0): [3,1,2,2]
    - (Row 2, Column 2): [2,4,2,2]
    - (Row 3, Column 2): [2,4,2,2]

## Constraints

- $n == grid.length == grid[i].length$
- $1 \leq n \leq 200$
- $1 \leq grid[i][j] \leq 10^5$

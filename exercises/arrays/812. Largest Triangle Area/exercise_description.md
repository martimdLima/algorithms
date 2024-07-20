<p align="center">

  <h3 align="center">812. Largest Triangle Area</h3>

  <p align="center">
    Array, Math, Geometry
    <br>
  </p>
</p>

## Problem Description

Given an array of points on the **X-Y** plane points where $points[i] = [xi, yi]$, _return the area of the largest triangle that can be formed by any three different points_. Answers within $10^{-5}$ of the actual answer will be accepted.

## Examples

- **Example 1**:
  <p><img align="top"  height="370" width="450" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png"><p>

  - **Input**: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
  - **Output**: 2.00000
  - **Explanation**: The five points are shown in the above figure. The red triangle is the largest.

- **Example 2**:
  - **Input**: points = [[1,0],[0,0],[0,1]]
  - **Output**: 0.50000

## Constraints

- $3 \leq points.length \leq 50$
- $-50 \leq xi, yi \leq 50$

<p align="center">

  <h3 align="center">1332. Check if is a Straight Line</h3>

  <p align="center">
    Array, Math, Geometry
    <br>
  </p>
</p>

## Problem Description

You are given an array $coordinates, coordinates[i] = [x, y]$, where $[x, y]$ represents the coordinate of a point. Check if these points make a straight line in the XY plane.

## Examples

- **Example 1**:
  <p><img align="top"  height="340" width="340" src="https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg"><p>
  
  - **Input**: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
  - **Output**: true

- **Example 2**:
  <p><img align="top"  height="350" width="340" src="https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg"><p>
  
  - **Input**: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
  - **Output**: false

## Constraints
- $2 \leq points.length \leq 1000$
- $coordinates[i].length == 2$
- $-10^4 \leq coordinates[i][0], coordinates[i][1] \leq 10^4$
- `coordinates` contains no duplicate point.

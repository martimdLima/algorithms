<p align="center">

  <h3 align="center">84. Largest Rectangle in Histogram</h3>

  <p align="center">
    Array, Stack, Monotonic Stack
    <br>
  </p>
</p>

## Problem Description

Given an array of integers $heights$ representing the histogram's bar height where the width of each bar is $1$, _return the area of the largest rectangle in the histogram_.

## Examples

- **Example 1**:
  <p><img align="top" width="520" height="240" src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg"></p>

  - **Input:** heights = [2,1,5,6,2,3]
  - **Output:** 10
  - **Explanation:** The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.

- **Example 2**:

      <p><img align="top" width="200" height="360" src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg"></p>

  - **Input:** heights = [2,4]
  - **Output:** 4
  - **Explanation:** The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.

## Constraints

- $1 \leq heights.length \leq 10^5$
- $0 \leq heights[i] \leq 10^4$

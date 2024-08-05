<p align="center">

  <h3 align="center">1502. Can Make Arithmetic Progression from Sequence</h3>

  <p align="center">
    Array, Sorting
    <br>
  </p>
</p>

## Problem Description

A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.

Given an array of numbers $arr$, return $true$ if the array can be rearranged to form an arithmetic progression. Otherwise, return $false$.


## Examples

- **Example 1**:  

  - **Input**: arr = [3,5,1]
  - **Output**: true
  - **Explanation**: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
- **Example 2**:  

  - **Input**: arr = [1,2,4]
  - **Output**: false
  - **Explanation**: There is no way to reorder the elements to obtain an arithmetic progression.

## Constraints

- $2 \leq arr.length \leq 1000$
- $-10^6 \leq arr[i] \leq 10^6$

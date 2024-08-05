<p align="center">

  <h3 align="center">2418. Sort the People</h3>

  <p align="center">
    Arrays, Hashtable, String, Sorting
    <br>
  </p>
</p>

## Problem Description

You are given an array of strings $names$, and an array $heights$ that consists of distinct positive integers. Both arrays are of length $n$.

For each index $i$, $names[i]$ and $heights[i]$ denote the name and height of the $i^{th}$ person.

Return $names$ _sorted in **descending** order by the people's heights_.

## Examples

- **Example 1**:
  - **Input**: names = ["Mary","John","Emma"], heights = [180,165,170]
  - **Output**: ["Mary","Emma","John"]
  - **Explanation**: Mary is the tallest, followed by Emma and John.  
  
- **Example 2**:
  - **Input**: names = ["Alice","Bob","Bob"], heights = [155,185,150]
  - **Output**: ["Bob","Alice","Bob"]
  - **Explanation**: The first Bob is the tallest, followed by Alice and the second Bob.

## Constraints

- $n == names.length == heights.length$
- $1 \leq n \leq 10^3$
- $1 \leq names[i].length \leq 20$
- $1 \leq heights[i] \leq 10^5$
- $names[i]$ consists of lower and upper case English letters.
- All the values of $heights$ are distinct.

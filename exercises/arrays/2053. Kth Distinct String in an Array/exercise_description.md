<p align="center">

  <h3 align="center">2053. Kth Distinct String in an Array</h3>

  <p align="center">
    Array, Hash Table, String, Counting
    <br>
  </p>
</p>

## Problem Description

A **distinct string** is a string that is present only **once** in an array.

Given an array of strings $arr$, and an integer $k$, return the $k^{th}$ **distinct string** present in $arr$. If there are **fewer** than $k$ distinct strings, return an **empty string** "".

Note that the strings are considered in the **order in which they appear** in the array.

## Examples

- **Example 1**:
    <p><img align="top" width="600" height="287" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg"></p>

  - **Input:** arr = ["d","b","c","b","c","a"], k = 2
  - **Output:** "a"
  - **Explanation:**
    - The only distinct strings in arr are "d" and "a".
    - "d" appears 1st, so it is the 1st distinct string.
    - "a" appears 2nd, so it is the 2nd distinct string.
    - Since k == 2, "a" is returned.

- **Example 2**:

  - **Input:** arr = ["aaa","aa","a"], k = 1
  - **Output:** "aaa"
  - **Expanation:** All strings in arr are distinct, so the 1st string "aaa" is returned.

- **Example 3**:

  - **Input:** arr = ["a","b","a"], k = 3
  - **Output:** ""
  - **Expanation:** The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

## Constraints

- $1 \leq k \leq arr.length \leq 1000 $
- $1 \leq arr[i].length \leq 5$
- $arr[i]$ consists of lowercase English letters.

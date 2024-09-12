<p align="center">

  <h3 align="center">2384. Largest Palindromic Number</h3>

  <p align="center">
    Array, Two Pointers, Sorting
    <br>
  </p>
</p>

## Problem Description

You are given a string $num$ consisting of digits only.

Return _the **largest palindromic** integer (in the form of a string) that can be formed using digits taken from num. It should not contain **leading zeroes**_.

Notes:

You do not need to use all the digits of $num$, but you must use **at least** one digit.
The digits can be reordered.

## Examples

- **Example 1**:

  - **Input:** num = "444947137"
  - **Output:** "7449447"
  - **Explanation:** Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
    It can be shown that "7449447" is the largest palindromic integer that can be formed.

- **Example 2**:

  - **Input:** num = "00009"
  - **Output:** "9"
  - **Explanation:** It can be shown that "9" is the largest palindromic integer that can be formed.
    Note that the integer returned should not contain leading zeroes.

## Constraints

- $1 \leq nums.length \leq 10^5$
- $num$ consists of digits.
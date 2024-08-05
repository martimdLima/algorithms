<p align="center">

  <h3 align="center">2071. Greatest Common Divisor of Strings</h3>

  <p align="center">
    String, Math
    <br>
  </p>
</p>

## Problem Description

For two strings $s$ and $t$, we say "$t$ divides $s$" if and only if $s = t + t + t + ... + t + t$ (i.e., $t$ is concatenated with itself one or more times).

Given two strings $str1$ and $str2$, return the _largest string_ $x$ _such that_ $x$ _divides both_ $str1$ _and_ $str2$.

## Examples

- **Example 1**:

  - **Input**: str1 = "ABCABC", str2 = "ABC"
  - **Output**: "ABC"

- **Example 2**:

  - **Input**: str1 = "ABABAB", str2 = "ABAB"
  - **Output**: "AB"

- **Example 3**:
  - **Input**: str1 = "LEET", str2 = "CODE"
  - **Output**: ""

## Constraints

- $1 \leq str1.length, str2.length \leq 1000$
- $str1$ and $str2$ consist of English uppercase letters.

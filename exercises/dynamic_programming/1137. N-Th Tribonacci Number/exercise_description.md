<p align="center">

  <h3 align="center">1137. N-th Tribonacci Number</h3>

  <p align="center">
    Math, Dynamic Programming, Memoization
    <br>
  </p>
</p>

## Problem Description

The Tribonacci sequence Tn is defined as follows:

$T_0 = 0,  T_1 = 1, T_2 = 1 \quad and \quad T_{n+3} = T_n + T_{n+1} + T_{n+2} \quad for \quad n \geq 0$

Given $n$, return the value of $T_n$.

## Examples

- **Example 1**:

  - **Input**
    ["RecentCounter", "ping", "ping", "ping", "ping"]
    [[], [1], [100], [3001], [3002]]
  - **Output**
    [null, 1, 2, 3, 3]
  - **Explanation:**
    - T_3 = 0 + 1 + 1 = 2
    - T_4 = 1 + 1 + 2 = 4

## Constraints

- $0 \leq n \leq 37$
- Each test case will call $ping$ with **strictly increasing** values of $t$.
- The answer is guaranteed to fit within a 32-bit integer, ie. $answer \leq 2^31 - 1$.

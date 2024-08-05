<p align="center">

  <h3 align="center">1653. Minimum Number of Deletions to Make String Balanced</h3>

  <p align="center">
    String, Dynamic Programming, Stack
    <br>
  </p>
</p>

## Problem Description

You are given a string s consisting only of characters $'a'$ and $'b'$​​​​.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices $(i,j)$ such that $i < j$ and $s[i] = 'b'$ and $s[j]= 'a'$.

Return _the **minimum number** of deletions needed to make $s$ **balanced**_.

## Examples

- **Example 1**:

  - **Input:** s = "aababbab"
  - **Output:** 2
  - **Explanation:** You can either:
    - Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
    - Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

- **Example 2**:

  - **Input:** s = "bbaaaaabb"
  - **Output:** 2
  - **Explanation:** The only solution is to delete the first two characters.

## Constraints

- $1 \leq s.length \leq 10^5$
- $s[i]$ is $'a'$ or $'b'$​​.

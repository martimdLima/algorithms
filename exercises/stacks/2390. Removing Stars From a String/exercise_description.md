<p align="center">

  <h3 align="center">2390. Removing Stars From a String</h3>

  <p align="center">
    Hash Table, String, Sorting, Counting
    <br>
  </p>
</p>

## Problem Description

You are given a string `s`, which contains stars `*`.

In one operation, you can:

Choose a star in `s`.
Remove the closest **non-star** character to its _left_, as well as remove the star itself.
_Return the string after *all* stars have been removed._

**Note**:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.

## Examples

- **Example 1**:

  - **Input:** s = "leet\**cod*e"
  - **Output:** "lecoe"
  - **Explanation:** Performing the removals from left to right:

- The closest character to the 1st star is 't' in "leet\**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod\*e".
- The closest character to the 3rd star is 'd' in "lecod\*e". s becomes "lecoe".
  There are no more stars, so we return "lecoe".

- **Example 2**:

  - **Input:** s = "erase**\***"
  - **Output:** ""
  - **Output:** The entire string is removed, so we return an empty string.

## Constraints

- $1 \leq s.length \leq 10^5$
- `s` consists of lowercase English letters and stars `*`.
- The operation above can be performed on `s`.

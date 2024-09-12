<p align="center">

  <h3 align="center">1657. Determine if Two Strings Are Close</h3>

  <p align="center">
    Hash Table, String, Sorting, Counting
    <br>
  </p>
</p>

## Problem Description

Two strings are considered **close** if you can attain one from the other using the following operations:

- Operation 1: Swap any two **existing** characters.
  - For example, abcde -> aecdb
- Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
  - For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.

Given two strings, `word1` and `word2`, _return $true$ if `word1` and `word2` are close, and $false$ otherwise._

## Examples

- **Example 1**:

  - **Input:** word1 = "abc", word2 = "bca"
  - **Output:** True
  - **Explanation:** You can attain word2 from word1 in 2 operations.
    Apply Operation 1: "abc" -> "acb"
    Apply Operation 1: "acb" -> "bca"

- **Example 2**:

  - **Input:** word1 = "a", word2 = "aa"
  - **Output:** False
  - **Output:** It is impossible to attain word2 from word1, or vice versa, in any number of operations.

- **Example 1**:

  - **Input:** word1 = "cabbba", word2 = "abbccc"
  - **Output:** True
  - **Explanation:** You can attain word2 from word1 in 3 operations.
    Apply Operation 1: "cabbba" -> "caabbb"
    Apply Operation 2: "caabbb" -> "baaccc"
    Apply Operation 2: "baaccc" -> "abbccc"

## Constraints

- $1 \leq word1.length, word2.length \leq 10^5$
- `word1` and `word2` contain only lowercase English letters.

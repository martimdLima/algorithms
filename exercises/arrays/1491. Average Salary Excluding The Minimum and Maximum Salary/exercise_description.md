<p align="center">

  <h3 align="center">1491. Average Sakary Withou the Minimum and Maximum Salary</h3>

  <p align="center">
    Array, Sorting
    <br>
  </p>
</p>

## Problem Description

You are given an array of unique integers salary where $salary[i]$ is the salary of the $i^{th}$ employee.

Return the _average salary of employees excluding the minimum and maximum salary_. Answers within $10^{-5}$ of the actual answer will be accepted.

## Examples

- **Example 1**:

  - **Input**: salary = [4000,3000,1000,2000]
  - **Output**: 2500.00000
  - **Explanation**: Minimum salary and maximum salary are 1000 and 4000 respectively. Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

- **Example 2**:
  - **Input**: salary = [1000,2000,3000]
  - **Output**: 2000.00000
  - **Explanation**: Minimum salary and maximum salary are 1000 and 3000 respectively. Average salary excluding minimum and maximum salary is (2000) / 1 = 2000

## Constraints

- $3 \leq salary.length \leq 100$
- $1000 \leq salary[i] \leq 10^6$
- All the integers of $salary$ _are unique_.

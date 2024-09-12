<p align="center">

  <h3 align="center">735. Asteroid Collision</h3>

  <p align="center">
    Array, Stack Simulation
    <br>
  </p>
</p>

## Problem Description

We are given an array `asteroids` of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

## Examples

- **Example 1**:

  - **Input:** asteroids = [5,10,-5]
  - **Output:** [5,10]
  - **Explanation:** The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

- **Example 2**:

  - **Input:** asteroids = [8,-8]
  - **Output:** []
  - **Output:** The 8 and -8 collide exploding each other.

- **Example 2**:

  - **Input:** asteroids = [10,2,-5]
  - **Output:** [10]
  - **Output:** The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

## Constraints

- $2 \leq asteroids.length \leq 10^4$
- $-1000 \leq asteroids[i] \leq 1000$
- $asteroids[i] != 0$
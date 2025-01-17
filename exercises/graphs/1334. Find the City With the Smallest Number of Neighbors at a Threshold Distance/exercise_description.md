<p align="center">

  <h3 align="center">1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance</h3>

  <p align="center">
    Dynamic Programming, Graph, Shortest Path
    <br>
  </p>
</p>

## Problem Description

There are $n$ cities numbered from $0$ to $n-1$. Given the array $edges$ where $edges[i] = [fromi, toi, weighti]$ represents a bidirectional and weighted edge between cities $\text{from}_i$ and $\text{to}_i$, and given the integer $distanceThreshold$.

Return the city with the smallest number of cities that are reachable through some path and whose distance is **at most** $distanceThreshold$, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

## Examples

- **Example 1:**
  <p><img align="top" width="300" height="225" src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_01.png"></p>

  - **Input:** n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4

  - **Output:** 3

  - **Explanation:** The figure above describes the graph. The neighboring cities at a distanceThreshold = 4 for each city are:
    - City 0 -> [City 1, City 2]
    - City 1 -> [City 0, City 2, City 3]
    - City 2 -> [City 0, City 1, City 3]
    - City 3 -> [City 1, City 2]
    - Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

- **Example 2:**
  <p><img align="top" width="300" height="225" src="https://assets.leetcode.com/uploads/2020/01/16/find_the_city_02.png"></p>

  - **Input:** n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]],

  - **Output:** 0

  - **Explanation:** The figure above describes the graph. The neighboring cities at a distanceThreshold = 4 for each city are:
    - City 0 -> [City 1, City 2]
    - City 1 -> [City 0, City 2, City 3]
    - City 2 -> [City 0, City 1, City 3]
    - City 3 -> [City 1, City 2]
    - Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

## Constraints

- $2 \leq  n \leq 100$
- $1 \leq  edges.length \leq n * (n - 1) / 2$
- $edges[i].length == 3$
- $0 \leq  \text{from}_i < \text{to}_i < n$
- $1 \leq \text{weight}_i, distanceThreshold \leq 10^4$
- All pairs $(\text{from}_i, \text{to}_i)$

<p align="center">

  <h3 align="center">3217. Delete Nodes From Linked List Present in Array</h3>

  <p align="center">
    Array, Hash Table, Linkied List
    <br>
  </p>
</p>

## Problem Description

You are given an array of integers `nums` and the `head` of a linked list. Return the `head` of the modified linked list after **removing** all nodes from the linked list that have a value that exists in `nums`.

&nbsp;

## Examples

**Example 1:**

**Input:** nums = [1,2,3], head = [1,2,3,4,5]  
**Output:** [4,5]  
**Explanation:**

![Example 1](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png)

Remove the nodes with values 1, 2, and 3.

&nbsp;

**Example 2:**

**Input:** nums = [1], head = [1,2,1,2,1,2]  
**Output:** [2,2,2]  
**Explanation:**

![Example 2](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png)

Remove the nodes with value 1.

&nbsp;

**Example 3:**

**Input:** nums = [5], head = [1,2,3,4]  
**Output:** [1,2,3,4]  
**Explanation:**

![Example 3](https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png)

No node has value 5.

&nbsp;

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
- All elements in `nums` are unique.
- The number of nodes in the given list is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`
- The input is generated such that there is at least one node in the linked list that has a value not present in `nums`.

---

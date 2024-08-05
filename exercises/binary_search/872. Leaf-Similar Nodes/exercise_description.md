<p align="center">

  <h3 align="center">872. Leaf-Similar Trees</h3>

  <p align="center">
    Tree, Depth-First Search, Binary Tree
    <br>
  </p>
</p>

## Problem Description

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence**.

<p><p><img align="top" width="400" height="336" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png"></p></p>
  
For example, in the given tree above, the leaf value sequence is $(6, 7, 4, 9, 8)$.

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return $true$ if and only if the two given trees with head nodes $root1$ and $root2$ are leaf-similar.

## Examples

- **Example 1**:

  <p><p><img align="top" width="600" height="247" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg"></p></p>
    
  **Input**: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
  **Output**: true

- **Example 2**:

  <p><p><img align="top" width="300" height="110" src="https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg"></p></p>

  **Input**: root1 = [1,2,3], root2 = [1,3,2]
  **Output**: false

## Constraints

- The number of nodes in each tree will be in the range $[1, 200]$.
- Both of the given trees will have values in the range $[0, 200]$.

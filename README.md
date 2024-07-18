<p align="center">
  <!--<a href="https://example.com/">
    <img src="https://via.placeholder.com/72" alt="Logo" width=72 height=72>
  </a>-->

  <h3 align="center">Algorithms & Data Structures</h3>

  <p align="center">
    Repository with a collection of examples of Data Structures, Algorithms and related exercises
    <br>
    <!--<a href="https://reponame/issues/new?template=bug.md">Report bug</a>
    ·
    <a href="https://reponame/issues/new?template=feature.md&labels=feature">Request feature</a>-->
  </p>
</p>


## Table of contents

- [Overview start](#overview)
- [What is an Algorithm](#what-is-an-algorithm)
- [What is a Data Structure](#what-is-a-data_structure)

## Overview
Welcome to the Algorithms and Data Structures Repository! This repository is dedicated to providing a comprehensive collection of fundamental and advanced algorithms, various data structures, and a wide range of related exercises to help you master these essential concepts. Whether you are a beginner or an experienced programmer, this repository aims to be your go-to resource for studying and practicing algorithms and data structures.

## What is an Algorithm?
An algorithm is a step-by-step procedure or a set of rules to solve a specific problem or perform a computation. Algorithms are the foundation of computer science and are used to process data, perform calculations, automate reasoning, and make decisions. They are essential for the development of software applications, enabling tasks such as sorting data, searching for information, and optimizing solutions.

  - **Sorting Algorithms**:
    - **Bubble Sort**: A simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
    - **Quick Sort**: An efficient, divide-and-conquer sorting algorithm that works by selecting a 'pivot' element and partitioning the array into two sub-arrays according to whether they are less than or greater than the pivot.
    - **Merge Sort**: A divide-and-conquer algorithm that divides the list into equal halves, sorts them, and then merges the sorted halves to produce a sorted list.

  - **Searching Algorithms**:
    - **Binary Search**: An efficient algorithm for finding an item from a sorted list of items by repeatedly dividing the search interval in half.
    - **Linear Search**: A simple algorithm that checks every element in the list until the desired element is found or the list ends.

  - **Graph Algorithms**:
    - **Depth-First Search (DFS)**: An algorithm for traversing or searching tree or graph data structures, starting at the root and exploring as far as possible along each branch before backtracking.
    - **Breadth-First Search (BFS)**: An algorithm for traversing or searching tree or graph data structures, starting at the root and exploring all neighbors at the present depth prior to moving on to nodes at the next depth level.

  - Dynamic Programming:
    - **Fibonacci Sequence**: Calculating the nth Fibonacci number using dynamic programming to store previously computed values.
    - **Knapsack Problem**: A problem in combinatorial optimization where the goal is to determine the most valuable combination of items that can fit in a knapsack of fixed capacity.

## What is a Data Structure?
A data structure is a way of organizing and storing data in a computer so that it can be accessed and modified efficiently. Data structures are crucial for managing large amounts of data and are integral to designing efficient algorithms. They define the relationship between data and the operations that can be performed on the data.

  - **Arrays**: A collection of items stored at contiguous memory locations. Elements can be accessed randomly using indices.
  - **Linked Lists**: A linear data structure where elements are stored in nodes, and each node points to the next node in the sequence.
  - **Stacks**: A collection of elements that follows the Last In, First Out (LIFO) principle.
  - **Queues**: A collection of elements that follows the First In, First Out (FIFO) principle.
  - **Trees**:
    - **Binary Trees**: A tree data structure where each node has at most two children.
    - **Binary Search Trees (BST)**: A binary tree in which each node has a value greater than all the values in its left subtree and less than those in its right subtree.
  - **Graphs**: A collection of nodes connected by edges, used to represent networks of relationships.
  - **Hash Tables**: A data structure that maps keys to values for efficient data retrieval.

## Repository Structure

```text
algorithms/
└── graph_algorithms/
└── searching_algorithms/
└── sorting_algorithms/
data_structures/
└── hash_based/
    ├── hash_maps/
    └── hash_tables/
└── linear/
    ├── dynamic_data/
    │    ├── linked_list
    │    ├── queue
    │    └── stack
    └── static_data/
        │    └── array
└── non_linear/
    ├── graph/
    └── tree/
exercises/
```

<!--```text
algorithms/
data_structures/
exercises/
└── folder2/
    ├── folder3/
    │   ├── file1
    │   └── file2
    └── folder4/
        ├── file3
        └── file4
```-->

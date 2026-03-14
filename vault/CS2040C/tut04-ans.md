---
tags: [CS2040C, lecture-notes, academic]
---

# Tutorial 04: Priority Queue

## Overview
This tutorial concludes the initial phase of CS2040C/IT5003, focusing on basic data structures and algorithms, including sorting algorithms and linear data structures. We will transition into non-linear data structures, specifically the [[Priority Queue]] (PQ) Abstract Data Type (ADT) and its implementation using a [[Binary Heap]]. The tutorial will also cover key operations and complexities associated with binary heaps.

## Key Concepts & Definitions
- **Priority Queue (PQ)**: An abstract data type where each element has a priority, and elements are served based on their priority.
- **Binary Heap**: A complete binary tree that satisfies the heap property; can be a max heap or min heap.
- **Big O Notation**: A mathematical notation used to describe the upper limit of the time complexity of an algorithm.
- **HeapSort**: A comparison-based sorting algorithm that uses a binary heap data structure.
- **ExtractMax()**: An operation that removes the maximum element from a max heap.
- **UpdateKey**: An operation that changes the value of a key in the heap.
- **DeleteKey**: An operation that removes a specific key from the heap.

## Detailed Technical Breakdown

### 1. Introduction and Objective
- **End of Phase 1**: Review of basic C++/Python/Java, algorithm analysis, and linear data structures.
- **Start of Phase 2**: Introduction to non-linear data structures, focusing on the Priority Queue ADT.

### 2. Tutorial Questions

#### Q1: Basic Binary Heap Operations
- Review operations available in [[VisuAlgo]] for Binary Heap.
- Focus on:
  - Changing modes between Complete Binary Tree and Compact Array.
  - Performing ExtractMax() and Insert operations.
  - Understanding the complexities of Create, UpdateKey, and Delete operations.

#### Q2: Comparisons in Binary Heap Construction
- **Minimum Comparisons**: 7 comparisons for an already max-heap array.
- **Maximum Comparisons**: 11 comparisons when the array requires maximum shifts down.

#### Q3: Finding Vertices Greater Than X
- **Algorithm**: Pre-order traversal of the max heap to find all vertices with values greater than x.
- **Time Complexity**: O(k), where k is the number of valid vertices found.

#### Q4: Converting Max Heap to Min Heap
- **Method**: Insert negated values into a new max heap.
- **Implementation**: Use of STL in C++ or heapq in Python.

#### Q5: Second Largest Element in Max Heap
- **Proof**: The second largest element must be a child of the root due to the max heap property.

#### Q6: Additional Binary Heap Operations
- **DecreaseKey**: Modify the key of an element and ensure the heap property is maintained.
- **DeleteKey**: Remove an arbitrary element from the heap.

### 3. Hands-on Activities
- Quick reviews of C++ STL, Java PriorityQueue, and Python heapq.
- Speed run of [[VisuAlgo]] online quizzes.
- Solve a Kattis/LeetCode problem involving the Priority Queue ADT.

> [!note] **Important**: Understanding the properties of binary heaps is crucial for efficient algorithm design and implementation in data structures.
> 
> [!warning] **Caution**: Ensure to grasp the complexities of operations as they can significantly impact performance in larger datasets.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Stacks and Queues]]
- [[Midterm+Briefing]]
- [[CS1231_TUTORIAL+4]]
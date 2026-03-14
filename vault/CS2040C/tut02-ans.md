---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C Tutorial 02: Sorting, ADT, List

## Overview
In this tutorial, we explore various [[Sorting]] algorithms and the concept of [[Abstract Data Type]] (ADT), particularly focusing on the List ADT. The session aims to enhance understanding of sorting techniques and their applications, as well as the theoretical underpinnings of ADTs, which are crucial throughout the course. Students are encouraged to utilize online resources for visual aids and deeper insights into the discussed topics.

## Key Concepts & Definitions
- **Sorting**: The process of arranging elements in a specified order, typically ascending or descending.
- **Abstract Data Type (ADT)**: A mathematical model for data types, defining operations without specifying implementation details.
- **List ADT**: A collection of elements that can be accessed by their position, supporting operations like insertion, deletion, and traversal.
- **Binary Search**: An efficient algorithm for finding an item from a sorted list by repeatedly dividing the search interval in half.
- **Median**: The middle value in a sorted list of numbers, which can be defined differently based on whether the count of numbers is odd or even.
- **QuickSelect**: An algorithm to find the k-th smallest element in an unordered list, utilizing partitioning similar to QuickSort.

## Detailed Technical Breakdown

### 1. Introduction and Objective
- Discuss the significance of sorting algorithms and ADTs in computer science.
- Review relevant online resources for visualization of sorting algorithms.

### 2. Tutorial Questions

#### Sorting Applications
- **Application 1**: [[Binary Search]] on sorted arrays.
- **Application 2**: Finding min/max and k-th smallest elements in a sorted array.
- **Application 3**: Detecting uniqueness in a sorted array.
- **Application 4**: Finding lower and upper bounds using binary search.
- **Application 5**: Set operations (intersection and union) on sorted arrays.
- **Application 6**: Solving the 2-SUM problem using binary search.
- **Application 7**: Counting elements within a range using binary search.

> [!note] **Important**: Understanding the efficiency of sorting algorithms is crucial for optimizing performance in various applications.

### 3. Sorting Mini Experiment
| Input Type → | Sorted | Nearly Sorted |
|---------------|--------|---------------|
| Algorithm     | Random | N-d | N-i | N-d | N-i | Many Duplicates |
| (Opt) Bubble Sort | O(N²) | O(N) | O(N²) | O(N) | O(N²) | O(N²) |
| (Min) Selection Sort | O(N²) | O(N²) | O(N²) | O(N²) | O(N²) | O(N²) |
| Insertion Sort | O(N²) | O(N) | O(N²) | O(N) | O(N²) | O(N²) |
| Merge Sort | O(N log N) | O(N log N) | O(N log N) | O(N log N) | O(N log N) | O(N log N) |
| Quick Sort | O(N log N) | O(N²) | O(N²) | O(N²) | O(N²) | O(N²) |
| (Rand) Quick Sort | O(N log N) | O(N log N) | O(N log N) | O(N log N) | O(N log N) | O(N log N) |
| Counting Sort | O(N) | O(N) | O(N) | O(N) | O(N) | O(N) |

### 4. Finding k-th Smallest Element
- **Algorithm**: QuickSelect
```python
def QuickSelect(A, l, r, k):
    if l == r:
        return A[l]
    PivotIndex = Randomized_Partition(A, l, r)
    if PivotIndex == k - 1:
        return A[PivotIndex]
    elif PivotIndex > k - 1:
        return QuickSelect(A, l, PivotIndex - 1, k)
    else:
        return QuickSelect(A, PivotIndex + 1, r, k)
```

### 5. Abstract Data Type (ADT)
- Discuss the List ADT and its operations.
- Compare fixed-size array implementations with dynamic implementations like Java's ArrayList.

> [!important] **Note**: Understanding ADTs is essential for implementing efficient data structures and algorithms.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[lec04a]]
- [[ch2]]
- [[lec04b]]
- [[Midterm+Briefing]]
- [[CS1231+TUTORIAL+3]]
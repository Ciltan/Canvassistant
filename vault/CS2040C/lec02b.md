---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 02b

## Overview
In this lecture, we explore various algorithms for sorting and manipulating data structures, particularly focusing on sorted arrays. We discuss practical applications, such as sorting a deck of cards and solving classic sorting puzzles. The session emphasizes the importance of space-time tradeoffs and introduces custom data structures to enhance understanding of Abstract Data Types (ADTs).

## Key Concepts & Definitions
- **Sorting Algorithms**: Techniques to arrange elements in a specific order. Common types include [[Bubble Sort]], [[Selection Sort]], and [[Insertion Sort]].
- **Space-Time Tradeoff**: A principle that suggests optimizing for either space or time can lead to better performance in algorithms.
- **Abstract Data Types (ADTs)**: A mathematical model for data types, defined by their behavior from the point of view of a user, rather than their implementation.
- **Custom ListArray Class**: A user-defined class in C++ that encapsulates an array of integers, allowing for operations such as adding, searching, and removing elements.

## Detailed Technical Breakdown

### Sorting Algorithms
- **Weak Sorting Algorithms**: 
  - Bubble Sort: O(n²)
  - Selection Sort: O(n²)
  - Insertion Sort: O(n²)
  
- **Efficient Sorting Algorithms**:
  - Quick Sort: O(n log n)
  - Merge Sort: O(n log n)

### Space-Time Tradeoff
- Example: Using a larger working memory can lead to faster sorting times, demonstrating the tradeoff between memory usage and execution speed.

### Custom ListArray Class Operations
- **Add Operation**: Insert a new or duplicate value at a specific index or at the end of the list.
- **Search Operation**: Find the index of a specific value.
- **Remove Operation**: Erase an element at a specific index.

### Example Implementations
#### Rank Problem Solution
```cpp
#include <iostream>
#include "ListArrayTest.cpp" // Custom ListArray class
using namespace std;

int main() {
    int n, m; cin >> n >> m;
    ListArray<int> rank;
    for (int i = 0; i < n; ++i)
        rank.add(i + 1);
    while (m--) {
        char d1, d2; int T1, T2; cin >> d1 >> T1 >> d2 >> T2; cin.ignore();
        int r1 = rank.indexOf(T1);
        int r2 = rank.indexOf(T2);
        if (r1 > r2) {
            rank.remove(r2);
            rank.add(r1, T2);
        }
    }
    for (int i = 0; i < n; ++i)
        cout << 'T' << rank.get(i) << ' ';
    cout << '\n';
    return 0;
}
```

#### Class Field Trip Problem
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    string ann; cin >> ann;
    string ben; cin >> ben;
    int i = 0, n = (int)ann.length(), j = 0, m = (int)ben.length();
    while (i < n && j < m) {
        if (ann[i] <= ben[j])
            cout << ann[i++];
        else
            cout << ben[j++];
    }
    while (i < n) cout << ann[i++];
    while (j < m) cout << ben[j++];
    return 0;
}
```

> [!note] **Important Note**: The custom ListArray class is not strictly necessary for solving the rank problem, as simpler data structures can suffice. However, it serves as a valuable exercise in understanding ADT operations.

> [!warning] **Caution**: When implementing sorting algorithms, be mindful of their time complexity, especially for larger datasets, as inefficient algorithms can lead to performance bottlenecks.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Stacks and Queues]]
- [[CS2113 - Software Engineering & Object-Oriented Programming]]
- [[Midterm+Briefing]]
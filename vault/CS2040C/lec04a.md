---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 04a

## Overview
In this lecture, we explore various Abstract Data Types (ADTs) including the List ADT, Stack ADT, Queue ADT, and Deque ADT. We discuss their implementations, advantages, and use cases, particularly focusing on linked data structures. Additionally, we provide important details regarding the upcoming midterm examination and a brief introduction to the Rancho Los Amigos Scale (RLAS).

## Key Concepts & Definitions
- **Abstract Data Type (ADT)**: A mathematical model that describes data, its possible values, and operations without detailing its implementation.
- **List ADT**: A collection of `n` similar type objects accessed via indices [0..n-1]. Common operations include [[get(i)]], [[search(v)]], [[insert(i, v)]], and [[remove(i)]].
- **Singly Linked List (SLL)**: A data structure where each element points to the next, allowing for dynamic memory allocation.
- **Stack ADT**: A collection that follows Last In First Out (LIFO) principle, where elements are added and removed from the same end.
- **Queue ADT**: A collection that follows First In First Out (FIFO) principle, where elements are added at one end and removed from the other.
- **Deque ADT**: A double-ended queue that allows insertion and deletion from both ends.

## Detailed Technical Breakdown

### Midterm Details
- **Venue**: MPSH 2A
- **Date and Time**: Tue, 03 Mar 26 (Week 7), 12:10 PM - 1:30 PM (80 mins)
- **Entry Time**: Earliest by 11:40 AM
- **Exit Time**: Latest by 1:45 PM
- Special arrangements for students with needs will be communicated separately.

### List ADT Review
- **Operations**:
  - `get(i)`: Access element at index `i`.
  - `search(v)`: Find value `v` in the list.
  - `insert(i, v)`: Insert value `v` at index `i`.
  - `remove(i)`: Remove element at index `i`.

| Operation       | C++ Vector Implementation         |
|------------------|----------------------------------|
| `get(i)`         | `L[i]`                           |
| `search(v)`      | `find(L.begin(), L.end(), v)`   |
| `insert(i, v)`   | `L.insert(iterator to i, v)`    |
| `remove(i)`      | `L.erase(iterator to i)`         |

### Singly Linked List (SLL) Review
- **Performance Comparison**:
  - `get(i)`: O(1) for arrays vs O(N) for SLL.
  - `insert(i, v)`: O(1) for SLL at head vs O(N) for arrays.
  - `remove(i)`: O(1) for SLL at head vs O(N) for arrays.

> [!important] The main advantage of SLL is its ability to allow non-contiguous memory allocation, which is beneficial for dynamic data structures like stacks and queues.

### Stack ADT Review
- **Implementation**:
  - Use SLL for Stack ADT.
  - Operations:
    - `top()`: `Get(0)` for SLL vs `s.top()` for C++ std::stack.
    - `push(v)`: `Insert(0, v)` for SLL vs `s.push(v)` for C++ std::stack.
    - `pop()`: `Remove(0)` for SLL vs `s.pop()` for C++ std::stack.

### Queue ADT Review
- **Implementation**:
  - Use SLL for Queue ADT.
  - O(1) performance for both enqueue and dequeue operations.

### Deque ADT Review
- **Implementation**:
  - Can be implemented using a Doubly Linked List (DLL) for efficient access at both ends.

## Implementation/Examples
```cpp
// Example of Stack ADT using SLL
class Stack {
    SLLNode* top;
public:
    void push(int value) {
        // Insert at head
    }
    void pop() {
        // Remove at head
    }
    int top() {
        // Return top value
    }
};
```

> [!note] For further practice, visit [VisuAlgo](https://visualgo.net/) for interactive training on data structures.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Stacks and Queues]]
- [[Singly Linked List]]
- [[Deque ADT]]
---
tags: [CS2040C, lecture-notes, academic]
---

# Tutorial 03: Linked List, Stack, Queue, Deque

## Overview
This tutorial focuses on the fundamental data structures of [[Linked List]], [[Stack]], [[Queue]], and [[Deque]]. Students will explore the variations of the [[List ADT]] and their respective operations, utilizing resources such as Visualgo for practical understanding. The session aims to deepen comprehension of the strengths and weaknesses of each data structure through hands-on experiments and algorithm implementations.

## Key Concepts & Definitions
- **Linked List**: A linear data structure where each element is a separate object, consisting of a data part and a reference (or link) to the next element in the sequence.
- **Stack**: A collection of elements that follows the Last In First Out (LIFO) principle.
- **Queue**: A collection of elements that follows the First In First Out (FIFO) principle.
- **Deque**: A double-ended queue that allows insertion and deletion from both ends.
- **List ADT**: An abstract data type that represents a sequence of elements, supporting various operations.

## Detailed Technical Breakdown

### 1. Introduction and Objective
- Review the [[List ADT]] and its variations, including:
  - Compact array-based List
  - Singly Linked List (SLL)
  - Stack
  - Queue
  - Doubly Linked List (DLL)
  - Deque

### 2. Tutorial Questions

#### Q1: Linked List Mini Experiment
- Use the Exploration Mode of Visualgo to complete the following table comparing operations across different linked list types.

| Mode → Action                | Singly Linked List | Stack | Queue | Doubly Linked List | Deque |
|------------------------------|--------------------|-------|-------|--------------------|-------|
| search(any-v)                | O(N)               | not allowed | not allowed | O(N)               | not allowed |
| peek-front()                 | O(1)               | O(1)  | O(1)  | O(1)               | O(1)  |
| peek-back()                  | O(1)               | not allowed | O(1)  | O(1)               | O(1)  |
| insert(0, new-v)             | O(1)               | O(1)  | not allowed | O(1)               | O(1)  |
| insert(N, new-v)             | O(1)               | not allowed | O(1)  | O(1)               | O(1)  |
| insert(i, new-v), i ∈[1..N-1]| O(N)               | not allowed | not allowed | O(N)               | not allowed |
| remove(0)                    | O(1)               | O(1)  | O(1)  | O(1)               | O(1)  |
| remove(N-1)                  | O(N)               | not allowed | not allowed | O(1)               | O(1)  |
| remove(i), i ∈[1..N-2]      | O(N)               | not allowed | not allowed | O(N)               | not allowed |

> [!note] **Important**: Understand the operations allowed in each data structure as they may vary across different implementations.

#### Q2: Implementing Additional Operations
1. **reverseList()**: 
   - Implement a function to reverse a Singly Linked List.
   - Time Complexity: O(N).
   - Possible methods:
     - Iterative method using a new list.
     - Pointer manipulation method.
     - Recursive method.

2. **sortList()**: 
   - Implement a function to sort a Singly Linked List.
   - Time Complexity: O(N log N).
   - Possible sorting algorithms:
     - Merge Sort.
     - Quick Sort.

> [!warning] **Note**: It is not possible to achieve better than Ω(N) for reversing a list, as all N items must change their pointers.

### 3. Stack, Queue, or Deque
#### Q3: Evaluating Lisp Expressions
- Design an algorithm using up to 2 stacks to evaluate a legal Lisp expression.
- The first stack stores tokens until an operator is encountered, then the second stack is used to reverse the order of operands for correct evaluation.

```cpp
#include <bits/stdc++.h>
using namespace std;

double performOperation(stack<double> &oprnds, char oprtor) {
    double result = 0.0;
    switch (oprtor) {
        case '+':
            result = 0.0;
            while (!oprnds.empty()) {
                result += oprnds.top();
                oprnds.pop();
            }
            return result;
        // Additional cases for '-', '*', and '/'...
    }
    return result; // unspecified behavior if operator invalid
}
```

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[lec04a]]
- [[ch2]]
- [[lec04b]]
- [[Midterm+Briefing]]
---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Optional LeetCode Summary

## Overview
This note summarizes the optional LeetCode exercises associated with the CS2040C course, focusing on data structures and algorithms. The exercises are designed to reinforce programming skills and algorithmic thinking through practical coding challenges. Each week covers specific topics, providing a structured approach to mastering the material discussed in lectures.

## Key Concepts & Definitions
- **Data Structures**: Ways to organize and store data for efficient access and modification. Examples include [[Stacks and Queues]], [[Linked Lists]], and [[Priority Queues]].
- **Algorithms**: Step-by-step procedures for calculations. Common algorithms include sorting algorithms and search algorithms.
- **LeetCode**: An online platform for practicing coding problems, often used to prepare for technical interviews.
- **Complexity Analysis**: Evaluating the efficiency of algorithms in terms of time and space, often expressed using Big O notation.

## Detailed Technical Breakdown

### Weekly Breakdown
- **Week 01**: Programming Skills Review
  - Focus on basic programming constructs and problem-solving techniques.
- **Week 02**: Advanced Data Structures
  - Introduction to more complex data structures like [[Stacks]], [[Queues]], and [[Linked Lists]].
- **Week 03**: Sorting Algorithms
  - Explore various sorting techniques and their complexities.
- **Week 04**: Linked Lists and Their Variants
  - Detailed examination of singly and doubly linked lists, including operations like insertion and deletion.
- **Week 05**: Priority Queues and Heaps
  - Understanding the implementation and application of priority queues.
- **Week 06**: Midterm Review
  - Consolidation of knowledge and preparation for the midterm exam.

### Exercise Guidelines
- **Consistency**: Engage with exercises daily to reinforce learning.
- **Time Management**: Allocate specific time slots for practice, especially during busy periods.
- **Self-Assessment**: Use LeetCode's timer feature to track progress without external help until completely stuck.

### Example Problems
#### Problem: Plus One
```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = (int)digits.size();
        for (int i = n-1; i >= 0; --i) {
            if (digits[i] < 9) {
                digits[i] += 1;
                break;
            } else {
                digits[i] = 0;
            }
        }
        if (digits[0] == 0) {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
```

#### Problem: Robot Return to Origin
```cpp
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0, y = 0;
        for (const auto& m : moves) {
            if (m == 'U') y++;
            else if (m == 'D') y--;
            else if (m == 'L') x--;
            else if (m == 'R') x++;
        }
        return (x == 0 && y == 0);
    }
};
```

> [!note] **Tip**: Always analyze the time complexity of your solutions to ensure efficiency, especially for larger inputs.

> [!warning] **Caution**: Avoid using external resources until you have attempted the problem independently to maximize learning.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]
- [[CS1231+TUTORIAL+3]]
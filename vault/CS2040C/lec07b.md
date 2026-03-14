---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C Lecture 07b: Union-Find Disjoint Set (UFDS)

## Overview
In this lecture, we explored the Union-Find Disjoint Set (UFDS) data structure, which is essential for efficiently managing and merging disjoint sets. We also conducted an early debrief of the midterm exam, discussing student feedback and grading progress. The session concluded with a live coding example related to the number of provinces problem, demonstrating the practical application of UFDS in algorithm optimization.

## Key Concepts & Definitions
- **Union-Find Disjoint Set (UFDS)**: A data structure that keeps track of a partition of a set into disjoint subsets and supports union and find operations efficiently.
- **Connected Components (CCs)**: A concept in graph theory where a connected component is a subset of a graph in which any two vertices are connected to each other by paths.
- **Live Coding**: An interactive programming session where the instructor codes in real-time, often used to demonstrate problem-solving techniques.

## Detailed Technical Breakdown

### Union-Find Disjoint Set (UFDS)
- **Operations**:
  - **Find**: Determine which subset a particular element is in.
  - **Union**: Merge two subsets into a single subset.
  
- **Applications**:
  - Efficiently solving problems related to connected components in graphs.
  - Speeding up algorithms that require dynamic connectivity queries.

### Midterm Exam Debrief
- **Attendance**: 155 students enrolled, with 149 attending the midterm.
- **Grading Status**:
  - Approximately 50 out of 152 assignments graded.
  - Verbal feedback on 20 out of 152 assignments.
  
- **Student Feedback**:
  - Positive reception of LeetCode emphasis and VisuAlgo.
  - Concerns regarding the weightage of the final exam and the flipped classroom approach.

### Example Problem: Number of Provinces
The following code snippet demonstrates the use of UFDS to solve the number of provinces problem:

```cpp
class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = (int)isConnected.size();
        UnionFind UF(n);
        for (int i = 0; i < n-1; ++i)
            for (int j = i+1; j < n; ++j)
                if (isConnected[i][j])
                    UF.unionSet(i, j);
        return UF.numDisjointSets();
    }
};
```

> [!note] **Important**: UFDS is not commonly featured in LeetCode problems, particularly at the Easy level. However, many problems related to finding connected components can be reclassified under UFDS.

> [!warning] **Caution**: While the flipped classroom model has its advantages, some students may struggle with the transition to C++ without additional support.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Logic - Propositional Logic]]
- [[Midterm+Briefing]]
- [[CS1231+TUTORIAL+3]]
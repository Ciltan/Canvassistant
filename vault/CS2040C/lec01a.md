---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C - Data Structures and Algorithms: Lecture 01

## Overview
This lecture serves as an introduction to the CS2040C course, focusing on Data Structures and Algorithms. Associate Professor Steven Halim outlines course administration, expectations, and resources available to students. Key changes from previous iterations of the course are highlighted, including a shift from Java to C++. The lecture emphasizes the importance of self-learning and engagement with programming challenges.

## Key Concepts & Definitions
- **Data Structures**: Ways to organize and store data for efficient access and modification.
- **Algorithms**: Step-by-step procedures for calculations or problem-solving.
- **Programming Competitions**: Competitive events where participants solve algorithmic problems under time constraints.
- **VisuAlgo**: An online platform for visualizing algorithms and data structures.
- **Kattis**: An online judge for programming exercises used in the course.
- **Flipped Classroom**: An instructional strategy where students learn content online and engage in interactive activities in class.

## Detailed Technical Breakdown

### Course Administration
- **Lecturer**: Associate Professor Steven Halim
- **Contact Information**:
  - Office: COM2-03-37
  - Email: dcssh@nus.edu.sg
  - Discord: 'prof halim'
- **Office Hours**: Mon-Fri, 10:30 AM - 5:30 PM (8:30 PM on Wed)

### Course Changes
- Transition from Java to C++ while maintaining other course elements.
- Adjustments to the final assessment weight from 60% to potentially 50%.

### Student Expectations
- Students are expected to have prior knowledge of at least one programming language.
- Self-learning is encouraged, with resources provided for assistance.

### Learning Tools
- **VisuAlgo**: A tool for algorithm visualization, developed by the lecturer.
- **Kattis**: Used for graded programming exercises and problem sets.

### Flipped Classroom Strategies
- Students must engage with e-Lecture slides prior to class to maximize understanding.
- Class time will focus on discussing complex topics and solving practical problems.

## Implementation/Examples
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n; 
    cin >> n;
    vector<long long> a(n); // Use long long for large integers
    for (int i = 0; i < n; ++i)
        cin >> a[i];
    cout << *max_element(a.begin(), a.end()) << " ";
    cout << *min_element(a.begin(), a.end()) << '\n';
    return 0;
}
```

> [!note] **Important**: Students are encouraged to declare any struggles with prerequisite courses early to receive assistance.
> 
> [!warning] **Caution**: Avoid using personal emails for Kattis registration to ensure proper identification and grading.

## Related
- [[AY2122+Sem1+Homework+1(S)]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[CS1231+TUTORIAL+3]]
- [[VisuAlgo]]
- [[Kattis]]
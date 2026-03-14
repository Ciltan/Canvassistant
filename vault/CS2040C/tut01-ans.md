---
tags: [CS2040C, lecture-notes, academic]
---

# CS2040C/IT5003 Tutorial 01: Basic C++/Python and Algorithm Analysis

## Overview
This tutorial serves as an introduction to the CS2040C/IT5003 course, focusing on basic programming in C++ and Python, alongside fundamental algorithm analysis. Students will engage in hands-on coding exercises and problem-solving sessions, utilizing platforms like Kattis and LeetCode. The tutorial emphasizes active participation and encourages students to seek clarification on any doubts with their Teaching Assistant (TA).

## Key Concepts & Definitions
- **C++**: A high-level programming language that supports object-oriented programming and is widely used for system/software development.
- **Python**: A versatile, high-level programming language known for its readability and ease of use, particularly in data analysis and web development.
- **Algorithm Analysis**: The study of the efficiency of algorithms in terms of time and space complexity.
- **List ADT**: An Abstract Data Type that represents a collection of elements, allowing for various operations such as insertion and deletion.
- **Kattis**: An online platform for competitive programming where students can submit their code for automatic judging.
- **LeetCode**: A platform that provides coding challenges to help improve programming skills.

## Detailed Technical Breakdown

### 1. Introduction and Objective
- Recap of initial sessions covering C++/Python basics and algorithm analysis.
- Ensure students can code and submit solutions on Kattis/LeetCode.
- Structure of the session: tutorial followed by hands-on lab.

### 2. Tutorial Structure
- **Ice Breaking**: Introduction to the TA as the primary contact for course-related queries.
- **Participation Guidelines**:
  - Attempt all tutorial questions.
  - Use Gen AI tools for assistance after personal effort.
  - Participation marks awarded based on engagement.

### 3. Tutorial Questions
#### Q1: Code Scrutiny
- **ListArrayTest.cpp** (CS2040C) / **ListArrayTest.py** (IT5003)
  - Analyze specific lines of code for functionality and potential issues.
  - Discuss differences in handling data types between C++ and Python.

#### Q2: Order of Growth Analysis
- Determine the tightest bound for the function \( F(n) = \log(2n) + n + 100000000 \).
  - **Answer**: \( O(n) \)

#### Q3: Complexity of Functions
- Analyze functions \( F(n) \), \( G(n) \), and \( H(n) \) for their time complexity.
  - **F(n)**: \( O(n \log n) \)
  - **G(n)**: \( O(n) \)
  - **H(n)**: \( O(n \log \log n) \)

### 4. Hands-on Lab
- Engage with a selected Kattis/LeetCode problem involving List ADT.
- Encourage collaborative problem-solving and peer assistance.

## Implementation/Examples
```cpp
// Example of a simple List ADT implementation in C++
template <typename T>
class ListArray {
    T arr[100]; // Fixed-size array
    int size;
public:
    void add(T value) {
        // Implementation of add method
    }
    // Other methods...
};
```

> [!note] **Important**: Always clarify doubts with your TA during the tutorial sessions to enhance understanding.
> [!warning] **Caution**: Avoid relying solely on Gen AI tools for answers; ensure you attempt the problems independently first.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[adc_handout_student]]
- [[Logic - Propositional Logic]]
- [[Midterm+Briefing]]
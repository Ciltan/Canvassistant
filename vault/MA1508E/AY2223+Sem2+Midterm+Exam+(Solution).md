---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Midterm Test Overview

## Overview
This note summarizes the key components of the MA1508E Midterm Test for AY2022/2023 Semester 2, focusing on linear algebra concepts and problem-solving techniques. The exam consists of five questions covering various topics, including linear systems, matrix operations, and determinants. Students are required to demonstrate their understanding through detailed workings and solutions.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables. [[Logic - Propositional Logic]]
- **Unique Solution**: A situation where a linear system has exactly one solution. [[Determinants]]
- **Infinitely Many Solutions**: Occurs when a linear system has more than one solution, often parameterized by one or more variables. [[Stacks and Queues]]
- **Elementary Row Operations**: Operations used to manipulate matrices to solve linear systems. [[Matlab+for+Engineering]]
- **Determinant**: A scalar value that can be computed from the elements of a square matrix, providing important properties of the matrix. [[Determinants]]

## Detailed Technical Breakdown

### Instructions to Students
- Write your name, student number, and tutorial group.
- The exam consists of 5 questions and is worth 50 marks.
- It is a closed book assessment; one A4 handwritten help sheet is allowed.
- Non-programmable calculators are permitted, but all workings must be shown.
- All questions must be answered.

### Question Breakdown
1. **Linear System Analysis** (12 points)
   - Analyze the given linear system for values of \(a\) and \(b\) that yield:
     - No solution
     - Unique solution
     - Infinitely many solutions (one parameter)
     - Infinitely many solutions (two parameters)

   **Elementary Row Operations**:
   - Use row operations to manipulate the augmented matrix and derive solutions.

2. **Matrix Equation** (4 points)
   - Solve the equation \(Ax = b\) for a given matrix \(A\) and vector \(b\).

3. **Elementary Matrices** (10 points)
   - Identify matrices \(A\) and \(B\) and find elementary matrices that relate them.

4. **Determinants** (10 points)
   - Calculate the determinant of a given matrix \(A\) and analyze conditions for non-trivial solutions.

5. **Vector Spaces** (10 points)
   - Determine which vectors belong to the span of a given set and express the span as a solution set to a linear system.

## Implementation/Examples

### Example of Row Operations
```plaintext
1. Start with the augmented matrix:
   [1 a b a-b | 1]
   [0 1 b a-b | 2]
   [-1 -a 0 0 | -1]
   [0 0 b a-b | 0]

2. Apply row operations to simplify:
   R2 - R1 → R2
   R4 - R1 → R4
```

### Example of Determinant Calculation
```plaintext
det(A) = a((a+5) + 6 - 2(a+5)) + a(2(a+5) - 3 - 1 + (a+5))
```

> [!note] Ensure to show all workings clearly in your answers to receive full credit.
> [!important] Remember that the exam is closed book; rely on your understanding and the help sheet you prepare.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[MA1508E+AY2122Sem1]]
- [[Tutorial+1+Solution]]
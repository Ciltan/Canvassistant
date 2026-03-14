---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 1 - Homework 1

## Overview
This document outlines the requirements and tasks for Homework 1 in the MA1508E course at the National University of Singapore. It includes instructions for submission, a linear system problem, and matrix equations. The homework consists of three main questions, focusing on the conditions for solutions of linear systems and matrix operations.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Matrix Equation**: An equation in which the variables are represented in matrix form, typically expressed as \(Ax = b\).
- **Elementary Row Operations**: Operations used to manipulate the rows of a matrix to solve linear systems.
- **Consistent System**: A system of equations that has at least one solution.
- **Unique Solution**: A system that has exactly one solution.
- **Infinitely Many Solutions**: A system that has more than one solution, often expressed with parameters.

## Detailed Technical Breakdown

### Submission Instructions
- Write answers on A4 size papers.
- Clearly write your student number and name on the top left corner of each page.
- Include page numbers on the top right corner of each page.
- Submit by scanning or photographing your work, merging images into one PDF named as StudentNo P1 (e.g., A123456Z P1).
- Upload the PDF to the LumiNUS folder for Practice 1 submission.

### Question Breakdown

#### Question 1: Linear System Analysis
1. **Given System**:
   - \(x_1 + (a-1)x_2 + x_3 + x_4 = a + 1\)
   - \((a-2)x_2 + (a+2)x_3 + 2x_4 = a + 1\)
   - \((a-2)x_2 + x_3 + x_4 = a\)
   - \(x_1 + x_2 + (a+2)x_3 + 2x_4 = a + 2\)

   - **Tasks**:
     - (i) Determine conditions on \(a\) for no solution.
     - (ii) Determine conditions on \(a\) for a unique solution and provide the solution.
     - (iii) Determine conditions on \(a\) for infinitely many solutions with one parameter and provide a general solution.
     - (iv) Determine conditions on \(a\) for infinitely many solutions with two parameters and provide a general solution.
   - **Note**: Clearly write down the elementary row operations used.

#### Question 2: Matrix Equation
1. **Given System**:
   - \(x_1 + x_2 + x_3 = 0\)
   - \(2x_2 - 2x_3 = -1\)
   - \(2x_2 - 2x_3 = 1\)
   - \(x_2 - 2x_3 = 1\)
   - \(-x_1 - x_2 - 2x_3 = 1\)

   - **Tasks**:
     - (i) Write the corresponding matrix equation \(Ax = b\) and check for consistency.
     - (ii) Compute \(A^TA\) and \(A^Tb\) and find a solution for \(A^TAx = A^Tb\).
   - (b) Write down a linear system that has the following general solution:
     - \(x_1 = 1 - s - t\)
     - \(x_2 = -2 - s + 2t\)
     - \(x_3 = s\)
     - \(x_4 = t\)

#### Question 3: Matrix Commutativity
1. **Given Matrix**:
   - Let \(A = \begin{pmatrix} 1 & -2 \\ 2 & -1 \end{pmatrix}\).
   - Find all matrices \(B = \begin{pmatrix} c & d \\ a & b \end{pmatrix}\) such that \(AB = BA\).

## Implementation/Examples
```plaintext
# Example of a matrix equation
A = [[1, -2], [2, -1]]
b = [0, -1]
```

> [!note] Ensure all images are clear and in order before merging into a PDF for submission.
> [!important] Pay attention to the conditions for solutions as they are critical for understanding linear systems.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]
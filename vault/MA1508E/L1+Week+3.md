---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Week 3 Lecture Notes

## Overview
This lecture focuses on solving linear systems using [[Gaussian Elimination]] and [[Gauss-Jordan Elimination]]. Key concepts include the formulation of associated homogeneous systems and the identification of unique, infinite, or no solutions. The lecture also discusses practical applications of linear algebra in various contexts, including traffic flow and chemical equations.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Gaussian Elimination**: A method for solving linear systems by transforming the system into an upper triangular form.
- **Gauss-Jordan Elimination**: An extension of Gaussian elimination that reduces the matrix to reduced row echelon form (RREF).
- **Homogeneous System**: A linear system where all constant terms are zero.
- **Unique Solution**: A scenario where a linear system has exactly one solution.
- **Infinite Solutions**: Occurs when there are free variables in the system, leading to multiple solutions.
- **No Solution**: A situation where the equations contradict each other.

## Detailed Technical Breakdown

### Announcements
- **Quizzes**: Attempt quizzes 1.5 to 2.2 by January 30, 2026.
- **Consultation**: Drop-in consultation sessions available on the Canvas page.
- **Homework**: Homework 1 has been published.

### Problem Breakdown

#### Question 1: Solve the Linear Systems
1. **System**:
   \[
   \begin{align*}
   3x_1 + 2x_2 - 4x_3 &= 3 \\
   2x_1 + 3x_2 + 3x_3 &= 15 \\
   5x_1 - 3x_2 + x_3 &= 14
   \end{align*}
   \]
   - **Gaussian Elimination Steps**:
     - Transform to RREF.
     - Identify unique solution: \(x_1 = 3, x_2 = 1, x_3 = 2\).

2. **Associated Homogeneous System**:
   \[
   \begin{align*}
   3x_1 + 2x_2 - 4x_3 &= 0 \\
   2x_1 + 3x_2 + 3x_3 &= 0 \\
   5x_1 - 3x_2 + x_3 &= 0
   \end{align*}
   \]
   - Result: Only trivial solution exists.

#### Question 2: Matrix Reduction
- **Matrix**:
  \[
  \begin{pmatrix}
  2 & 6 & 5 & 0 \\
  1 & 0 & 4 & 0 \\
  1 & 4 & 5 & 0
  \end{pmatrix}
  \]
- **Operations**: Reduce to RREF using Gaussian and Gauss-Jordan elimination.

#### Question 3: Parameter Analysis
- **System**:
  \[
  \begin{align*}
  ax + bz &= 2 \\
  ax + ay + 4z &= 4 \\
  ay + 2z &= b
  \end{align*}
  \]
- **Conditions**:
  - (a) No solution: \(a = 0, b \neq 2\)
  - (b) Unique solution: \(a \neq 0, b \neq 2\)
  - (c) Infinitely many solutions with one parameter: \(a \neq 0, b = 2\)
  - (d) Infinitely many solutions with two parameters: \(a = 0, b = 2\)

#### Question 4: Chemical Equations
- **Example**: Combustion of methane represented by a balanced equation.
- **Homogeneous System**:
  \[
  \begin{align*}
  x_1 - x_3 &= 0 \\
  4x_1 - 2x_4 &= 0 \\
  2x_2 - 2x_3 - x_4 &= 0
  \end{align*}
  \]
- **General Solution**: Infinitely many solutions.

## Implementation/Examples
```plaintext
# Example of Gaussian Elimination Steps
1. Start with the augmented matrix.
2. Perform row operations to achieve RREF.
3. Identify solutions based on the final matrix form.
```

> [!note] **Important**: Always check for consistency in the system before concluding the type of solution.
> [!warning] **Caution**: Misapplication of elimination methods can lead to incorrect solutions.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Matlab+for+Engineering]]
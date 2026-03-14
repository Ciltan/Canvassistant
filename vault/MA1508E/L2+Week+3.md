---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - L2 Week 3 Live Lecture

## Overview
This lecture focuses on solving linear systems using [[Gaussian Elimination]] and [[Gauss-Jordan Elimination]]. Students are introduced to the concepts of homogeneous systems and their solutions, as well as practical applications in engineering contexts. The session also includes a discussion on the implications of system consistency and the relationship between parameters and solutions.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Gaussian Elimination**: A method for solving linear systems by transforming the system into an upper triangular form.
- **Gauss-Jordan Elimination**: An extension of Gaussian elimination that reduces the system to reduced row echelon form (RREF).
- **Homogeneous System**: A linear system in which all of the constant terms are zero.
- **Unique Solution**: A solution to a linear system where there is exactly one set of values for the variables.
- **Inconsistent System**: A system of equations that has no solution.

## Detailed Technical Breakdown

### Announcements
- Attempt quizzes 1.5 to 2.2 by January 30, 2026.
- Consultation sessions available on the Canvas page.
- Homework 1 has been published.

### Problem Breakdown

#### Question 1: Solve Linear Systems
1. **System of Equations**:
   - \(3x_1 + 2x_2 - 4x_3 = 3\)
   - \(2x_1 + 3x_2 + 3x_3 = 15\)
   - \(5x_1 - 3x_2 + x_3 = 14\)

   **Solution Steps**:
   - Apply [[Gaussian Elimination]] or [[Gauss-Jordan Elimination]].
   - Identify the associated homogeneous system:
     - \(3x_1 + 2x_2 - 4x_3 = 0\)
     - \(2x_1 + 3x_2 + 3x_3 = 0\)
     - \(5x_1 - 3x_2 + x_3 = 0\)

   **Results**:
   - Unique solution: \(x_1 = 3, x_2 = 1, x_3 = 2\).
   - Homogeneous system has only the trivial solution.

#### Question 2: Matrix Reduction
- Reduce the matrix:
  \[
  \begin{pmatrix}
  2 & 6 & 5 & 0 \\
  1 & 0 & 4 & 0 \\
  1 & 4 & 5 & 0
  \end{pmatrix}
  \]
- Discuss the efficiency of operations in Gaussian vs. Gauss-Jordan elimination.

#### Question 3: Parameter Analysis
- Determine values of \(a\) and \(b\) for different solution types:
  - No solution: \(a = 0, b \neq 2\)
  - Unique solution: \(a \neq 0, b \neq 2\)
  - Infinitely many solutions with one parameter: \(a \neq 0, b = 2\)
  - Infinitely many solutions with two parameters: \(a = 0, b = 2\)

#### Question 4: Chemical Equations
- Balance chemical equations using linear systems.
- Example: Methane combustion represented as:
  \[
  CH_4 + 2O_2 \rightarrow CO_2 + 2H_2O
  \]

#### Question 5: Traffic Flow Model
- Analyze a network of streets using a system of equations.
- Discuss the implications of junction closures on traffic flow.

#### Question 6: Temperature Distribution
- Model temperature distribution on a plate using linear equations.
- Solve the system and discuss the uniqueness of the solution.

## Implementation/Examples
```markdown
# Example of Gaussian Elimination
1. Start with the augmented matrix.
2. Perform row operations to achieve RREF.
3. Interpret the results to find solutions.
```

> [!note] **Important**: Always check for consistency in your linear systems. An inconsistent system will yield no solutions.
> [!warning] **Caution**: Be mindful of the parameters when determining the nature of solutions in linear systems.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
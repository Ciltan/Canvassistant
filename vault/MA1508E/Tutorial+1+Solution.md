---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 1 Solutions

## Overview
This note provides a comprehensive breakdown of the solutions to Tutorial 1 for the MA1508E course at the National University of Singapore. It covers the application of [[Gaussian Elimination]] and [[Gauss-Jordan Elimination]] to solve linear systems, the formulation of associated homogeneous systems, and the exploration of unique and infinite solutions. Additionally, it includes applications of linear algebra in chemical equations and traffic flow analysis.

## Key Concepts & Definitions
- **Gaussian Elimination**: A method for solving linear systems by transforming the system's augmented matrix into row echelon form.
- **Gauss-Jordan Elimination**: An extension of Gaussian elimination that reduces the matrix to reduced row echelon form.
- **Homogeneous System**: A system of linear equations where all constant terms are zero.
- **Unique Solution**: A scenario where a linear system has exactly one solution.
- **Infinite Solutions**: Occurs when a linear system has more than one solution, typically due to free variables.

## Detailed Technical Breakdown

### Problem 1: Solving Linear Systems
1. **System (a)**:
   - Given:
     \[
     \begin{align*}
     3x_1 + 2x_2 - 4x_3 &= 3 \\
     2x_1 + 3x_2 + 3x_3 &= 15 \\
     5x_1 - 3x_2 + x_3 &= 14
     \end{align*}
     \]
   - **Solution**:
     - Unique solution: \( x_1 = 3, x_2 = 1, x_3 = 2 \)
     - Associated homogeneous system:
     \[
     \begin{align*}
     3x_1 + 2x_2 - 4x_3 &= 0 \\
     2x_1 + 3x_2 + 3x_3 &= 0 \\
     5x_1 - 3x_2 + x_3 &= 0
     \end{align*}
     \]
     - Trivial solution only.

2. **System (b)**:
   - Given:
     \[
     \begin{align*}
     a + b - c - 2d &= 0 \\
     2a + b - c + d &= -2 \\
     -a + b - 3c + d &= 4
     \end{align*}
     \]
   - **Solution**:
     - General solution: \( a = -2 - 3s, b = 2 + 19s, c = 9s, d = s \), \( s \in \mathbb{R} \)
     - Associated homogeneous system yields a similar form.

3. **System (c)**:
   - Given:
     \[
     \begin{align*}
     x - 4y + 2z &= -2 \\
     x + 2y - 2z &= -3 \\
     x - y &= 4
     \end{align*}
     \]
   - **Solution**:
     - Inconsistent system.

### Problem 2: Matrix Reduction
- Given matrix:
\[
\begin{pmatrix}
2 & 6 & 5 & 0 \\
1 & 0 & 4 & 0 \\
1 & 4 & 5 & 0
\end{pmatrix}
\]
- **Solution**:
  - Reduced row echelon form achieved through Gaussian elimination.

### Problem 3: Parameter Analysis
- Determine values of \( a \) and \( b \) for various solution types:
  - (a) No solution: \( a = 0, b \neq 2 \)
  - (b) Unique solution: \( a \neq 0, b \neq 2 \)
  - (c) Infinitely many solutions with one parameter: \( a \neq 0, b = 2 \)
  - (d) Infinitely many solutions with two parameters: \( a = 0, b = 2 \)

### Problem 4: Chemical Reactions
- Balancing chemical equations using linear systems derived from reaction coefficients.

### Problem 5: Traffic Flow Analysis
- Analyzing a network of streets using linear equations to determine traffic volumes.

## Implementation/Examples
```matlab
% Example MATLAB code for solving a linear system
A = [4 -1 -1 0; -1 4 0 -1; -1 0 4 -1; 0 -1 -1 4];
b = [160; 140; 60; 40];
x = rref([A b]);
```

> [!note] **Important**: Ensure to practice Gaussian and Gauss-Jordan elimination manually to solidify understanding before relying on MATLAB.
> [!warning] **Caution**: Be aware of the conditions under which systems may become inconsistent or yield infinite solutions.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
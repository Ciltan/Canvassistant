---
tags: [MA1508E, lecture-notes, academic]
---

# Chapter 1: Linear Systems

## Overview
This chapter introduces the fundamental concepts of [[Linear Systems]], focusing on the definition, solutions, and classifications of linear equations. It explores the structure of linear systems, including homogeneous and inconsistent systems, and provides methods for solving them. The chapter also emphasizes the importance of visualizing linear systems in both two and three dimensions.

## Key Concepts & Definitions
- **Linear Equation**: A linear equation with n variables in standard form is expressed as \( a_1x_1 + a_2x_2 + \ldots + a_nx_n = b \). Here, \( a_1, a_2, \ldots, a_n \) are known constants (coefficients), and \( b \) is the constant term.
- **Homogeneous Linear Equation**: A linear equation is homogeneous if \( b = 0 \).
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Consistent System**: A linear system that has at least one solution.
- **Inconsistent System**: A linear system that has no solutions.
- **General Solution**: The solution that captures all possible solutions of a linear system, often expressed in terms of parameters.

## Detailed Technical Breakdown

### 1. Introduction to Linear Systems
- Example of a linear system:
  - \( \begin{cases} x + y = 2 \\ x - y = 0 \end{cases} \)
  - Solution: \( x = 1, y = 1 \)
- Geometric interpretation: The solution represents the intersection of two lines.

### 2. Definitions
- **Linear Equation**: 
  - Standard form: \( a_1x_1 + a_2x_2 + \ldots + a_nx_n = b \)
  - Homogeneous: \( a_1x_1 + a_2x_2 + \ldots + a_nx_n = 0 \)

- **Linear System**:
  - General form for \( m \) equations and \( n \) variables:
  \[
  \begin{cases}
  a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n = b_1 \\
  a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n = b_2 \\
  \vdots \\
  a_{m1}x_1 + a_{m2}x_2 + \ldots + a_{mn}x_n = b_m
  \end{cases}
  \]

### 3. Solutions to a Linear System
- A solution \( (x_1, x_2, \ldots, x_n) \) satisfies all equations simultaneously.
- Example:
  - Given \( \begin{cases} x + 2y = 5 \\ 2x + 4y = 10 \end{cases} \)
  - General solution: \( x = 5 - 2s, y = s, s \in \mathbb{R} \)

### 4. Inconsistent Linear Systems
- A system is inconsistent if it has no solutions.
- Example:
  - \( \begin{cases} x + y = 2 \\ x - y = 0 \\ 2x + y = 1 \end{cases} \)
  - No solution exists.

### 5. Visualizing Linear Systems
- **2 Variables**: 
  - Three cases: parallel lines (no solution), intersecting lines (unique solution), coinciding lines (infinitely many solutions).
- **3 Variables**: 
  - Intersecting planes can yield unique solutions, no solutions, or infinitely many solutions.

## Implementation/Examples
```markdown
### Example of Augmented Matrix
For the linear system:
\[
\begin{cases}
3x + 2y - z = 1 \\
5y + z = 3 \\
x + z = 2
\end{cases}
\]
The augmented matrix is:
\[
\begin{pmatrix}
3 & 2 & -1 & | & 1 \\
0 & 5 & 1 & | & 3 \\
1 & 0 & 1 & | & 2
\end{pmatrix}
\]
```

> [!note] **Important Concepts**: Understanding the difference between consistent and inconsistent systems is crucial for solving linear equations effectively.

> [!warning] **Caution**: Avoid using variables as parameters in the general solution to prevent circular reasoning.

## Related
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Stacks and Queues]]
- [[Chapter+2]]: Further exploration of linear algebra concepts.
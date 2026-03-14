---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E - Linear Algebra for Engineering: Midterm Make-up Test Overview

## Overview
This note summarizes the key concepts and solutions from the MA1508E Midterm Make-up Test for AY2022/2023 Semester 2. The test consists of three questions focusing on linear systems, matrix operations, and vector spaces. It emphasizes understanding the conditions for unique, infinite, and no solutions in linear systems, as well as the properties of matrices and their null spaces.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Unique Solution**: A situation where a linear system has exactly one solution.
- **Infinitely Many Solutions**: Occurs when a linear system has more than one solution, often parameterized by one or more variables.
- **Elementary Row Operations**: Operations used to manipulate matrices to solve linear systems.
- **Rank-Nullity Theorem**: A fundamental theorem in linear algebra that relates the rank and nullity of a matrix.

## Detailed Technical Breakdown

### Question 1: Analyzing a Linear System
1. **System Definition**:
   - Given a linear system with parameters \( a \):
     \[
     \begin{align*}
     x_1 + x_2 + x_3 &= 1 \\
     x_1 + ax_2 + a^2x_3 &= 1 \\
     ax_1 + ax_2 + a^3x_3 &= a^2 + a^{-1}
     \end{align*}
     \]

2. **Conditions for Solutions**:
   - **No Solution**: Occurs when \( a = 0 \).
   - **Unique Solution**: Exists when \( a \neq -1, 0, 1 \).
   - **Infinitely Many Solutions**:
     - One parameter: \( a = -1 \) with general solution \( x_1 = 1 - s, x_2 = 0, x_3 = s \).
     - Two parameters: \( a = 1 \) with general solution \( x_1 = 1 - s - t, x_2 = s, x_3 = t \).

### Question 2: Matrix and Basis
1. **Matrix Construction**:
   - Find a \( 2 \times 4 \) matrix \( A \) such that \( Ax = b \) has a general solution.
   - Example matrix:
     \[
     A = \begin{pmatrix}
     1 & -2 & -1 & 1 \\
     2 & -4 & -2 & 2
     \end{pmatrix}
     \]

2. **Basis Verification**:
   - Show that set \( T = \{v_1, v_2, v_3\} \) is a basis for \( V \) by demonstrating linear independence and spanning.

### Question 3: Matrix Properties
1. **Singularity Conditions**:
   - Matrix \( A \) is singular if \( a = -1, 0, 2 \).
   - Use elementary row operations to determine singularity.

2. **Finding \( b \) and \( c \)**:
   - For \( a = 2 \), find \( b = -2 \) and \( c = 0 \) such that the system has a nontrivial solution.

3. **Rank and Nullity**:
   - Rank of \( A \) is 3, and nullity is 1, indicating a unique solution structure.

## Implementation/Examples
```plaintext
1. Row operations to find conditions for solutions:
   R2 - R1, R3 - R1, etc.
2. Matrix example:
   A = [[1, -2, -1, 1], [2, -4, -2, 2]]
```

> [!note] **Important**: Always show your workings clearly when solving linear systems to ensure full credit.
> [!warning] **Caution**: Be mindful of the conditions under which a linear system may have no solutions or infinitely many solutions.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Rank-Nullity Theorem]]
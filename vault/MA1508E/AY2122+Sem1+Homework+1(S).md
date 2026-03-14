---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 1 - Solutions Overview

## Overview
This note summarizes the solutions to various problems related to linear algebra concepts, specifically focusing on augmented matrices and their implications on the existence and uniqueness of solutions. The problems explore conditions under which systems of equations have no solution, a unique solution, or infinitely many solutions, along with matrix operations and their applications in solving linear systems.

## Key Concepts & Definitions
- **Augmented Matrix**: A matrix that includes the coefficients of the variables and the constants from the equations.
- **Elementary Row Operations**: Operations used to manipulate rows of a matrix to achieve row echelon form or reduced row echelon form.
- **Unique Solution**: A scenario where a system of equations has exactly one solution.
- **Infinitely Many Solutions**: A situation where there are multiple solutions to a system of equations, often represented with parameters.
- **Inconsistent System**: A system of equations that has no solution.

## Detailed Technical Breakdown

### Problem 1: Augmented Matrix Analysis
1. **Given Augmented Matrix**:
   \[
   \begin{pmatrix}
   1 & a & 2-a & 0 \\
   1 & a & a+2 & 2a
   \end{pmatrix}
   \]

2. **Conditions for Solutions**:
   - **No Solution**: Occurs when \( a = 1 \).
     - Resulting matrix: 
     \[
     \begin{pmatrix}
     0 & 0 & 0 & 1 \\
     0 & 0 & 2 & 2
     \end{pmatrix}
     \]
   - **Unique Solution**: Occurs when \( a \neq 1 \) and \( a \neq 0 \).
     - Unique solution:
     \[
     x_1 = \frac{a}{a-1}, \quad x_2 = \frac{2-2a}{a-1}, \quad x_3 = 1
     \]
   - **Infinitely Many Solutions**: Occurs when \( a = 0 \).
     - General solution:
     \[
     x_1 = -2s, \quad x_2 = s, \quad x_3 = s, \quad s \in \mathbb{R}
     \]
     - Particular solution: \( x_1 = -2, x_2 = 1, x_3 = 1 \).

### Problem 2: Linear System Consistency
1. **Linear System**:
   \[
   \begin{align*}
   x_1 - x_2 + x_3 &= -1 \\
   2x_1 - x_2 - x_3 &= 1 \\
   x_2 + 2x_3 &= 1 \\
   x_1 + 2x_2 &= 1 \\
   x_1 + x_3 &= 1
   \end{align*}
   \]

2. **Matrix Equation**:
   \[
   Ax = b
   \]
   - The system is inconsistent after reduction.

3. **Matrix Calculations**:
   - Compute \( A^TA \) and \( A^Tb \):
   \[
   A^TA = \begin{pmatrix}
   1 & -1 & 1 \\
   2 & -1 & -1 \\
   0 & 1 & 2 \\
   1 & 2 & 0 \\
   1 & 0 & 1
   \end{pmatrix}
   \]
   - Solution for \( A^TAx = A^Tb \):
   \[
   x = \begin{pmatrix}
   1 \\
   0
   \end{pmatrix}
   \]

### Problem 3: Commutative Matrices
1. **Matrix A**:
   \[
   A = \begin{pmatrix}
   2 & 1 \\
   2a-c & 2b-d
   \end{pmatrix}
   \]

2. **Conditions for Commutativity**:
   - The conditions derived from \( AB = BA \) yield:
     - \( 2b + c = 0 \)
     - \( a + b - d = 0 \)
   - General solution:
   \[
   a = s + t, \quad b = -s, \quad c = s, \quad d = t, \quad s, t \in \mathbb{R}
   \]

## Implementation/Examples
```plaintext
# Example of an augmented matrix operation
1  a  2-a  0
1  a  a+2  2a
```

> [!note] **Key Takeaway**: Understanding the conditions for the existence of solutions in linear systems is crucial for solving real-world engineering problems.
> 
> [!important] **Reminder**: Always check for consistency in systems of equations before attempting to find solutions.

## Related
- [[AY2122+Sem1+Homework+1(S)]]
- [[AY2122+Sem1+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Logic - Propositional Logic]]
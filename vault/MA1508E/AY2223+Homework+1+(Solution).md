---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 1 Solutions

## Overview
This note provides a structured summary of the solutions to Homework 1 for the MA1508E course at the National University of Singapore. It covers the consistency of linear systems, matrix equations, and determinants, along with the conditions for unique and infinite solutions. The solutions are presented with clear explanations and relevant mathematical operations.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Matrix Equation**: An equation in which the unknowns are represented by matrices.
- **Determinant**: A scalar value that is a function of the entries of a square matrix and provides important properties of the matrix, such as invertibility.
- **Row Reduction**: A method used to simplify matrices to solve systems of equations.

## Detailed Technical Breakdown

### Problem 1: Consistency of Linear System
1. **Given System**:
   \[
   \begin{align*}
   x - y + 2z &= 1 \\
   x + y + 2z &= 0 \\
   2x + y &= 1 \\
   y + z &= -1
   \end{align*}
   \]
2. **Solution**: The system is inconsistent as shown by the row reduction leading to a contradiction.

### Problem 2: Matrix Equation \( Ax = b \)
1. **Matrix Form**:
   \[
   A^TAx = A^Tb
   \]
2. **Solution**: The unique solution is derived from the matrix operations leading to:
   \[
   \begin{align*}
   x &= \frac{5}{21} \\
   y &= -\frac{13}{21} \\
   z &= -\frac{4}{21}
   \end{align*}
   \]

### Problem 3: Conditions for Solutions
1. **System**:
   \[
   \begin{align*}
   x + y - z &= 0 \\
   (a+1)y + z &= -1 \\
   -x - (a+2)y + (b-a)z &= 2 \\
   x - ay - 2z &= 1
   \end{align*}
   \]
2. **Cases**:
   - **No Solution**: If \( b = a \) or \( a = -1 \) and \( b \neq -2 \).
   - **Unique Solution**: If \( a \neq -1 \) and \( b \neq a \).
   - **Infinitely Many Solutions**: If \( a = -1 \) and \( b = -2 \).

### Problem 4: Determinant of Matrix \( A \)
1. **Matrix**:
   \[
   A = \begin{pmatrix}
   1 & 1 & 1 & 1 \\
   1 & a & 1 & 1 \\
   1 & a & 2 & 3 \\
   1 & 1 & 1 & -a
   \end{pmatrix}
   \]
2. **Determinant Calculation**:
   \[
   \text{det}(A) = 1 - a^2
   \]
3. **Invertibility Condition**: \( A \) is invertible if \( a \neq \pm 1 \).

## Implementation/Examples
```matlab
% MATLAB code for solving the matrix equation
A = [1 -1 2; 1 1 2; 2 1 0; 0 1 1];
b = [1; 0; 1; -1];
x = A\b; % Solving Ax = b
```

> [!note] **Important**: Always show workings clearly when using MATLAB for calculations.
> [!warning] **Caution**: Ensure that the PDF submission is named correctly as per guidelines.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Logic - Propositional Logic]]
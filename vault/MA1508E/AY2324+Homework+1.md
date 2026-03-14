---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 1

## Overview
This document outlines the requirements and problems for Homework 1 in the MA1508E course at the National University of Singapore. It includes instructions for submission, a series of linear algebra problems involving symmetric matrices, linear systems, and determinants. The homework emphasizes the importance of showing all workings and utilizing MATLAB for calculations.

## Key Concepts & Definitions
- **Symmetric Matrix**: A matrix that is equal to its transpose, denoted as \( B = B^T \).
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Elementary Row Operations**: Operations that can be performed on the rows of a matrix to simplify it, including row swapping, scaling, and row addition.
- **Determinant**: A scalar value that is a function of a square matrix, providing important properties about the matrix, such as whether it is invertible.

## Detailed Technical Breakdown

### Submission Instructions
- Write answers on A4 size paper or digitally.
- Include page numbers on the top right corner.
- Use MATLAB for calculations, showing all workings.
- Submit scanned images or a PDF file named as per the format: `StudentNo HW1.pdf`.

### Problems

1. **Symmetric Matrices**
   - Given matrix \( A = \begin{pmatrix} 1 & -1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & -1 \end{pmatrix} \), find all symmetric matrices \( B \) such that \( AB \) is symmetric.

2. **Linear System Analysis**
   - Consider the system:
     \[
     \begin{align*}
     x_1 + x_2 - bx_3 + (b-a)x_4 &= b-2 \\
     x_1 + ax_2 - bx_3 &= 1 \\
     2x_1 + 2x_2 + ax_4 &= 0 \\
     x_1 + x_2 - bx_3 &= 0
     \end{align*}
     \]
   - **(a)** Determine values of \( a \) and \( b \) for no solution.
   - **(b)** Determine values for one unique solution and provide the solution.
   - **(c)** Determine values for infinitely many solutions with one parameter and provide the general solution.
   - **(d)** Discuss the possibility of infinitely many solutions with two parameters.

3. **Matrix A and Elementary Matrices**
   - Given matrix \( A \):
     \[
     A = \begin{pmatrix} 1 & 0 & 2 \\ -2 & -2 & a \\ 0 & 0 & b \end{pmatrix}
     \]
   - **(a)** Find values of \( a \) and \( b \) such that \( A \) is singular.
   - **(b)** If \( R = I \) (identity matrix), express \( A \) as a product of elementary matrices.
   - **(c)** If \( \text{det}(A) = -20 \), find \( \text{det}(R) \).

4. **Homogeneous System**
   - For matrix \( A = \begin{pmatrix} \lambda-1 & -2 & 2 \\ -1 & \lambda-3 & 1 \\ -1 & -4 & \lambda+2 \end{pmatrix} \):
   - **(a)** Determine values of \( \lambda \) for infinitely many solutions of \( Ax = 0 \).
   - **(b)** For each \( \lambda \) found, provide the general solution for \( Ax = 0 \).

## Implementation/Examples
```matlab
% Example MATLAB code for solving a linear system
A = [1 -1 0; 0 1 1; 1 0 -1];
b = [b-2; 1; 0];
x = A\b; % Solving the system Ax = b
```

> [!note] **Important**: Ensure all workings are shown clearly, especially when using MATLAB for calculations.
> [!warning] **Caution**: Double-check the naming convention for your PDF submission to avoid any issues.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Elementary Row Operations]]
- [[Linear Systems]]
---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 1 Solutions

## Overview
This note summarizes the solutions to Homework 1 for the MA1508E course at the National University of Singapore. It covers the identification of symmetric matrices, the analysis of linear systems, and the conditions for singular matrices. The solutions are structured to provide clarity on the mathematical processes involved, including the use of [[MATLAB]] for calculations.

## Key Concepts & Definitions
- **Symmetric Matrix**: A matrix that is equal to its transpose, denoted as \( B = B^T \).
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Singular Matrix**: A square matrix that does not have an inverse, which occurs when its determinant is zero.
- **Elementary Row Operations**: Operations that can be performed on the rows of a matrix to simplify it, including row swapping, scaling, and row addition.

## Detailed Technical Breakdown

### Problem 1: Symmetric Matrices
1. **Given Matrix**: 
   \[
   A = \begin{pmatrix}
   1 & -1 & 0 \\
   0 & 1 & 1 \\
   1 & 0 & -1
   \end{pmatrix}
   \]
2. **Find Symmetric Matrices \( B \)**:
   - Let \( B = \begin{pmatrix}
   b_1 & b_2 & b_3 \\
   b_2 & b_4 & b_5 \\
   b_3 & b_5 & b_6
   \end{pmatrix} \)
   - Condition for symmetry: \( AB = B^T A^T \)
   - Resulting equations:
     - \( b_3 + b_4 = 0 \)
     - \( b_1 - 2b_2 + b_5 = 0 \)
     - \( b_2 - 2b_5 - b_6 = 0 \)

### Problem 2: Linear System Analysis
1. **System of Equations**:
   \[
   \begin{align*}
   x_1 + x_2 - bx_3 + (b-a)x_4 &= b-2 \\
   x_1 + ax_2 - bx_3 &= 1 \\
   2x_1 + 2x_2 + ax_4 &= 0 \\
   x_1 + x_2 - bx_3 &= 0
   \end{align*}
   \]
2. **Conditions**:
   - **No Solution**: \( a = 1 \) or \( b = 0 \) with \( a \neq 0 \) or \( b = a \neq 2 \).
   - **Unique Solution**: \( a \neq 1, b \neq 0, a \neq b \).
   - **Infinitely Many Solutions**: \( a = b = 2 \).

### Problem 3: Determinants and Singular Matrices
1. **Matrix**:
   \[
   A = \begin{pmatrix}
   1 & 0 & 2 \\
   0 & 2 & a \\
   0 & 0 & b
   \end{pmatrix}
   \]
2. **Singularity Condition**:
   - \( \text{det}(A) = 2b = 0 \) implies \( b = 0 \).

### Problem 4: Homogeneous Systems
1. **Matrix**:
   \[
   A = \begin{pmatrix}
   \lambda - 1 & -2 & 2 \\
   -1 & \lambda - 3 & 1 \\
   -1 & -4 & \lambda + 2
   \end{pmatrix}
   \]
2. **Infinitely Many Solutions**:
   - Occurs when \( \text{det}(A) = 0 \) leading to \( \lambda = -1, 1, 2 \).

## Implementation/Examples
```matlab
% MATLAB code for solving the linear system
A = [1 1 -b; 1 a -b; 2 2 0; 1 1 -b];
b_values = [0, 1, 2]; % Example values for b
for b = b_values
    % Perform row operations to find solutions
    RREF_A = rref(A);
    disp(RREF_A);
end
```

> [!note] **Important**: Always ensure to show all workings clearly when submitting homework.
> [!warning] **Caution**: When using MATLAB, verify that all matrices are correctly defined to avoid computational errors.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Linear Systems]]
- [[Symmetric Matrices]]
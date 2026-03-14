---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 1 Solutions

## Overview
This note summarizes the solutions to Homework 1 for the MA1508E course, focusing on matrix operations, row reduction, and system of equations. The tasks involve reducing matrices to row echelon form, determining invertibility conditions, and solving linear systems. Key concepts such as [[row operations]], [[invertible matrices]], and [[linear systems]] are explored in detail.

## Key Concepts & Definitions
- **Row Echelon Form**: A matrix is in row echelon form if all non-zero rows are above any rows of all zeros, and the leading coefficient of a non-zero row is always to the right of the leading coefficient of the previous row.
- **Reduced Row Echelon Form**: A matrix is in reduced row echelon form if it is in row echelon form and all leading coefficients are 1 and are the only non-zero entries in their columns.
- **Invertible Matrix**: A square matrix is invertible if there exists another matrix such that their product is the identity matrix.
- **Elementary Row Operations**: Operations that can be performed on rows of a matrix to achieve row echelon form, including row swapping, scaling, and adding multiples of one row to another.

## Detailed Technical Breakdown

### Problem 1: Matrix Reduction
1. **Matrix Definition**:
   \[
   A = \begin{pmatrix}
   2 & 2 & 3 & 2 \\
   2 & -1 & 0 & 0 \\
   0 & -1 & a-4 & 1 \\
   2 & 1 & 5-a & 2
   \end{pmatrix}
   \]

2. **Row Reduction Steps**:
   - Apply row operations to reduce \( A \) to row echelon form \( U \):
   \[
   U = \begin{pmatrix}
   2 & 2 & 3 & 2 \\
   0 & -3 & -3 & -2 \\
   0 & 0 & a-3 & 5/3 \\
   0 & 0 & 0 & 7/3
   \end{pmatrix}
   \]

3. **Elementary Row Operations**:
   - \( R_2 \leftarrow R_2 - R_1 \)
   - \( R_3 \leftarrow R_3 - \frac{1}{3}R_2 \)
   - \( R_4 \leftarrow R_4 - R_1 \)

> [!important] The sequence of operations must be clearly shown to receive full credit.

### Problem 2: Invertibility Conditions
- **Condition for Invertibility**: The matrix \( A \) is invertible if \( a \neq 3 \) since the determinant of \( U \) must be non-zero.

### Problem 3: Solving Linear Systems
1. **System Definition**:
   \[
   Py = b \quad \text{where} \quad b = \begin{pmatrix} 7 \\ 6-a \\ a+4 \end{pmatrix}
   \]

2. **Unique Solution**: The system has a unique solution when \( a \neq -2, 0, 1 \).

3. **General Solution**:
   - For \( a = 1 \), the system has infinitely many solutions:
   \[
   x_1 = \frac{14-s}{3}, \quad x_2 = s - 5, \quad x_3 = 5 - s, \quad x_4 = s, \quad s \in \mathbb{R}
   \]

## Implementation/Examples
```matlab
% MATLAB code for row reduction
A = [2 2 3 2; 2 -1 0 0; 0 -1 a-4 1; 2 1 5-a 2];
RREF_A = rref(A);
disp(RREF_A);
```

> [!note] Ensure to document all MATLAB commands used for calculations.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Linear Systems]]
- [[Matlab+for+Engineering]]
---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 3 Solutions

## Overview
This note provides a structured solution to Tutorial 3 of the MA1508E course, focusing on the application of [[Gaussian elimination]] to determine the invertibility of matrices and the computation of determinants. The tutorial also explores conditions for matrix invertibility and the implications of Cramer’s Rule in solving linear equations.

## Key Concepts & Definitions
- **Gaussian elimination**: A method for solving linear systems by transforming the matrix into row echelon form.
- **Invertible matrix**: A square matrix that has an inverse, meaning there exists another matrix such that their product is the identity matrix.
- **Determinant**: A scalar value that can be computed from the elements of a square matrix, providing insights into the matrix's properties, including invertibility.
- **Cramer’s Rule**: A theorem that provides an explicit formula for the solution of a system of linear equations with as many equations as unknowns, using determinants.

## Detailed Technical Breakdown

### 1. Invertibility of Matrices
#### (a) Matrix A
Given matrix:
\[
A = \begin{pmatrix}
-1 & 3 \\
3 & -2
\end{pmatrix}
\]
- **Gaussian elimination steps**:
  - Transform to row echelon form:
    - \( R_2 \leftarrow R_2 - 3R_1 \)
    - Resulting matrix:
    \[
    \begin{pmatrix}
    -1 & 3 \\
    0 & 1
    \end{pmatrix}
    \]
- **Conclusion**: The matrix is invertible, and its inverse is:
\[
A^{-1} = \frac{1}{7} \begin{pmatrix}
-2 & -3 \\
3 & -1
\end{pmatrix}
\]

#### (b) Matrix B
Given matrix:
\[
B = \begin{pmatrix}
-1 & 3 & -4 \\
2 & 4 & 1 \\
-4 & 2 & -9
\end{pmatrix}
\]
- **Gaussian elimination steps**:
  - Transform to row echelon form:
    - Resulting matrix:
    \[
    \begin{pmatrix}
    1 & 0 & 0 \\
    0 & 10 & -7 \\
    0 & 0 & 1
    \end{pmatrix}
    \]
- **Conclusion**: The matrix is not invertible.

### 2. Conditions for Invertibility
#### (a) Matrix with Variables
Given matrix:
\[
\begin{pmatrix}
1 & 1 & 1 \\
a & b & c \\
a^2 & b^2 & c^2
\end{pmatrix}
\]
- **Conditions for invertibility**:
  - The matrix is invertible if \( a \neq b \), \( b \neq c \), and \( c \neq a \).

#### (b) Vandermonde Matrix
- **Conclusion**: The conditions for the points \((x_1, y_1)\), \((x_2, y_2)\), \((x_3, y_3)\) to ensure a unique polynomial of degree 2 are that the x-coordinates must be distinct.

### 3. Solving Matrix Equations
#### (a) Solve \( AX = B \)
Given:
\[
A = \begin{pmatrix}
0 & 1 & 2 \\
1 & 3 & 2 \\
1 & 1 & 2
\end{pmatrix}, \quad B = \begin{pmatrix}
1 \\
0 \\
3
\end{pmatrix}
\]
- **Solution**:
\[
X = \begin{pmatrix}
1 \\
-2 \\
-13
\end{pmatrix}
\]

#### (b) Solve \( Ax = -1 \)
- **Conclusion**: The solution can be derived from the previous results.

### 4. Cramer’s Rule
#### (a) Determinants of Matrices
- **Determinants**:
  - \( \text{det}(A_1) = 8 \)
  - \( \text{det}(A_2) = -16 \)
  - \( \text{det}(A_3) = 6 \)
  - \( \text{det}(A_4) = -2 \)

#### (b) Solve \( Ax = b \)
- **Conclusion**: The unique solution can be derived using Cramer’s Rule.

### 5. Stochastic Matrices
#### (a) Examples
- **Invertible Stochastic Matrix**: Identity matrix \( I \).
- **Singular Stochastic Matrix**: A matrix where the sum of each column is 1 but is not invertible.

#### (b) Properties of Stochastic Matrices
- **Conclusion**: \( I - P \) is singular if \( P \) is a stochastic matrix.

## Implementation/Examples
```markdown
# Example of Gaussian elimination
A = [[-1, 3], [3, -2]]
# Perform row operations to find the inverse
```

> [!important] Remember that a matrix is invertible if its determinant is non-zero.
> [!note] The conditions for invertibility are crucial for solving linear systems effectively.

## Related
- [[MA1508E+AY2122Sem1]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Cramer’s Rule]]
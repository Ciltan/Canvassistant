---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 3

## Overview
This tutorial focuses on the application of [[Gaussian elimination]] to determine the invertibility of matrices and to find their inverses. It also explores the conditions for the invertibility of specific matrix forms, the use of [[Cramer’s Rule]], and the properties of [[stochastic matrices]]. The tutorial concludes with supplementary problems that apply determinants to compute areas of geometric shapes.

## Key Concepts & Definitions
- **Gaussian Elimination**: A method for solving linear systems by transforming the matrix into row echelon form.
- **Invertible Matrix**: A matrix that has an inverse, meaning there exists another matrix such that their product is the identity matrix.
- **Cramer’s Rule**: A theorem that provides an explicit formula for the solution of a system of linear equations with as many equations as unknowns, using determinants.
- **Stochastic Matrix**: A square matrix used to describe the transitions of a Markov chain, where each column sums to 1.

## Detailed Technical Breakdown

### 1. Gaussian Elimination
- **Task**: Determine if the following matrices are invertible and find their inverses if they are.
  - (a) 
    \[
    \begin{pmatrix}
    -1 & 3 \\
    3 & -2
    \end{pmatrix}
    \]
  - (b) 
    \[
    \begin{pmatrix}
    -1 & 3 & -4 \\
    2 & 4 & 1 \\
    -4 & 2 & -9
    \end{pmatrix}
    \]

### 2. Conditions for Invertibility
- **Matrix**: 
  \[
  \begin{pmatrix}
  1 & 1 & 1 \\
  a & b & c \\
  a^2 & b^2 & c^2
  \end{pmatrix}
  \]
- **Conditions**: The matrix is invertible if the points \((x_1, y_1)\), \((x_2, y_2)\), \((x_3, y_3)\) are distinct.

### 3. Solving Matrix Equations
- **Matrix Equation**: 
  \[
  \begin{pmatrix}
  0 & 1 & 2 \\
  1 & 3 & 2 \\
  2 & 1 & 1
  \end{pmatrix} X = 
  \begin{pmatrix}
  1 & 0 & 3 & 7
  \end{pmatrix}
  \]
- **Solution**: Use Gaussian elimination to find \(X\).

### 4. Cramer’s Rule
- **Determinants**:
  - (i) 
    \[
    A_1 = \begin{pmatrix}
    1 & 5 & 3 \\
    0 & 2 & -2 \\
    0 & 1 & 3
    \end{pmatrix}
    \]
  - (ii) 
    \[
    A_2 = \begin{pmatrix}
    1 & 1 & 3 \\
    0 & 2 & -2 \\
    0 & 0 & 3
    \end{pmatrix}
    \]
  - (iii) 
    \[
    A_3 = \begin{pmatrix}
    1 & 5 & 1 \\
    0 & 2 & 2 \\
    0 & 1 & 0
    \end{pmatrix}
    \]
- **Unique Solution**: If \(A\) is invertible, the solution to \(Ax = b\) can be expressed using determinants.

### 5. Stochastic Matrices
- **Definition**: A matrix \(P\) is stochastic if the sum of each column is 1.
- **Example**: 
  \[
  P = \begin{pmatrix}
  0.2 & 0.8 & 0.4 \\
  0.3 & 0.2 & 0.4 \\
  0.5 & 0 & 0.2
  \end{pmatrix}
  \]
- **Homogeneous System**: Solve \((I - P)x = 0\).

## Implementation/Examples
```markdown
# Example of Gaussian Elimination
1. Start with the augmented matrix.
2. Apply row operations to achieve row echelon form.
3. Back substitute to find the inverse if applicable.
```

> [!important] **Note**: Ensure that the matrix is in reduced row echelon form to confirm invertibility.

> [!warning] **Caution**: If the determinant of a matrix is zero, the matrix is singular and does not have an inverse.

## Related
- [[Determinants]]
- [[Linear Algebra]]
- [[Matrix Theory]]
- [[Cramer’s Rule]]
- [[Stochastic Processes]]
---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 9

## Overview
This tutorial focuses on the application of linear algebra concepts, particularly in the context of MATLAB and least squares approximation. Key topics include finding the nullspace of a matrix, projecting vectors onto subspaces, and deriving least squares approximating lines and polynomials from given data points. The tutorial also explores eigenvalues and eigenvectors, emphasizing their properties and applications in various scenarios.

## Key Concepts & Definitions
- **Nullspace**: The set of all vectors that, when multiplied by a given matrix, yield the zero vector. [[Determinants]]
- **Projection**: The operation of projecting a vector onto a subspace, which can be computed using the formula \( P = N(N^TN)^{-1}N^T \) where \( N \) is a matrix whose columns form a basis for the subspace. [[Matlab+for+Engineering]]
- **Least Squares Approximation**: A method to find the best-fitting curve by minimizing the sum of the squares of the offsets (the residuals) of points from the curve. [[Logic - Propositional Logic]]
- **Eigenvalues and Eigenvectors**: For a square matrix \( A \), an eigenvalue \( \lambda \) is a scalar such that there exists a non-zero vector \( v \) (the eigenvector) satisfying \( Av = \lambda v \). [[Stacks and Queues]]

## Detailed Technical Breakdown

### 1. MATLAB and Nullspace
- **Problem Statement**: Given matrix \( A \):
  \[
  A = \begin{pmatrix}
  1 & 1 & 2 & 1 & 0 \\
  1 & 1 & 1 & 2 & 0 \\
  0 & 1 & 1 & 1 & 1
  \end{pmatrix}
  \]
  - **(a)** Find a basis \( S \) for the nullspace \( W \).
  - **(b)** Project standard basis vectors \( e_i \) onto \( W \).
  - **(c)** Project vector \( x \) onto \( W \):
  \[
  x = \begin{pmatrix}
  x_1 \\
  x_2 \\
  x_3 \\
  x_4 \\
  x_5
  \end{pmatrix}
  \]

### 2. Least Squares Approximation
- **Line Equation**: \( p(x) = a_0 + a_1 x \)
- **Objective**: Minimize the sum of squares:
  \[
  S = \sum_{i=1}^{m} (y_i - p(x_i))^2
  \]
- **Matrix Formulation**:
  \[
  N = \begin{pmatrix}
  1 & x_1 \\
  1 & x_2 \\
  \vdots & \vdots \\
  1 & x_m
  \end{pmatrix}, \quad a = \begin{pmatrix}
  a_0 \\
  a_1
  \end{pmatrix}
  \]
- **Minimization**: Solve \( ||y - Na||^2 \).

### 3. Eigenvalues and Eigenvectors
- **Eigenvalue Condition**: \( \lambda \) is an eigenvalue of \( A \) if \( \det(A - \lambda I) = 0 \).
- **Properties**:
  - If \( v \) is an eigenvector of \( A \) for \( \lambda \), then \( v \) is also an eigenvector of \( A^T \) for the same \( \lambda \).
  - If \( A \) is nilpotent, then \( 0 \) is the only eigenvalue.

### 4. QR Factorization
- **Gram-Schmidt Process**: Used to create an orthonormal basis from the columns of matrix \( A \).
- **Factorization**: \( A = QR \) where \( Q \) is orthonormal and \( R \) is upper triangular.

## Implementation/Examples
```matlab
% MATLAB code for least squares approximation
x = [4; 4.5; 5; 5.5; 6; 6.5; 7; 8; 8.5];
y = [0.8651; 0.4828; 2.590; -4.389; -7.858; 3.103; 7.456; 0.0965; 4.326];
N = fliplr(vander(x));
N = N(:, 1:5); % Up to the 4th power
a = (N' * N) \ (N' * y); % Least squares solution
```

> [!note] **Important**: Ensure that the matrix \( N \) has full rank for the least squares solution to be unique.
> [!warning] **Caution**: When interpreting eigenvalues, remember that they can indicate stability in systems; a positive eigenvalue may suggest instability.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+9]]
- [[CS1231+TUTORIAL+3]]
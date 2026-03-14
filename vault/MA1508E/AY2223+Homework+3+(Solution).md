---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 3 Solutions

## Overview
This document provides detailed solutions to Homework 3 for the MA1508E course at the National University of Singapore. It covers various topics in linear algebra, including eigenvalues, eigenvectors, projections, and polynomial fitting. The solutions are structured to enhance understanding and facilitate learning.

## Key Concepts & Definitions
- **Eigenvalues**: Scalars associated with a linear transformation that indicate how much the eigenvector is stretched or compressed.
- **Eigenvectors**: Non-zero vectors that change at most by a scalar factor when a linear transformation is applied.
- **Characteristic Polynomial**: A polynomial which is invariant under matrix similarity and whose roots are the eigenvalues of the matrix.
- **Projection**: The operation of projecting a vector onto a subspace.
- **Orthonormal Basis**: A basis where all vectors are orthogonal and of unit length.

## Detailed Technical Breakdown

### 1. Eigenvalues and Eigenvectors
- Let \( A \) be a symmetric matrix of order 3 with eigenvalues \( -1, 1, 2 \).
- The characteristic polynomial is given by:
  \[
  \text{char}(A) = (x + 1)(x - 1)(x - 2) = x^3 - 2x^2 - x + 2
  \]

### 2. Finding Eigenvectors
- For eigenvalue \( 2 \):
  - The eigenvector \( v_2 \) must satisfy the orthogonality condition with other eigenvectors.
  - The system of equations derived leads to:
    \[
    v_2 = s \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}, \quad s \in \mathbb{R}
    \]

### 3. Matrix Representation
- The matrix \( A \) can be expressed in the form \( A = PDP^T \) where \( P \) is an orthogonal matrix and \( D \) is a diagonal matrix.

### 4. Projection onto a Subspace
- Given vectors \( u_1, u_2, u_3 \), the projection \( u_p \) of \( u \) into the span of these vectors is computed using:
  \[
  u_p = A(ATA)^{-1}ATu
  \]

### 5. Polynomial Fitting
- For the data set \( (x, y) \):
  - Degree 2 polynomial fitting shows inconsistency.
  - Degree 3 polynomial fitting yields:
    \[
    p(x) = x^3 - 3x^2 - 4x + 12
    \]

## Implementation/Examples

### Characteristic Polynomial Calculation
```matlab
syms x
char_poly = (x + 1)*(x - 1)*(x - 2);
expand(char_poly)
```

### Eigenvector Calculation
```matlab
A = [1 2 -1; -1 3 0; -5 6 4];
[v, d] = eig(A);
```

### Projection Calculation
```matlab
u = [1; 1; 1];
A = [1 2 1; 0 1 0; -2 0 2];
u_p = A * (A' * A) \ (A' * u);
```

> [!note] Ensure all workings are clearly shown when submitting homework.
> [!important] Use MATLAB for calculations but document all steps in your submission.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Stacks and Queues]]
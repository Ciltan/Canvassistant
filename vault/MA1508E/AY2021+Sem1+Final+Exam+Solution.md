---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E AY2021 Sem 1 Final Exam Solutions

## Overview
This note provides a structured breakdown of the solutions to the final exam questions for MA1508E, focusing on linear algebra concepts such as column space, row space, nullspace, and projections. The solutions illustrate the application of reduced row-echelon form (RREF) and the properties of matrices, including determinants and eigenvalues. Each section is designed to clarify the underlying mathematical principles and provide examples for better understanding.

## Key Concepts & Definitions
- **Column Space**: The set of all possible linear combinations of the column vectors of a matrix. [[Column Space]]
- **Row Space**: The set of all possible linear combinations of the row vectors of a matrix. [[Row Space]]
- **Nullspace**: The set of all vectors that, when multiplied by the matrix, yield the zero vector. [[Nullspace]]
- **Reduced Row-Echelon Form (RREF)**: A form of a matrix that simplifies solving linear equations. [[RREF]]
- **Projection**: The process of mapping a vector onto a subspace. [[Projection]]
- **Eigenvector**: A non-zero vector that changes by only a scalar factor when a linear transformation is applied. [[Eigenvector]]
- **Determinant**: A scalar value that can be computed from the elements of a square matrix, providing important properties about the matrix. [[Determinant]]

## Detailed Technical Breakdown

### Question 1
#### (a) Basis for the Column Space of A
- Given matrix \( A \):
  \[
  A = \begin{pmatrix}
  1 & 2 & 0 & -4 & 1 & 4 \\
  2 & -1 & 1 & 5 & 0 & -3 \\
  1 & 0 & 1 & 3 & -1 & 2 \\
  1 & 0 & 2 & 6 & -1 & 4 \\
  1 & 0 & 0 & 0 & 0 & -1
  \end{pmatrix}
  \]
- RREF of \( A \):
  \[
  \text{RREF}(A) = \begin{pmatrix}
  1 & 0 & 0 & 0 & 0 & -1 \\
  0 & 1 & 0 & -2 & 0 & 3 \\
  0 & 0 & 1 & 3 & 0 & 2 \\
  0 & 0 & 0 & 0 & 1 & -1 \\
  0 & 0 & 0 & 0 & 0 & 0
  \end{pmatrix}
  \]
- **Basis**: The first, second, third, and fifth columns of \( A \):
  \[
  \left\{ \begin{pmatrix} 1 \\ 2 \\ 1 \\ 1 \\ 1 \end{pmatrix}, \begin{pmatrix} 2 \\ -1 \\ 0 \\ 0 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 1 \\ 2 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ -1 \\ -1 \\ 0 \end{pmatrix} \right\}
  \]
- **Conclusion**: The column space of \( A \) does not span \( \mathbb{R}^5 \) since it has only 4 vectors.

#### (b) Basis for the Row Space of A
- **Basis**: The first four rows of the RREF of \( A \):
  \[
  \left\{ \begin{pmatrix} 1 & 0 & 0 & 0 & 0 & -1 \end{pmatrix}, \begin{pmatrix} 0 & 1 & 0 & -2 & 0 & 3 \end{pmatrix}, \begin{pmatrix} 0 & 0 & 1 & 3 & 0 & 2 \end{pmatrix}, \begin{pmatrix} 0 & 0 & 0 & 0 & 1 & -1 \end{pmatrix} \right\}
  \]

#### (c) Nullspace of A
- **Explicit Set Notation**:
  \[
  \text{Nullspace}(A) = \left\{ s \begin{pmatrix} 0 \\ 1 \\ 2 \\ -3 \\ 1 \end{pmatrix} + t \begin{pmatrix} -3 \\ -2 \\ 0 \\ 1 \\ 0 \end{pmatrix} \mid s, t \in \mathbb{R} \right\}
  \]

#### (d) Column Space Membership
- **Vectors**:
  \[
  v_1 = \begin{pmatrix} 1 \\ 2 \\ 0 \\ 1 \end{pmatrix}, \quad v_2 = \begin{pmatrix} 1 \\ 2 \\ 1 \\ 2 \end{pmatrix}
  \]
- **RREF of \( B \) with \( v_1 \) and \( v_2 \)**:
  \[
  \text{RREF}(B) = \begin{pmatrix}
  1 & 0 & 0 & 0 & 0 & 1 \\
  0 & 1 & 0 & 0 & 0 & 0 \\
  0 & 0 & 1 & 0 & 0 & -1 \\
  0 & 0 & 0 & 1 & 0 & -1 \\
  0 & 0 & 0 & 0 & 1 & 0
  \end{pmatrix}
  \]
- **Conclusion**: \( v_1 \) is not in the column space of \( A \), while \( v_2 \) is.

#### (e) Projection of Vectors
- **Projection Formula**:
  \[
  \text{Projection}(v) = B(B^TB)^{-1}B^Tv
  \]
- **Result**: The projection of \( v_1 \) onto the column space of \( A \) is itself since it lies in the space.

#### (f) Orthogonal Vector
- **Nonzero Vector**: Any nonzero multiple of \( \begin{pmatrix} 1 \\ 2 \\ 4 \\ -3 \end{pmatrix} \) is orthogonal to the column space of \( A \).

#### (g) Basis Verification
- **Set \( S \)**:
  \[
  S = \left\{ \begin{pmatrix} 6 \\ 0 \\ 0 \\ 0 \\ 1 \\ 2 \\ 0 \\ 1 \\ 1 \\ 0 \\ 0 \\ 0 \end{pmatrix} \right\}
  \]
- **Verification**: Since \( |S| = 4 = \text{rank}(A) \), \( S \) is a basis for the column space of \( A \).

#### (h) Set Function
- **Function**: \( u = \begin{pmatrix} 2 \\ -2 \\ 4 \\ -1 \end{pmatrix} \)

### Question 2
#### (a) Conditions for Full Rank
- **Condition**: \( a \neq 1 \)

#### (b) RREF and Invertible Matrix
- **RREF**:
  \[
  R = \begin{pmatrix} 1 & 0 & 0 & -1 \\ 0 & 1 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}
  \]
- **Invertible Matrix**:
  \[
  P = \begin{pmatrix} \frac{a}{a-1} & \frac{1}{a-1} & -\frac{(a+1)}{a-1} \\ \frac{1}{a-1} & \frac{1}{a-1} & -\frac{2}{a-1} \end{pmatrix}
  \]

#### (c) Determinants
- **Determinants**:
  \[
  \text{det}(A A^T) = 3(a-1)^2, \quad \text{det}(A^T A) = 0
  \]

#### (d) Limit Calculation
- **Limit**:
  \[
  \lim_{n \to \infty} R R^T = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
  \]

### Question 3
#### (a) Eigenvector Verification
- **Eigenvector**:
  \[
  A v = (3 + 2i)v
  \]

#### (b) General Solution
- **Fundamental Set**:
  \[
  \left\{ e^{3t} \cos(2t), e^{3t} \sin(2t) \right\}
  \]
- **Wronskian**:
  \[
  W = -e^{6t} \neq 0
  \]

#### (c) Initial Value Problem
- **Solution**:
  \[
  y(t) = e^{3t} \begin{pmatrix} \cos(2t) - \sin(2t) \\ \sin(2t) + \cos(2t) \end{pmatrix}
  \]

## Implementation/Examples
```matlab
% MATLAB code for projection calculation
A = [1 2 0 -4 1 4; 2 -1 1 5 0 -3; 1 0 1 3 -1 2; 1 0 2 6 -1 4; 1 0 0 0 0 -1];
v = [1; 2; 1; 2];
proj = A * (A' * A) \ (A' * v);
```

> [!note] The basis for the column space of a matrix is crucial for understanding its dimensionality and the span of its vectors.
> [!important] Always verify the conditions for full rank when dealing with matrices to ensure accurate computations in linear algebra.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[RREF]]
- [[Eigenvector]]
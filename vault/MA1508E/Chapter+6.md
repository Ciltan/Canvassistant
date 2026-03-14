---
tags: [MA1508E, lecture-notes, academic]
---

# Chapter 6: Eigenanalysis

## Overview
This chapter delves into the concepts of [[Eigenvalues]] and [[Eigenvectors]], fundamental components in the study of linear transformations represented by square matrices. It explores the geometric interpretations of these concepts, the characteristic polynomial, and the conditions for diagonalization. Understanding these principles is crucial for applications in various fields, including computer science and engineering.

## Key Concepts & Definitions
- **Eigenvalue**: A scalar λ associated with a square matrix A such that there exists a nonzero vector v satisfying the equation \( Av = \lambda v \).
- **Eigenvector**: A nonzero vector v that satisfies the equation \( Av = \lambda v \) for a given eigenvalue λ.
- **Characteristic Polynomial**: The polynomial defined as \( \text{char}(A) = \text{det}(xI - A) \), where I is the identity matrix.
- **Diagonalization**: A process of transforming a matrix A into a diagonal matrix D via an invertible matrix P such that \( P^{-1}AP = D \).

## Detailed Technical Breakdown

### 6.1 Eigenvalues and Eigenvectors
- **Definition**: For a square matrix A of order n, a real number λ is an eigenvalue if there exists a nonzero vector v such that \( Av = \lambda v \).
- **Geometric Interpretation**: Eigenvectors are scaled by the eigenvalues when transformed by A.

#### Examples
- For the matrix 
  \[
  A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
  \]
  - Eigenvalues: λ = ±1
  - Eigenvectors: Corresponding vectors along the lines x = y and x = -y.

### Characteristic Polynomial
- **Definition**: The characteristic polynomial of A is given by \( \text{char}(A) = \text{det}(xI - A) \).
- **Example**: For 
  \[
  A = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}
  \]
  - Characteristic polynomial: \( x^2 - 1 \).

### Finding Eigenvalues
- **Theorem**: λ is an eigenvalue of A if and only if the homogeneous system \( (λI - A)v = 0 \) has nontrivial solutions.

### Eigenvalue and Invertibility
- **Theorem**: A square matrix A is invertible if and only if λ = 0 is not an eigenvalue of A.

### Algebraic Multiplicity
- **Definition**: The algebraic multiplicity of an eigenvalue λ is the largest integer r such that \( \text{det}(xI - A) = (x - λ)^r p(x) \).

### Eigenvalues of Triangular Matrices
- **Theorem**: The eigenvalues of a triangular matrix are the diagonal entries.

### Eigenspace
- **Definition**: The eigenspace associated with an eigenvalue λ is defined as \( E_\lambda = \{ v \in \mathbb{R}^n \mid Av = \lambda v \} \).

## Implementation/Examples
```markdown
# Example of Eigenvalue Calculation
Let A = 
\[
\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}
\]
The characteristic polynomial is calculated as follows:
det(xI - A) = det\left(\begin{pmatrix} x-1 & -2 \\ -3 & x-4 \end{pmatrix}\right) = (x-1)(x-4) - 6 = x^2 - 5x - 2.
```

> [!note] **Important Note**: Eigenvalues can provide insights into the stability of systems in engineering and physics.
> [!warning] **Caution**: Not all matrices are diagonalizable; a matrix may have fewer linearly independent eigenvectors than its order.

## Related
- [[Determinants]]
- [[Linear Transformations]]
- [[Diagonalization]]
- [[ModuleIndex]]
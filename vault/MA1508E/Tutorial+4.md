---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 4

## Overview
This tutorial focuses on key concepts in linear algebra, including determinants, matrix invertibility, and properties of linear systems. It explores the implications of matrix representations, such as diagonal and orthogonal matrices, and introduces the concept of nilpotent matrices. Additionally, the tutorial addresses linear combinations and spans in vector spaces, providing a comprehensive understanding of these foundational topics.

## Key Concepts & Definitions
- **Determinant**: The scalar value that is a function of a square matrix, denoted as [[det(A)]].
- **Invertible Matrix**: A matrix that has an inverse, denoted as [[A^(-1)]].
- **Diagonal Matrix**: A matrix in which the entries outside the main diagonal are all zero, denoted as [[D]].
- **Nilpotent Matrix**: A square matrix [[A]] such that [[A^k = 0]] for some positive integer [[k]].
- **Orthogonal Matrix**: A square matrix [[A]] satisfying [[A^T = A^(-1)]], where [[A^T]] is the transpose of [[A]].
- **Linear Combination**: A sum of scalar multiples of vectors.
- **Span**: The set of all possible linear combinations of a given set of vectors.

## Detailed Technical Breakdown

### 1. Determinants and Invertibility
- **(a)** If \( A = PDP^{-1} \), then:
  - \( \text{det}(A) = \text{det}(D) \)
- **(b)** \( A \) is invertible if all diagonal entries of \( D \) are nonzero.

### 2. Nilpotent Matrices
- **(c)** If \( A \) is nilpotent, then:
  - \( \text{det}(A) = 0 \)

### 3. Orthogonal Matrices
- **(d)** If \( A \) is orthogonal, then:
  - \( \text{det}(A) = \pm 1 \)

### 4. Linear Systems
- Given matrix \( A \):
  \[
  A = \begin{pmatrix}
  -1 & 3 & -4 \\
  2 & 4 & 1 \\
  -4 & 2 & -9
  \end{pmatrix}
  \]
- **(a)** Calculate \( \text{det}(A) \).
- **(b)** Show that the homogeneous linear system \( ABx = 0 \) has infinitely many solutions.

### 5. Expressing Solutions
- **(a)** For the linear system:
  \[
  \begin{align*}
  a + b - c - 2d &= 0 \\
  2a + b - c + d &= -2 \\
  -a + b - 3c + d &= 4
  \end{align*}
  \]
  - Express solutions in set notation.
  
- **(b)** Given reduced row-echelon form:
  \[
  \begin{pmatrix}
  1 & 0 & 0 & -1 & 1 & -2 \\
  0 & 1 & 0 & 1 & -1 & 3 \\
  0 & 0 & 1 & 0 & 1 & -2 \\
  0 & 0 & 0 & 0 & 0 & 0
  \end{pmatrix}
  \]
  - Express solutions in set notation.

### 6. Linear Combinations
- Given vectors \( u_1, u_2, u_3 \):
  \[
  u_1 = \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}, \quad u_2 = \begin{pmatrix} 5 \\ 3 \\ 2 \end{pmatrix}, \quad u_3 = \begin{pmatrix} 2 \\ 1 \\ 1 \end{pmatrix}
  \]
- **(a)** Express the following vectors as linear combinations of \( u_1, u_2, u_3 \):
  - \( \begin{pmatrix} 2 \\ 0 \\ 1 \\ -4 \end{pmatrix} \)
  - \( \begin{pmatrix} 3 \\ 0 \\ 1 \\ 6 \end{pmatrix} \)
  - \( \begin{pmatrix} -7 \\ 0 \\ 1 \\ -13 \end{pmatrix} \)
  - \( \begin{pmatrix} 3 \\ 0 \\ 1 \\ 4 \end{pmatrix} \)

- **(b)** Determine if it is possible to find two vectors \( v_1 \) and \( v_2 \) that are not multiples of each other and not linear combinations of \( u_1, u_2, u_3 \).

### 7. Spanning Sets
- Let \( V = \{(x, y, z) \in \mathbb{R}^3 : x - y - z = 0\} \).
- **(a)** Show that \( \text{span}(S) = V \) for \( S = \{(1, 1, 0), (5, 2, 0)\} \).
- **(b)** Show that \( \text{span}(T) = \mathbb{R}^3 \) for \( T = S \cup \{(0, 0, 1)\} \).

### 8. Spanning \( \mathbb{R}^4 \)
- Determine which of the following sets \( S \) spans \( \mathbb{R}^4 \):
  - (i) \( S = \{(1, 0, 1, 1), (0, 1, 1, 1), (0, 0, 1, 1), (1, 0, 1, 0)\} \)
  - (ii) \( S = \{(1, 1, 0), (2, 1, 0), (1, -1, 0)\} \)
  - (iii) \( S = \{(6, 2, 3, 5, 0), (4, 0, 2, 6, 4), (-2, 0, -1, -3, -2)\} \)
  - (iv) \( S = \{(1, 1, 0, 2, 1), (1, 2, 0, 1, 2), (0, -1, 1, 2, 3)\} \)

## Implementation/Examples
```matlab
% MATLAB code to compute mean, centered sample vector, variance, and standard deviation
n = 10;
x = [51, 35, 62, 78, 84, 55, 68, 92, 55, 69]';
mean_x = mean(x);
centered_x = x - mean_x;
variance_x = var(x);
std_dev_x = std(x);
percentile_75 = prctile(x, 75);
```

> [!note] **Important Concepts**: Understanding the properties of determinants and matrix types is crucial for solving linear algebra problems effectively.
> [!warning] **Common Pitfalls**: Be cautious with the assumptions regarding matrix invertibility and the implications of nilpotent matrices.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]
- [[Matlab+for+Engineering]]
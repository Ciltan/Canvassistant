---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 4 Solutions

## Overview
This note summarizes the solutions to Tutorial 4 for the MA1508E course at the National University of Singapore. It covers key concepts such as determinants, invertibility of matrices, nilpotent matrices, orthogonal matrices, and linear combinations. The solutions provided illustrate the application of these concepts through various mathematical problems and examples.

## Key Concepts & Definitions
- **Determinant**: The scalar value that is a function of a square matrix, denoted as [[det(A)]].
- **Invertible Matrix**: A matrix that has an inverse, denoted as [[A = PDP−1]].
- **Diagonal Matrix**: A matrix where all off-diagonal elements are zero, denoted as [[D]].
- **Nilpotent Matrix**: A square matrix [[A]] such that [[Ak = 0]] for some positive integer [[k]].
- **Orthogonal Matrix**: A square matrix [[A]] satisfying [[AT = A−1]].
- **Linear Combination**: A vector expressed as a sum of scalar multiples of other vectors.

## Detailed Technical Breakdown

### 1. Determinants and Invertibility
- **(a)** Given \( A = PDP^{-1} \):
  - \( \text{det}(A) = \text{det}(PDP^{-1}) = \text{det}(P)\text{det}(D)\text{det}(P^{-1}) = \text{det}(D) \)
  
- **(b)** \( A \) is invertible if and only if all diagonal entries of \( D \) are nonzero:
  - \( \text{det}(A) = d_1 d_2 \cdots d_n \) where \( d_i \) are diagonal entries of \( D \).

- **(c)** If \( A \) is nilpotent, then \( \text{det}(A) = 0 \):
  - \( 0 = \text{det}(A^k) = \text{det}(A)^k \Rightarrow \text{det}(A) = 0 \).

- **(d)** For orthogonal matrices:
  - \( 1 = \text{det}(A^{-1}A) = \text{det}(A^T)\text{det}(A) = \text{det}(A)^2 \Rightarrow \text{det}(A) = \pm 1 \).

### 2. Matrix Determinants
- **Example Matrix**: 
  \[
  A = \begin{pmatrix}
  -1 & 3 & -4 \\
  2 & 4 & 1 \\
  -4 & 2 & -9
  \end{pmatrix}
  \]
- **(a)** \( \text{det}(A) = 0 \) (as shown in Tutorial 3).

- **(b)** For a homogeneous linear system \( ABx = 0 \):
  - \( \text{det}(AB) = \text{det}(A)\text{det}(B) = 0 \Rightarrow \) infinitely many solutions.

### 3. Linear Systems
- **(a)** General solution expressed in set notation:
  \[
  \{ \begin{pmatrix}
  -2 - 3s \\
  2 + 19s \\
  9s \\
  s
  \end{pmatrix} : s \in \mathbb{R} \}
  \]

- **(b)** Reduced row-echelon form solutions:
  \[
  \{ \begin{pmatrix}
  -2 \\
  1 \\
  -1
  \end{pmatrix} + s \begin{pmatrix}
  0 \\
  1 \\
  0
  \end{pmatrix} + t \begin{pmatrix}
  -1 \\
  0 \\
  0
  \end{pmatrix} : s, t \in \mathbb{R} \}
  \]

### 4. Linear Combinations
- **Vectors**: \( u_1, u_2, u_3 \)
- **(a)** Expressing vectors as linear combinations:
  - For \( \begin{pmatrix} 2 \\ 3 \\ -7 \end{pmatrix} \): \( 2u_1 - u_2 - u_3 \).
  - For \( \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} \): trivial solution.
  - For \( \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \): not a linear combination.
  - For \( \begin{pmatrix} -4 \\ 6 \\ -13 \end{pmatrix} \): \( 3u_1 - 3u_2 + u_3 \).

### 5. Span and Linear Independence
- **(a)** Show \( \text{span}(S) = V \):
  - General solution confirms \( V \subseteq \text{span}(S) \).

- **(b)** Show \( \text{span}(T) = \mathbb{R}^3 \):
  - Row-echelon form indicates no zero rows, confirming span.

## Implementation/Examples
```matlab
% MATLAB Code for Mean Calculation
x = [51; 35; 62; 78; 84; 55; 68; 92; 55; 69];
xmean = (1/10) * dot(x, ones(10, 1)); % Mean
xcenter = x - xmean * ones(10, 1); % Centered vector
xvar = (1/9) * norm(xcenter)^2; % Variance
xstd = (1/sqrt(9)) * norm(xcenter); % Standard deviation
```

> [!note] The determinant of a matrix provides crucial information about its properties, such as invertibility and singularity.
> [!important] Understanding linear combinations is essential for grasping concepts of span and vector spaces in linear algebra.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Tutorial+1+Solution]]
- [[CS1231+TUTORIAL+3]]
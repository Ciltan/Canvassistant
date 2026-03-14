---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 2 Solutions

## Overview
This note summarizes the solutions to Homework 2 for the MA1508E course at the National University of Singapore. It covers key concepts in linear algebra, including subspaces, dimensions, and the properties of matrices. The solutions demonstrate the application of theoretical principles to practical problems, utilizing tools such as MATLAB for calculations.

## Key Concepts & Definitions
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. [[Subspace]]
- **Basis**: A set of linearly independent vectors that span a vector space. [[Basis]]
- **Dimension**: The number of vectors in a basis for a vector space. [[Dimension]]
- **Rank**: The dimension of the column space of a matrix. [[Rank]]
- **Nullity**: The dimension of the null space of a matrix. [[Nullity]]
- **Row Echelon Form (REF)**: A form of a matrix where all non-zero rows are above any rows of all zeros, and the leading coefficient of a non-zero row is always to the right of the leading coefficient of the previous row. [[Row Echelon Form]]

## Detailed Technical Breakdown

### Problem 1: Subspace and Basis
1. **Given Vectors**:
   \[
   u_1 = \begin{pmatrix} -1 \\ 1 \\ 2 \\ 3 \\ 1 \end{pmatrix}, \quad u_2 = \begin{pmatrix} 2 \\ -1 \\ 3 \\ 2 \\ 3 \end{pmatrix}, \quad u_3 = \begin{pmatrix} -1 \\ 3 \\ 2 \\ 3 \\ -1 \end{pmatrix}, \quad u_4 = \begin{pmatrix} -1 \\ 3 \\ -1 \\ 1 \\ 0 \end{pmatrix}
   \]
2. **Subspace V**: Defined as \( V = \{ v \in \mathbb{R}^5 \mid v \cdot u_i = 0, i=1,2,3,4 \} \).

#### (a) Show that V is a subspace and find a basis for V.
- **Solution**: 
  - Show that \( V \) is closed under addition and scalar multiplication.
  - Solve the homogeneous system to find a basis.

#### (b) Dimension of U
- **Solution**: 
  - Determine if \( \{u_1, u_2, u_3, u_4\} \) is linearly independent.
  - Conclude that \( \text{dim}(U) = 4 \).

#### (c) Orthogonality
- **Solution**: 
  - Show that for any \( u \in U \) and \( v \in V \), \( u \cdot v = 0 \).

### Problem 2: Rank and Nullity of Matrix A
1. **Matrix A**: A \( 5 \times 6 \) matrix with a given null space.
2. **Rank and Nullity**:
   - **Rank**: Found using the rank-nullity theorem.
   - **Nullity**: Determined from the number of free variables in the RREF.

### Problem 3: Basis for V
1. **Vectors in S**: 
   \[
   S = \{ u_1, u_2, u_3, u_4, u_5, u_6 \}
   \]
2. **Finding Basis**:
   - Identify a subset \( B \subset S \) that forms a basis for \( V \).

### Problem 4: Linear Combinations
1. **Vectors \( v_1 \) and \( v_2 \)**:
   - Calculate \( v_1 \) and \( v_2 \) using the basis \( S \).
2. **Linear Combinations**:
   - Show how to derive new vectors from existing ones using linear combinations.

## Implementation/Examples
```matlab
% MATLAB code to compute the RREF of matrix A
A = [1 -1 -1 1 -1 3; 2 0 2 1 1 3; 1 1 1 1 1 3; 2 2 6 -1 1 -1; 0 0 0 0 0 0];
RREF_A = rref(A);
disp(RREF_A);
```

> [!note] **Important**: Always ensure that your workings are clearly shown when submitting homework. This is crucial for receiving full credit.
> 
> [!warning] **Reminder**: When using MATLAB, ensure that all calculations are verified and documented to avoid errors in your final submission.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Stacks and Queues]]
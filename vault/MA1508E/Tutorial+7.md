---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 7

## Overview
This tutorial focuses on key concepts in linear algebra, including the column and row spaces of matrices, the rank-nullity theorem, and error detection in binary transmission. Students will explore various problems involving linear combinations, basis determination, and the implications of row equivalence in matrices. The tutorial also introduces practical applications of linear algebra in error correction codes.

## Key Concepts & Definitions
- **Column Space**: The set of all possible linear combinations of the column vectors of a matrix. [[Column Space]]
- **Row Space**: The set of all possible linear combinations of the row vectors of a matrix. [[Row Space]]
- **Null Space**: The set of all vectors that, when multiplied by the matrix, yield the zero vector. [[Null Space]]
- **Rank**: The dimension of the row space or column space of a matrix. [[Rank]]
- **Nullity**: The dimension of the null space of a matrix. [[Nullity]]
- **Linear Combination**: A sum of scalar multiples of vectors. [[Linear Combination]]
- **Orthonormal Set**: A set of vectors that are both orthogonal and of unit length. [[Orthonormal Set]]
- **Error-Correcting Codes**: Techniques used to detect and correct errors in data transmission. [[Error-Correcting Codes]]

## Detailed Technical Breakdown

### Problem 1: Column and Row Spaces
1. **Matrix A and vector b**:
   - \( A = \begin{pmatrix} 1 & -1 & 1 \\ 1 & 1 & -1 \\ -1 & -1 & 1 \end{pmatrix} \)
   - \( b = \begin{pmatrix} 1 \\ -1 \\ 1 \\ 0 \end{pmatrix} \)
   - **Task**: Determine if \( b \) is in the column space of \( A \).

2. **Matrix A and vector b**:
   - \( A = \begin{pmatrix} -1 & 3 & 1 \\ 1 & 9 & 1 \\ 1 & 1 & 1 \end{pmatrix} \)
   - \( b = \begin{pmatrix} 5 \\ 1 \\ -1 \end{pmatrix} \)
   - **Task**: Determine if \( b \) is in the row space of \( A \).

3. **Matrix A**:
   - \( A = \begin{pmatrix} 0 & 1 & 2 & 1 \\ 1 & 2 & 1 & 3 \\ 0 & 1 & 2 & 2 \end{pmatrix} \)
   - **Task**: Check if the row space and column space of \( A \) span \( \mathbb{R}^4 \).

### Problem 2: Basis Determination
- For each matrix \( A \):
  - **(i)** Find a basis for the row space.
  - **(ii)** Find a basis for the column space.
  - **(iii)** Find a basis for the null space.
  - **(iv)** Determine rank(A) and nullity(A) and verify the dimension theorem.
  - **(v)** Check if \( A \) is full rank.

### Problem 3: Null Space Containment
- Given matrices \( A \) and \( B \) such that \( AB = 0 \), show that the column space of \( B \) is contained in the null space of \( A \.

### Problem 4: Basis and Linear Combinations
1. **Vectors**:
   - \( v_1 = (1, -2, 0, 3) \)
   - \( v_2 = (2, -5, -3, 6) \)
   - \( v_3 = (0, 1, 3, 0) \)
   - \( v_4 = (2, -1, 4, -7) \)
   - \( v_5 = (5, -8, 1, 2) \)
   - **Task**: Find a basis for the span of these vectors.

### Problem 5: Orthonormal Sets
- Given an orthonormal set \( \{v_1, v_2, v_3\} \):
  - **(a)** Calculate \( x \cdot y \).
  - **(b)** Find \( ||x|| \) and \( ||y|| \).
  - **(c)** Determine the angle \( \theta \) between \( x \) and \( y \).

### Problem 6: Linear Systems
1. **Linear Equation**: Express \( a_1 x_1 + a_2 x_2 + \ldots + a_n x_n = b \) as \( a \cdot x = b \).
2. **Solution Set**: Find the solution set for the given linear system.
3. **Nonzero Vector**: Find a nonzero vector \( v \in \mathbb{R}^3 \) such that \( a \cdot v = 0 \).

### Supplementary Problems
- **MATLAB and Error Correction**: Investigate binary n-space and error detection in transmission.
- **Hamming Code**: Explore the Hamming matrix and its implications for error correction.

> [!note] **Important**: Understanding the relationship between row and column spaces is crucial for solving linear systems and determining the properties of matrices.
> 
> [!warning] **Caution**: Ensure to verify the conditions for full rank and the implications of null spaces when working with matrices.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Stacks and Queues]]
- [[Midterm+Briefing]]
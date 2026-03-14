---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 2 Solutions

## Overview
This document outlines the solutions to Homework 2 for the MA1508E course at the National University of Singapore. It includes detailed explanations of subspaces, basis, rank, and nullspace, along with MATLAB usage guidelines for calculations. The solutions are structured to enhance understanding of linear algebra concepts relevant to engineering applications.

## Key Concepts & Definitions
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. 
- **Basis**: A set of linearly independent vectors that span a vector space.
- **Rank**: The dimension of the column space of a matrix, indicating the maximum number of linearly independent column vectors.
- **Nullspace**: The set of all vectors that, when multiplied by a given matrix, yield the zero vector.

## Detailed Technical Breakdown

### Problem 1: Subspaces
1. **Let** \( w = \begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix} \)
   - **W**: \( \{ u \in \mathbb{R}^4 \mid u \cdot w = 2 \} \)
   - **V**: \( \{ u - \begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix} \mid u \in W \} \)

   - **(a)** Is W a subspace?
     - **Solution**: W is not a subspace since it does not contain the origin, as \( 0 \cdot w = 0 \neq 2 \).

   - **(b)** Show that V is a subspace and that \( T = \begin{pmatrix} 1 \\ 0 \\ 0 \\ 0 \\ 1 \end{pmatrix} \) is a basis for V.
     - **Solution**: 
       - Write \( u = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} \).
       - Show that \( u \cdot w = x_1 + 2x_2 - x_3 = 2 \).
       - Explicitly express W and V.

### Problem 2: Rank and Basis
1. **Let** \( A = \begin{pmatrix} a_1 & a_2 & a_3 & a_4 & a_5 \end{pmatrix} \)
   - **Row Equivalent**: \( R = \begin{pmatrix} 1 & 2 & -1 & 2 & -1 \\ 0 & 1 & -1 & 1 & -1 \\ 0 & 0 & 0 & 1 & 1 \end{pmatrix} \)

   - **(a)** What is the rank of A?
     - **Solution**: The rank of A is 3, as determined by the number of non-zero rows in R.

   - **(b)** Show that \( \begin{pmatrix} 2 \\ 11 \\ 5 \end{pmatrix}, \begin{pmatrix} 2 \\ 1 \\ 3 \end{pmatrix}, \begin{pmatrix} 2 \\ 2 \\ 4 \end{pmatrix} \) is a basis for the column space of A.
     - **Solution**: Demonstrate linear independence and that the dimension matches the rank.

### Problem 3: Row Space and Nullspace
1. **Given** \( A^TA = \begin{pmatrix} 3 & 4 & 0 \\ 4 & 10 & -3 \\ 0 & -3 & 3 \end{pmatrix} \)

   - **(a)** Solve the homogeneous system \( Ax = 0 \).
     - **Solution**: Since \( A^TA \) is invertible, the only solution is the trivial solution.

   - **(b)** Find a basis for the nullspace of A.
     - **Solution**: The nullspace is derived from the RREF of A.

## Implementation/Examples
```matlab
% MATLAB code to compute the RREF of a matrix
A = [1 -2 -3; -1 0 3; 0 1 3];
RREF_A = rref(A);
disp(RREF_A);
```

> [!note] Ensure all workings are shown clearly when submitting homework.
> [!important] Remember to name your PDF file as per the guidelines: StudentNo HW2.pdf.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
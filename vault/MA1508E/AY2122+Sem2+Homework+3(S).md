---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 3 - Solutions Overview

## Overview
This note summarizes the solutions to key problems in the MA1508E course, focusing on the concepts of subspaces, bases, and the reduced row-echelon form (RREF) of matrices. The solutions demonstrate the application of linear algebra principles to determine the properties of vector spaces and their dimensions, as well as the relationships between different bases.

## Key Concepts & Definitions
- **Subspace**: A subset of a vector space that is closed under vector addition and scalar multiplication. [[Subspace]]
- **Basis**: A set of linearly independent vectors that span a vector space. [[Basis]]
- **Dimension**: The number of vectors in a basis for a vector space, indicating its size. [[Dimension]]
- **Reduced Row-Echelon Form (RREF)**: A form of a matrix that simplifies the process of solving linear equations. [[RREF]]
- **Span**: The set of all possible linear combinations of a given set of vectors. [[Span]]
- **Linear Independence**: A property of a set of vectors where no vector can be expressed as a linear combination of the others. [[Linear Independence]]

## Detailed Technical Breakdown

### Problem 1: Subspace and Basis
1. **Given Vector**:
   \[
   V = \begin{pmatrix}
   0 & 2 & -1 \\
   0 & -2 & 1 \\
   0 & -4 & 2
   \end{pmatrix}
   \]
   - **Prove that V is a subspace of \( \mathbb{R}^3 \)**:
     - Since \( V \) is the solution set to a homogeneous system, it is a subspace of \( \mathbb{R}^3 \).
   - **Finding a Basis**:
     - RREF of the matrix yields:
       \[
       \begin{pmatrix}
       1 & 0 \\
       0 & 1 \\
       0 & 0
       \end{pmatrix}
       \]
     - Basis for \( V \): \( \{(0, 1, 2), (0, 1, -1)\} \)
     - **Dimension**: 2

### Problem 2: Basis Verification
1. **Given Set**:
   \[
   S = \begin{pmatrix}
   2 & 2 & 2 & 1 \\
   2 & 1 & 3 & -1 \\
   1 & 2 & 0 & 1 \\
   -1 & 1 & -3 & -1 \\
   2 & 0 & 4 & 0
   \end{pmatrix}
   \]
   - **(a) Is \( S \) a basis for \( V \)?**
     - Check linear independence using RREF:
       - Result shows a non-pivot column, hence \( S \) is not linearly independent.
   - **(b) Basis \( T \)**:
     - Let \( T = \{(0, 1, 0), (0, 0, 1)\} \)
     - Show \( T \) is a basis for \( V \):
       - RREF confirms that \( T \) spans \( V \) and is linearly independent.
   - **(c) Coordinates of \( v \)**:
     - Given \( v = \begin{pmatrix} 1 \\ -2 \\ 2 \end{pmatrix} \)
     - RREF shows \( v \) is in \( V \) with coordinates \( [v]_T = \begin{pmatrix} 1 \\ 1 \end{pmatrix} \).

### Problem 3: Matrix and Nullspace
1. **Matrix \( A \)**:
   \[
   A = \begin{pmatrix}
   1 & 1 & -1 & 0 & 2 \\
   0 & 1 & 1 & 0 & -1 \\
   0 & 0 & 0 & 1 & -1 \\
   0 & 0 & 0 & 0 & 0
   \end{pmatrix}
   \]
   - **(a) RREF of \( A \)**:
     - Derived from the original matrix, confirming it is in RREF.
   - **(b) Finding \( A \)**:
     - Using relationships from RREF, derive \( a_3 \) and \( a_5 \).
   - **(c) Row Space**:
     - Check vectors \( v_1 \) and \( v_2 \) against \( A^T \):
       - \( v_1 \) is in the row space, \( v_2 \) is not.

> [!important] Understanding the properties of subspaces and bases is crucial for mastering linear algebra concepts. Ensure to practice these definitions with various examples to solidify your understanding.

> [!note] The RREF is a powerful tool for solving systems of linear equations and determining the properties of matrices. Familiarity with this technique will greatly enhance your problem-solving skills in linear algebra.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
- [[Stacks and Queues]]
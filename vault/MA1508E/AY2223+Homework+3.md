---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 3

## Overview
This document outlines the requirements and tasks for Homework 3 in the MA1508E course at the National University of Singapore. The homework involves working with symmetric matrices, eigenvalues, projections, polynomial fitting, and solving initial value problems. Students are expected to demonstrate their understanding of linear algebra concepts through calculations and proofs, utilizing tools such as MATLAB where appropriate.

## Key Concepts & Definitions
- **Symmetric Matrix**: A matrix that is equal to its transpose.
- **Eigenvalues**: Scalars associated with a linear transformation represented by a matrix, indicating the factor by which the eigenvector is scaled.
- **Eigenvectors**: Non-zero vectors that change at most by a scalar factor when a linear transformation is applied.
- **Characteristic Polynomial**: A polynomial which is derived from the determinant of a matrix subtracted by a scalar multiple of the identity matrix.
- **Projection**: The operation of projecting a vector onto a subspace.
- **Orthonormal Basis**: A basis consisting of orthogonal vectors, each of unit length.
- **Polynomial Fitting**: The process of finding a polynomial that best fits a set of data points.

## Detailed Technical Breakdown

### 1. Symmetric Matrix and Eigenvalues
- Let \( A \) be an order 3 symmetric matrix with eigenvalues \( -1, 1, 2 \).
- Given eigenvectors:
  - \( v_{-1} = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} \) associated with eigenvalue \( -1 \)
  - \( v_{1} = \begin{pmatrix} -1 \\ 2 \\ 0 \end{pmatrix} \) associated with eigenvalue \( 1 \)

#### Tasks:
- **(a)** Write down the characteristic polynomial of \( A \).
- **(b)** Find an eigenvector associated with eigenvalue \( 2 \) and explain the derivation.
- **(c)** Express \( A \) as \( PDPT \) for some orthogonal matrix \( P \) and diagonal matrix \( D \).

### 2. Projection and Orthonormal Basis
- Given vectors:
  - \( u_1 = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix}, u_2 = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, u_3 = \begin{pmatrix} -2 \\ 1 \\ -1 \end{pmatrix} \)
  - \( V = \text{span}\{u_1, u_2, u_3\} \)

#### Tasks:
- **(a)** Find \( u_p \), the projection of \( u = \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \) into \( V \).
- **(b)** Find an orthonormal basis \( T = \{v_1, v_2, v_3\} \) of \( V \).
- **(c)** Given \( v = \begin{pmatrix} 2 \\ 1 \\ -4 \end{pmatrix} \), find \( [v]_T \).

### 3. Polynomial Fitting
- Given data set:
  - \( x: -2, -1, 0, 1, 2 \)
  - \( y: 0, 12, 12, 6, 0 \)

#### Tasks:
- **(a)** Determine if a degree 2 polynomial \( p(x) = a_2 x^2 + a_1 x + a_0 \) can pass through the data points.
- **(b)** Find a degree 3 polynomial \( p(x) = a_3 x^3 + a_2 x^2 + a_1 x + a_0 \) that fits the data.

### 4. Eigenvectors and Initial Value Problem
- Given matrix:
  \[
  A = \begin{pmatrix}
  1 & 2 & -1 & 0 & -1 \\
  -1 & 3 & 0 & 1 & 0 \\
  -5 & 6 & 4 & 3 & -3 \\
  8 & -8 & -6 & -5 & 2 \\
  3 & -4 & -3 & -3 & 2
  \end{pmatrix}
  \]

#### Tasks:
- **(a)** Verify that \( \begin{pmatrix} 1+i \\ 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} \) and \( \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \\ 1 \end{pmatrix} \) are eigenvectors of \( A \).
- **(b)** Find a vector \( v \) such that \( Av = v \).
- **(c)** Find a generalized eigenvector associated with eigenvalue \( 1 \).
- **(d)** Solve the initial value problem with the given conditions.

> [!important] Ensure all workings are shown clearly, whether using MATLAB or manual calculations. 
> [!note] Remember to submit your answers in the specified format, either as scanned images or a digital PDF.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Logic - Propositional Logic]]
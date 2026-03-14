---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 4 - Solutions Overview

## Overview
This note summarizes the solutions to key problems in the MA1508E course, focusing on orthogonal diagonalization, initial value problems, and differential systems. The solutions utilize concepts from [[Linear Algebra]], including eigenvalues, eigenvectors, and the Gram-Schmidt process. The material is structured to provide clarity on the methods used and the results obtained, serving as a reference for students in engineering mathematics.

## Key Concepts & Definitions
- **Orthogonal Diagonalization**: The process of diagonalizing a matrix using an orthogonal basis.
- **Eigenvalues**: Scalars associated with a linear transformation that indicate the factor by which the eigenvector is stretched.
- **Eigenvectors**: Non-zero vectors that change at most by a scalar factor during a linear transformation.
- **Gram-Schmidt Process**: A method for orthonormalizing a set of vectors in an inner product space.
- **Initial Value Problem**: A differential equation along with specified values at a given point.
- **Differential System**: A set of differential equations that describe a system's behavior over time.

## Detailed Technical Breakdown

### Problem 1: Orthogonally Diagonalize Matrix A
Given the matrix:
\[ A = \begin{pmatrix} 5 & 1 & 1 \\ 1 & 5 & 1 \\ 1 & 1 & 5 \end{pmatrix} \]

- **Characteristic Polynomial**:
  \[
  \text{det}(xI - A) = (x - 4)^2(x - 7)
  \]
- **Eigenvalues**: 
  - \( \lambda_1 = 4 \)
  - \( \lambda_2 = 7 \)

- **Eigenvectors**:
  - For \( \lambda = 7 \):
    \[
    \text{Basis of } E_7 = \left\{ \begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix} \right\}
    \]
  - For \( \lambda = 4 \):
    \[
    \text{Basis of } E_4 = \left\{ \begin{pmatrix} 1 \\ 0 \\ -1 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix} \right\}
    \]

- **Orthonormal Basis**:
  - Apply the Gram-Schmidt process to obtain orthonormal bases for \( E_4 \) and \( E_7 \).

### Problem 2: Solve the Initial Value Problem
Given the system:
\[
\begin{align*}
y_1' &= y_1 + 3y_2 + 2y_3 \\
y_2' &= y_1 - 2y_2 + 3y_3 \\
y_3' &= y_1 + y_2
\end{align*}
\]
with initial conditions \( y_1(0) = 1, y_2(0) = 1, y_3(0) = 1 \).

- **Matrix Representation**:
  \[
  A = \begin{pmatrix} 1 & 3 & 2 \\ 1 & -2 & 3 \\ 1 & 1 & 0 \end{pmatrix}
  \]
- **Eigenvalues**: \( \lambda = 3, 1+i, 1-i \)

- **General Solution**:
  \[
  x(t) = c_1 e^{3t} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} + c_2 e^{t} \begin{pmatrix} \cos(t) \\ \sin(t) \\ 0 \end{pmatrix} + c_3 e^{t} \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}
  \]

### Problem 3: General Solution to the Differential System
Given the system:
\[
\begin{align*}
y_1' &= 2y_1 + y_2 \\
y_2' &= -2y_1 + y_2
\end{align*}
\]
- **Matrix Representation**:
  \[
  A = \begin{pmatrix} 1 & 2 \\ -2 & 1 \end{pmatrix}
  \]
- **Eigenvalue**: \( \lambda = 1 \) (repeated)

- **General Solution**:
  \[
  x(t) = e^{t} \left( c_1 \begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2 t \begin{pmatrix} 1 \\ 1 \end{pmatrix} \right)
  \]

> [!important] Ensure to practice the Gram-Schmidt process for orthonormalization as it is crucial for diagonalization tasks in linear algebra.
> [!note] Review the properties of eigenvalues and eigenvectors, as they are foundational for understanding linear transformations.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Midterm+Briefing]]
- [[Determinants]]
- [[Matlab+for+Engineering]]
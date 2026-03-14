---
tags: [MA1508E, lecture-notes, academic]
---

# Chapter 2: Matrix Algebra

## Overview
This chapter introduces the fundamental concepts of matrix algebra, focusing on the definition and types of matrices, operations such as addition and multiplication, and the properties of linear systems. Understanding these concepts is crucial for applications in engineering and other fields that utilize linear algebra.

## Key Concepts & Definitions
- A **matrix** is a rectangular array of real numbers, denoted as \( A = (a_{ij})_{m \times n} \), where \( m \) is the number of rows and \( n \) is the number of columns.
- The **size** of a matrix is expressed as \( m \times n \).
- The **(i,j)-entry** of a matrix is the element located in the \( i \)-th row and \( j \)-th column, denoted as \( a_{ij} \).
- **Special types of matrices** include:
  - **Column vector**: An \( n \times 1 \) matrix.
  - **Row vector**: A \( 1 \times n \) matrix.
  - **Zero matrix**: A matrix where all entries are zero, denoted as \( 0_{m \times n} \).
  - **Square matrix**: A matrix where the number of rows equals the number of columns.
  - **Diagonal matrix**: A square matrix where all off-diagonal entries are zero.
  - **Identity matrix**: A diagonal matrix with ones on the diagonal.
  - **Symmetric matrix**: A matrix that is equal to its transpose, \( A = A^T \).

## Detailed Technical Breakdown

### 2.1 Definition and Special Types of Matrices
- **Matrix Definition**: 
  \[
  A = \begin{pmatrix}
  a_{11} & a_{12} & \cdots & a_{1n} \\
  a_{21} & a_{22} & \cdots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{m1} & a_{m2} & \cdots & a_{mn}
  \end{pmatrix}
  \]
- **Example**: 
  \[
  A = \begin{pmatrix}
  1 & 2 & -1 & 5 & 10 \\
  3 & 5 & 13 & 23 & 41 \\
  -7 & 2 & 0 & 0 & 11
  \end{pmatrix}
  \]
  - Size: \( 3 \times 5 \)
  - (2,3)-entry: \( 13 \)

### 2.2 Matrix Algebra
- **Matrix Addition**: 
  \[
  A + B = \begin{pmatrix}
  a_{11} + b_{11} & a_{12} + b_{12} & \cdots \\
  a_{21} + b_{21} & a_{22} + b_{22} & \cdots \\
  \vdots & \vdots & \ddots
  \end{pmatrix}
  \]
- **Scalar Multiplication**: 
  \[
  cA = \begin{pmatrix}
  ca_{11} & ca_{12} & \cdots \\
  ca_{21} & ca_{22} & \cdots \\
  \vdots & \vdots & \ddots
  \end{pmatrix}
  \]

### 2.3 Linear System and Matrix Equation
- A linear system can be expressed in matrix form as \( Ax = b \), where:
  - \( A \) is the coefficient matrix.
  - \( x \) is the variable vector.
  - \( b \) is the constant vector.

## Implementation/Examples
```plaintext
Example of a linear system:
3x + 2y - z = 1
x + 2y + z = 3
x + z = 2

Matrix form:
A = \begin{pmatrix}
3 & 2 & -1 \\
1 & 2 & 1 \\
1 & 0 & 1
\end{pmatrix}, \quad
x = \begin{pmatrix}
x \\
y \\
z
\end{pmatrix}, \quad
b = \begin{pmatrix}
1 \\
3 \\
2
\end{pmatrix}
```

> [!note] **Important Properties**: 
> - A homogeneous linear system \( Ax = 0 \) is always consistent.
> - The zero solution is the trivial solution; non-zero solutions are nontrivial.

## Related
- [[Chapter+4+How+Designers+Think]]
- [[Determinants]]
- [[Logic - Propositional Logic]]
- [[Midterm+Briefing]]
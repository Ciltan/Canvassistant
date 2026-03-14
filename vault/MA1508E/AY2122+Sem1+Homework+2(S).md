---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 2 - Solutions Overview

## Overview
This note provides a structured summary of solutions to linear systems and matrix operations as covered in MA1508E. It includes methods for solving linear equations, computing matrix inverses, and determining determinants. The solutions are presented with detailed steps and explanations, making them useful for students seeking to understand the underlying concepts of linear algebra.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables. 
- **Matrix Inverse**: A matrix \( A^{-1} \) that, when multiplied by \( A \), yields the identity matrix.
- **Determinant**: A scalar value that is a function of a square matrix, providing important properties about the matrix, such as invertibility.
- **Elementary Row Operations**: Operations used to manipulate matrices, including row swapping, scaling, and row addition.

## Detailed Technical Breakdown

### 1. Solving Linear Systems
- Given the system:
  - \( x_1 + x_3 - x_4 = a \)
  - \( x_2 - 2x_4 = b \)
  - \( x_1 + 2x_3 - 2x_4 = c \)

#### Solutions for Different Values
- **(i)** For \( a = -1, b = 1, c = 4 \):
  - General solution: \( x_1 = -6, x_2 = 1 + 2s, x_3 = 5 + s, x_4 = s, s \in \mathbb{R} \)
  
- **(ii)** For \( a = 1, b = 4, c = 5 \):
  - General solution: \( x_1 = -3, x_2 = 4 + 2s, x_3 = 4 + s, x_4 = s, s \in \mathbb{R} \)

- **(iii)** For \( a = 2, b = 3, c = 5 \):
  - General solution: \( x_1 = -1, x_2 = 3 + 2s, x_3 = 3 + s, x_4 = s, s \in \mathbb{R} \)

### 2. Computing the Inverse of a Matrix
- Let \( A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & -6 & -3 \\ 1 & 0 & 2 \end{pmatrix} \)

#### Steps to Compute \( A^{-1} \)
- Perform elementary row operations:
  - \( R_1 \) and \( R_2 \) operations to form the identity matrix.
  
- Final result:
  - \( A^{-1} = \begin{pmatrix} -\frac{3}{2} & \frac{1}{3} & \frac{1}{2} \\ 1 & -\frac{1}{3} & 0 \end{pmatrix} \)

### 3. Determinants
- For matrix \( A \):
  - \( \text{det}(A) = -5 \) computed via cofactor expansion along the first column.

#### Properties of Determinants
- If \( B \) is a square matrix with \( \text{det}(B) = 3 \):
  - \( \text{det}\left(\frac{1}{2} A^T\right) = \frac{1}{16} \cdot (-5) = -\frac{5}{16} \)
  - \( \text{det}(AB^{-1}) = -\frac{5}{3} \)
  - \( \text{det}((3B)^{-1}) = \frac{1}{243} \)

## Implementation/Examples
```plaintext
# Example of solving a linear system
x1 + x3 - x4 = a
x2 - 2x4 = b
x1 + 2x3 - 2x4 = c
```

> [!note] **Important Note**: The general solutions for the linear systems depend on the values of \( a, b, c \) and can be expressed in terms of a parameter \( s \).
> 
> [!warning] **Caution**: Ensure that the matrix is invertible before attempting to compute its inverse; this is determined by checking if the determinant is non-zero.

## Related
- See also [[AY2122+Sem1+Homework+3]], [[Determinants]], [[Matlab+for+Engineering]], and [[Logic - Propositional Logic]] for further exploration of related topics in linear algebra and engineering mathematics.
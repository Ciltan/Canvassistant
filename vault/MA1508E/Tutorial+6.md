---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Tutorial 6

## Overview
This tutorial focuses on the concepts of vector spaces, linear independence, and the properties of determinants in the context of linear algebra. It explores the conditions under which specific sets of vectors form a basis for \( \mathbb{R}^3 \) and examines the implications of these conditions on the determinants of matrices. Additionally, the tutorial delves into binary vector spaces and their properties, providing a comprehensive understanding of these fundamental concepts.

## Key Concepts & Definitions
- **Basis**: A set of vectors in a vector space that are linearly independent and span the space.
- **Determinant**: A scalar value that can be computed from the elements of a square matrix, providing important properties about the matrix, such as whether it is invertible.
- **Linear Independence**: A set of vectors is linearly independent if no vector in the set can be expressed as a linear combination of the others.
- **Subspace**: A subset of a vector space that is itself a vector space under the same operations.

## Detailed Technical Breakdown

### 1. Conditions for Basis Formation
- **Problem 1(a)**: Determine values of \( a \) for which vectors \( u_1, u_2, u_3 \) form a basis for \( \mathbb{R}^3 \).
- **Problem 1(b)**: Identify values of \( a \) for which the determinant of the matrix formed by these vectors is non-zero.
- **Problem 1(c)**: Formulate a conjecture based on the results of (a) and (b).

### 2. Coordinate Vectors
- **Problem 2**: For given vectors \( v \) and basis \( S = \{u_1, u_2, u_3\} \), find the coordinate vector of \( v \) relative to \( S \).
  - **Example**:
    - \( v = \begin{pmatrix} 1 \\ -2 \\ 6 \end{pmatrix}, u_1 = \begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}, u_2 = \begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}, u_3 = \begin{pmatrix} 0 \\ 1 \\ 3 \end{pmatrix} \)

### 3. Subspaces and Their Properties
- **Problem 4**: Analyze the properties of subspaces \( U \) and \( V \) in \( \mathbb{R}^n \).
  - **(a)**: Is \( U \cup V \) a subspace?
  - **(b)**: Show that \( U + V \) is a subspace and determine its dimension.
  - **(c)**: Verify that \( U + V \) contains both \( U \) and \( V \).
  - **(d)**: Determine the dimensions of \( U \) and \( V \).
  - **(e)**: Show that \( U \cap V \) is a subspace and find its dimension.
  - **(f)**: Prove that \( \text{dim}(U + V) = \text{dim}(U) + \text{dim}(V) - \text{dim}(U \cap V) \).

### 4. Binary Vector Spaces
- **Problem 5**: Explore the properties of binary digits in vector spaces.
  - **(a)**: Complete addition and multiplication tables for binary digits.
  - **(b)**: Analyze the number of vectors in \( B^n \) and compare with \( \mathbb{R}^n \).
  - **(c)**: Show that standard unit vectors form a basis for \( B^3 \) and analyze the set \( T \).
  - **(d)**: Investigate the Hamming matrix and its properties.

## Implementation/Examples
```markdown
# Example of Determinant Calculation
Given the matrix:
\[
A = \begin{pmatrix}
a & -1 & 1 \\
1 & a & -1 \\
-1 & 1 & a
\end{pmatrix}
\]
The determinant can be computed using the formula:
\[
\text{det}(A) = a^3 - 3a + 2
\]
```

> [!important] **Note**: The determinant must be non-zero for the vectors to form a basis for \( \mathbb{R}^3 \).

> [!warning] **Caution**: Ensure that the vectors are linearly independent before concluding they form a basis.

## Related
- See [[Determinants]] for more on calculating determinants.
- Refer to [[Linear Independence]] for a deeper understanding of linear independence in vector spaces.
- Explore [[Binary Vector Spaces]] for insights into operations in binary systems.
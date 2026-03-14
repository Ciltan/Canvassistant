---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 2 - Homework 2

## Overview
This note summarizes the key components of Homework 2 for the MA1508E course, focusing on matrix operations, determinants, and linear systems. The homework consists of three main questions, each designed to assess understanding of matrix manipulation, including finding inverses, determinants, and solving linear equations. Students are required to demonstrate their workings clearly and submit their answers in a specified format.

## Key Concepts & Definitions
- **Matrix A**: A rectangular array of numbers arranged in rows and columns.
- **Elementary Row Operations**: Operations that can be performed on rows of a matrix to simplify it, including row swapping, scaling, and row addition.
- **Determinant**: A scalar value that is a function of a square matrix, providing important properties about the matrix, such as whether it is invertible.
- **Row Equivalent**: Two matrices are row equivalent if one can be transformed into the other through a series of elementary row operations.
- **Cofactor Expansion**: A method for calculating the determinant of a matrix by expanding along a row or column.

## Detailed Technical Breakdown

### Question 1
1. Given the matrix:
   \[
   A = \begin{pmatrix}
   2 & -3 & 1 \\
   -1 & -1 & -1 \\
   -3 & 1 & -1 \\
   0 & 2 & 0 \\
   -1 & 2 & 0 \\
   2 & 4 & -2
   \end{pmatrix}
   \]
   - **Task**: Determine the value of \( A \) and show workings clearly.

### Question 2
1. Given the matrix:
   \[
   A = \begin{pmatrix}
   1 & 1 & 1 \\
   0 & -1 & -1 \\
   0 & 2 & -1
   \end{pmatrix}
   \]
   - **(a)** Compute the inverse of \( A \) using 5 elementary row operations.
   - **(b)** Express \( A \) as a product of 5 elementary row operations.
   - **(c)** Calculate the determinant of \( A \) using the result from (b).
   - **(d)** Solve the linear system:
     \[
     \begin{align*}
     x_1 + x_2 + x_3 &= 1 \\
     -x_2 - x_3 &= 3 \\
     2x_2 - x_3 &= 3
     \end{align*}
     \]
   - **(e)** Determine if \( A \) is row equivalent to:
     \[
     \begin{pmatrix}
     1 & 0 & 1 \\
     0 & 0 & 0
     \end{pmatrix}
     \]
     Provide an explanation.

### Question 3
1. Given the matrix:
   \[
   A = \begin{pmatrix}
   2 & -2 & -2 & 1 \\
   1 & 0 & -1 \\
   1 & a & 0 & 1 \\
   1 & 2 & 0 & 0
   \end{pmatrix}
   \]
   - **(a)** Compute the determinant of \( A \) using cofactor expansion.
   - **(b)** If \( \text{det}(B) = 18 \), find \( \text{det}(3A^T B^{-1}) \).

## Implementation/Examples
```plaintext
# Example of elementary row operations
1. R1 ↔ R2 (swap rows)
2. R2 = R2 + R1 (add row 1 to row 2)
3. R3 = R3 - 2*R1 (subtract 2 times row 1 from row 3)
4. R1 = R1 * 1/2 (scale row 1)
5. R3 = R3 + R2 (add row 2 to row 3)
```

> [!note] **Submission Guidelines**: Ensure that your answers are written on A4 size papers, with your student number and name clearly indicated. Each page must be numbered, and submissions should be merged into a single PDF file named according to the specified format.

> [!important] **Clarity in Workings**: It is crucial to show all workings clearly for each question to receive full marks. Pay attention to the format and ensure that your calculations are easy to follow.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Logic - Propositional Logic]]
- [[Tutorial+1+Solution]]
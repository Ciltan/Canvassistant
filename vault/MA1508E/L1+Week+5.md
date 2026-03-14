---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - L1 Week 5 Live Lecture

## Overview
This lecture focuses on the concepts of matrix invertibility and Gaussian elimination, essential topics in linear algebra. Students are reminded of upcoming deadlines for quizzes and homework, as well as the midterm exam schedule. The lecture includes practical examples of determining matrix invertibility and finding inverses using Gaussian elimination.

## Key Concepts & Definitions
- **Matrix Invertibility**: A matrix is invertible if there exists another matrix such that their product is the identity matrix. 
- **Gaussian Elimination**: A method for solving systems of linear equations, determining the rank of a matrix, and finding the inverse of an invertible matrix.
- **Determinant**: A scalar value that can be computed from the elements of a square matrix and provides information about the matrix's invertibility.

## Detailed Technical Breakdown

### Announcements
- **Quizzes**: Complete quizzes 2.6 to 2.9 by February 13, 2026.
- **Homework**: Homework 1 is due on February 15, 2026. Ensure submissions are complete and clear.
- **Lecture Schedule**: No lecture next week due to Chinese New Year; students will watch recordings from L2.
- **Midterm Exam**: Scheduled for March 13, 2026, from 1900 to 2000 hours at MPSH.

### Example Problems

#### Question 1(a)
**Task**: Use Gaussian elimination to determine if the following matrix is invertible and find its inverse if it is.

Matrix:
\[
\begin{pmatrix}
-1 & 3 \\
3 & -2
\end{pmatrix}
\]

**Solution**:
1. Form the augmented matrix:
   \[
   \begin{pmatrix}
   -1 & 3 & | & 1 \\
   3 & -2 & | & 0
   \end{pmatrix}
   \]
2. Apply Gaussian elimination to find the reduced row echelon form.

#### Question 1(b)
**Task**: Determine the invertibility of the following matrix:
\[
\begin{pmatrix}
-1 & 3 & -4 \\
2 & 4 & 1 \\
-4 & 2 & -9
\end{pmatrix}
\]

**Solution**:
1. Form the augmented matrix and apply Gaussian elimination.
2. Determine if the matrix can be reduced to the identity matrix.

> [!important] **Note**: A matrix is invertible if its determinant is non-zero.

#### Question 2(a)
**Task**: Write down the conditions for the matrix:
\[
\begin{pmatrix}
1 & 1 & 1 \\
a & b & c \\
a^2 & b^2 & c^2
\end{pmatrix}
\]
to be invertible.

**Conditions**:
- The points \(a\), \(b\), and \(c\) must be distinct.

#### Question 3(a)
**Task**: Solve the matrix equation:
\[
\begin{pmatrix}
2 & 1 & 1 \\
0 & 1 & 2
\end{pmatrix} X = 
\begin{pmatrix}
1 & 0 & 3 \\
1 & 3 & 2
\end{pmatrix}
\]

**Solution**:
1. Use Gaussian elimination to solve for \(X\).

## Implementation/Examples
```matlab
% Example MATLAB code for Gaussian elimination
A = [-1 3; 3 -2];
b = [1; 0];
X = A\b; % Solves the system Ax = b
```

> [!note] **Reminder**: Always check your solutions by substituting back into the original equations.

## Related
- [[Determinants]]
- [[Gaussian Elimination]]
- [[Matrix Inverses]]
- [[Linear Algebra Concepts]]
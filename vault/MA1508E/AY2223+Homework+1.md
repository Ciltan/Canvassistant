---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 1

## Overview
This document outlines the requirements and tasks for Homework 1 in the MA1508E course at the National University of Singapore. It includes instructions for submission, a series of linear algebra problems, and guidelines for using MATLAB in calculations. The homework aims to assess students' understanding of linear systems, matrix equations, determinants, and solution methods.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables.
- **Matrix Equation**: An equation in which the unknowns are represented by matrices.
- **Determinant**: A scalar value that is a function of the entries of a square matrix and provides important properties of the matrix, such as invertibility.
- **Elementary Row Operations**: Operations that can be performed on the rows of a matrix to solve linear systems or find determinants.

## Detailed Technical Breakdown

### Submission Guidelines
- Write answers on A4 size papers or type them digitally.
- Include page numbers on the top right corner.
- Use MATLAB for calculations but show all workings clearly.
- Submit scanned images or a PDF file named as per the format: `StudentNo HW1.pdf`.

### Problem Breakdown
1. **Problem 1**: Consistency of a Linear System
   - (a) Determine if the system is consistent without showing row operations.
   - (b) Solve the matrix equation \( A^TAx = A^Tb \).

2. **Problem 2**: Matrix Equation Solution
   - Find all matrices \( X \) satisfying the given matrix equation.

3. **Problem 3**: Parameterized Solutions
   - Determine values of \( a \) and \( b \) for various solution types (no solution, unique solution, infinitely many solutions).

4. **Problem 4**: Determinants and Invertibility
   - (a) Calculate the determinant of matrix \( A \) using cofactor expansion.
   - (b) Identify values of \( a \) for which \( A \) is invertible.
   - (c) Perform specified row operations and express \( A \) as a product of elementary matrices.

## Implementation/Examples
```matlab
% Example MATLAB code for solving a linear system
A = [1 -1 2; 1 1 2; 2 1 0; 0 1 -1];
b = [1; 0; 1; -1];
x = A\b; % Solving Ax = b
disp(x);
```

> [!note] **Important**: Ensure all workings are shown clearly, even if MATLAB is used for calculations.
> [!warning] **Caution**: Do not compute the determinant using methods other than cofactor expansion along the first column.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Matrix Equations]]
- [[Linear Systems]]
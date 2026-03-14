---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 2 - Homework 2

## Overview
This document outlines the key components of Homework 2 for the MA1508E course, focusing on solving linear systems, computing matrix inverses, and determining determinants. The homework consists of three main questions, each designed to reinforce understanding of linear algebra concepts through practical application. Students are required to submit their work in a specified format to ensure clarity and organization.

## Key Concepts & Definitions
- **Linear System**: A collection of linear equations involving the same set of variables. [[Logic - Propositional Logic]]
- **Matrix Inverse**: A matrix that, when multiplied by the original matrix, yields the identity matrix. [[Determinants]]
- **Elementary Row Operations**: Operations that can be performed on rows of a matrix to simplify it, including row swapping, scaling, and row addition. [[Stacks and Queues]]
- **Determinant**: A scalar value that is a function of a square matrix, providing important properties about the matrix, such as whether it is invertible. [[Determinants]]

## Detailed Technical Breakdown

### Question 1: Solve the Linear System
1. Solve the following system for given values of \( a, b, c \):
   - \( x_1 + x_3 - x_4 = a \)
   - \( x_2 - 2x_4 = b \)
   - \( x_1 + 2x_3 - 2x_4 = c \)

   **Values to Solve:**
   - (i) \( a = -1, b = 1, c = 4 \)
   - (ii) \( a = 1, b = 4, c = 5 \)
   - (iii) \( a = 2, b = 3, c = 5 \)

### Question 2: Matrix Operations
#### (a) Compute the Inverse of Matrix A
Given:
\[ A = \begin{pmatrix} 1 & -2 & 0 \\ 3 & -6 & -3 \\ 1 & 0 & 2 \end{pmatrix} \]
- Perform elementary row operations to find \( A^{-1} \).
- Document each operation clearly.

#### (b) Express A as a Product of Elementary Matrices
Given the row operations:
\[ A \xrightarrow{-R_2 \rightarrow R_1} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 2 \\ 0 & 1/3 & 0 \end{pmatrix} \]
- Write \( A \) as a product of 6 elementary matrices: \( A = E_1 E_2 E_3 E_4 E_5 E_6 \).

#### (c) Compute the Determinant of A
From part (b), compute \( \text{det}(A) \).

### Question 3: Determinant Calculations
Given:
\[ A = \begin{pmatrix} -1 & 0 & -1 & 0 \\ 3 & 2 & 0 & 5 \\ 0 & 0 & 1 & 0 \\ 4 & 1 & 1 & 5 \end{pmatrix} \]
#### (a) Compute the Determinant by Cofactor Expansion
- Use cofactor expansion along the first column.

#### (b) Sum of Entries in Reduced Row-Echelon Form
- Let \( R \) be the reduced row-echelon form of \( A \). Calculate the sum of all entries in \( R \).

#### (c) Determinant of Matrix B
Given \( \text{det}(B) = 3 \):
- (i) Compute \( \text{det}\left(\frac{1}{2} A^T\right) \)
- (ii) Compute \( \text{det}(AB^{-1}) \)
- (iii) Compute \( \text{det}((3B)^{-1}) \)

## Implementation/Examples
```plaintext
# Example of solving a linear system
1. x + 2y = 3
2. 2x - y = 1
```

> [!note] **Submission Guidelines**
> - Write answers on A4 paper, include student number and name on each page, and submit as a single PDF.

> [!important] **Formatting Requirements**
> - Ensure clarity in images when scanning or photographing your work. Follow the naming convention for the PDF file.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Midterm+Briefing]]
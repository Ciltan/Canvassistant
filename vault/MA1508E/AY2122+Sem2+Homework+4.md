---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering Practice 4

## Overview
This document outlines the requirements and tasks for Homework 4 in the MA1508E course at the National University of Singapore. It includes instructions for submission, as well as three mathematical problems focusing on concepts such as orthonormal bases, diagonalization, and eigenvalues. Each problem is designed to assess students' understanding of linear algebra principles and their application in engineering contexts.

## Key Concepts & Definitions
- **Orthonormal Basis**: A basis for a vector space where all vectors are orthogonal and of unit length. 
- **Projection**: The operation of projecting a vector onto a subspace.
- **Diagonalization**: The process of finding a diagonal matrix that is similar to a given matrix.
- **Eigenvalues and Eigenvectors**: Scalars and vectors associated with a linear transformation that describe the factor by which the eigenvector is stretched or compressed.

## Detailed Technical Breakdown

### Problem 1: Orthonormal Basis and Projection
1. **Given**: 
   - Set \( S = \left\{ \begin{pmatrix} -1 \\ 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 1 \\ 0 \\ 2 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \\ 2 \end{pmatrix} \right\} \)
   - Subspace \( V = \text{span}(S) \)

2. **Tasks**:
   - (a) Convert \( S \) into an orthonormal basis for \( V \). Show all workings clearly. [3 marks]
   - (b) Find the projection of \( \begin{pmatrix} 3 \\ 3 \\ 3 \end{pmatrix} \) onto the subspace \( V \). [2 marks]

### Problem 2: Diagonalization
1. **Given**: 
   - Matrix \( A = \begin{pmatrix} 0.5 & 0.4 & 0.2 \\ 0.4 & 0.5 & 0.2 \\ 0.1 & 0.1 & 0.6 \end{pmatrix} \)

2. **Tasks**:
   - (a) Diagonalize \( A \). Show all workings clearly. [6 marks]
   - (b) Find \( \lim_{n \to \infty} A^n \begin{pmatrix} 0.4 \\ 0.2 \end{pmatrix} \). [2 marks]

### Problem 3: Eigenvalues and Differential Systems
1. **Given**: 
   - Matrix \( A = \begin{pmatrix} -3 & 1 & 0 & 1 \\ 1 & 1 & 1 & 0 \\ -1 & 0 & 1 & 3 \\ -1 & 1 & 1 & 0 \end{pmatrix} \)

2. **Tasks**:
   - (a) Show that \( \begin{pmatrix} i \\ 1 \end{pmatrix} \) and \( \begin{pmatrix} 1 \\ 1 \end{pmatrix} \) are eigenvectors of \( A \), where \( i \) is the imaginary unit \( i = \sqrt{-1} \). [2 marks]
   - (b) Solve the differential system:
     \[
     \begin{align*}
     y_1' &= 3y_1 + y_2 - y_4 \\
     y_2' &= y_1 + y_2 + y_3 \\
     y_3' &= -y_2 + 3y_3 - y_4 \\
     y_4' &= y_1 - y_2 - y_4
     \end{align*}
     \]
     with initial conditions \( y_1(0) = y_2(0) = y_3(0) = y_4(0) = 1 \). Show your workings clearly. (Hint: You may use the fact that 2 is a repeated eigenvalue of \( A \)). [5 marks]

## Implementation/Examples
```plaintext
1. Orthonormal Basis Calculation:
   - Use the Gram-Schmidt process to convert \( S \) into an orthonormal basis.
   - Show calculations for each step.

2. Diagonalization of Matrix A:
   - Find eigenvalues by solving \( \text{det}(A - \lambda I) = 0 \).
   - Find corresponding eigenvectors.

3. Differential System Solution:
   - Use eigenvalues to simplify the system.
   - Apply initial conditions to find particular solutions.
```

> [!note] Ensure all answers are clearly written and well-organized. Use A4 size paper for submissions.
> [!important] Remember to scan your work clearly and submit as a single PDF file named by your student number.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Determinants]]
- [[Diagonalization]]
- [[Eigenvalues and Eigenvectors]]
---
tags: [MA1508E, lecture-notes, academic]
---

# MA1508E Linear Algebra for Engineering - Homework 3 Solutions

## Overview
This note summarizes the solutions to Homework 3 for the MA1508E course at the National University of Singapore. The homework covers topics such as orthonormal sets, projection in vector spaces, and eigenvalues of matrices. MATLAB is utilized for calculations, and clear workings are provided for each problem.

## Key Concepts & Definitions
- **Orthonormal Set**: A set of vectors that are all unit vectors and orthogonal to each other. [[Orthonormal Set]]
- **Projection**: The process of projecting a vector onto a subspace spanned by a set of vectors. [[Projection]]
- **Eigenvalue**: A scalar associated with a linear transformation represented by a matrix, indicating how much a corresponding eigenvector is stretched or compressed. [[Eigenvalue]]
- **Transition Matrix**: A square matrix used to describe the transitions of a Markov chain. [[Transition Matrix]]
- **Differential System**: A system of equations involving derivatives of functions. [[Differential System]]

## Detailed Technical Breakdown

### Problem 1: Orthonormal Set and QR Decomposition
1. **Finding an Orthonormal Set**:
   - Given vectors \( a_1, a_2, a_3, a_4 \), find an orthonormal set \( q_1, q_2, q_3, q_4 \) such that \( \text{span}\{a_1, a_2, a_3, a_4\} = \text{span}\{q_1, q_2, q_3, q_4\} \).
   - Use the Gram-Schmidt process to derive \( q_i \).

2. **QR Decomposition**:
   - Express matrix \( A \) as \( A = QR \) where \( Q \) is orthonormal and \( R \) is upper triangular.
   - Calculate \( R \) using \( R = Q^T A \).

### Problem 2: Telecommunication Service Providers
1. **Transition Matrix**:
   - Construct the transition matrix \( A \) based on subscriber changes between telcos A, B, and C.
   - Calculate the proportion of subscribers after 5 years using \( A^5 \).

2. **Long-term Subscribers**:
   - Determine the stable equilibrium by finding the eigenvector associated with eigenvalue 1.

### Problem 3: Differential System
1. **Eigenvalue Calculation**:
   - Show that \( 2+i \) is an eigenvalue of matrix \( A \) and find a corresponding eigenvector.
   - Construct complex solutions from the eigenvalue.

2. **Real Solutions**:
   - Derive independent real solutions from the complex solutions obtained.

## Implementation/Examples

### MATLAB Code Snippet for QR Decomposition
```matlab
% Given matrix A
A = [0 -1 1 1; 1 0 1 1; -1 1 1 1; 0 -1 0 0];

% QR Decomposition
[Q, R] = qr(A);
disp('Orthonormal Matrix Q:');
disp(Q);
disp('Upper Triangular Matrix R:');
disp(R);
```

> [!note] **Important**: Ensure all workings are shown clearly when submitting your homework. Use MATLAB to aid calculations but do not rely solely on it for solutions.

> [!warning] **Submission Guidelines**: Submit your answers as a single PDF file named by your student number followed by "HW3". Ensure clarity in scanned images if handwritten.

## Related
- [[AY2122+Sem1+Homework+3]]
- [[AY2122+Sem2+Homework+3]]
- [[Matlab+for+Engineering]]
- [[Determinants]]
- [[Logic - Propositional Logic]]